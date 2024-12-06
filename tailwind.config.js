module.exports = {
  content: [
    '../templates/**/*.html',  // Caminho para os templates do Django
    '../**/templates/**/*.html', // Inclui templates em outros apps do Django
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};

