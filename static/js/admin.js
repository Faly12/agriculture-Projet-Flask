function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    // Sauvegarde le mode dans le localStorage
    const isDark = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDark ? 'enabled' : 'disabled');
}

// Appliquer automatiquement au chargement
window.addEventListener('DOMContentLoaded', () => {
    if (localStorage.getItem('darkMode') === 'enabled') {
        document.body.classList.add('dark-mode');
    }
});

function updateCartCount() {
    fetch('/cart_count')
      .then(response => response.json())
      .then(data => {
        document.getElementById('cart-count').textContent = data.count;
      });
  }

  // Appel au chargement de la page
  updateCartCount();