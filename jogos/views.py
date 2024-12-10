from django.shortcuts import render,redirect
from .models import Jogo, Presenca
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404



# Create your views here.

class JogoListView(ListView):
  model = Jogo
  template_name = 'jogos/jogos.html'
  context_object_name = 'jogos'
  paginate_by = 10
  ordering = '-data_jogo'
  queryset = Jogo.objects.all()

class JogoDetailView(DetailView):
  model = Jogo
  template_name = 'jogos/jogo.html'
  pk_url_kwarg = 'id'
  context_object_name = 'jogo'
  
class JogoCreateView(CreateView):
  model = Jogo
  fields = '__all__'
  template_name = 'jogos/cadastrar_jogo.html'
  success_url = reverse_lazy('jogos')

class JogoUpdateView(UpdateView):
  model = Jogo
  fields = '__all__'
  template_name = 'jogos/atualizar_jogo.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('jogos')

class JogoDeleteView(DeleteView):
  model = Jogo
  template_name = 'jogos/deletar_jogo.html'
  pk_url_kwarg = 'id'
  success_url = reverse_lazy('jogos')

class PresencaListView(ListView):
  model = Presenca
  template_name = 'presencas/presencas.html'
  context_object_name = 'presencas'
  paginate_by = 11
  
  def get_queryset(self):
    jogo_id = self.kwargs['jogo_id']
    return Presenca.objects.filter(jogo_id=jogo_id)
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    jogo = get_object_or_404(Jogo, id=self.kwargs['jogo_id'])
    context['jogo'] = jogo
    return context

def criar_presenca(jogo, usuario, confirmado=False):
    # Verificar duplicatas
    if Presenca.objects.filter(jogo=jogo, usuario=usuario).exists():
        return {"success": False, "detail": "Você já marcou presença neste jogo."}
    
    # Criar a presença
    presenca = Presenca.objects.create(jogo=jogo, usuario=usuario, confirmado=confirmado)
    return {"success": True, "presenca": presenca}

class MarcarPresencaView(View):
    def get(self, request, *args, **kwargs):
        jogo_id = kwargs['jogo_id']
        jogo = get_object_or_404(Jogo, id=jogo_id)
        return render(request, "presencas/cadastrar_presenca.html", {"jogo": jogo})
    
    def post(self, request, *args, **kwargs):
        jogo_id = kwargs['jogo_id']
        jogo = get_object_or_404(Jogo, id=jogo_id)
        confirmado = request.POST.get("confirmado","off") == "on"
        
        # Reutilizando a lógica
        resultado = criar_presenca(jogo, request.user, confirmado=confirmado)
        
        if not resultado["success"]:
            return render(request, "presencas/erro.html", {"error": resultado["detail"]})
        
        return redirect("presencas", jogo_id=jogo.id)

  