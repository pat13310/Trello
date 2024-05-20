// tailwind.config.js
module.exports = {
  content: [
    './templates/**/*.html',
    './boards/templates/**/*.html',
    // Ajoutez d'autres chemins si nécessaire
  ],
  theme: {
    extend: {
      colors: {
        'bg-primary':'#1c39cc',
        'bg-secondary':'#0a1f88',
        'accent': '#99a7f1', // Bleu encore plus clair
        'accent-2': '#bbc3ef', // Bleu encore plus clair
        'gray-1':'#F1F2F4',
      },
      backgroundImage: theme => ({
        'gradient-to-r': 'linear-gradient(to right, #1D4ED8, #3B82F6, #93C5FD)',
        'gradient-to-l': 'linear-gradient(to left, #1D4ED8, #3B82F6, #93C5FD)',
        'gradient-to-b': 'linear-gradient(to bottom, #99a7f1, #bbc3ef, #F1F2F4 100%)',
      })
    },
  },
  plugins: [],
}
