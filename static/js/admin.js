
function updateCartCount() {
    fetch('/cart_count')
      .then(response => response.json())
      .then(data => {
        document.getElementById('cart-count').textContent = data.count;
      });
  }

  // Appel au chargement de la page
  updateCartCount();


  //fonction dark /light mode

  const darkModeStyles = `
  body.dark-mode {
    background-color: #121212;
    color: #fff;
  }
  .navbar.dark-mode,
  .footer.dark-mode {
    background-color: #1f1f1f;
  }
  .card.dark-mode {
    background-color: #2a2a2a;
    color: white;
  }
  .dark-mode .nav-link {
    color: rgba(2, 2, 2, 0.82) !important;
  }
`;

const styleSheet = document.createElement("style");
styleSheet.type = "text/css";
styleSheet.innerText = darkModeStyles;
document.head.appendChild(styleSheet);

// 2. Fonction pour basculer entre dark et light mode
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
  document.querySelectorAll('.navbar, .footer, .card')
    .forEach(el => el.classList.toggle('dark-mode'));

  const paramLink = document.getElementById("paramLink");
  if (document.body.classList.contains("dark-mode")) {
    localStorage.setItem("theme", "dark");
    if (paramLink) paramLink.innerHTML = '<i class="bi bi-moon me-2"></i>Mode clair';
  } else {
    localStorage.setItem("theme", "light");
    if (paramLink) paramLink.innerHTML = '<i class="bi bi-moon me-2"></i>Mode sombre';
  }
}

// 3. Appliquer le thème enregistré au chargement de la page
window.onload = function () {
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
    document.querySelectorAll('.navbar, .footer, .card')
      .forEach(el => el.classList.add('dark-mode'));
    const paramLink = document.getElementById("paramLink");
    if (paramLink) {
      paramLink.innerHTML = '<i class="bi bi-gear me-2"></i>Mode clair';
    }
  }
};

$(document).ready(function () {
    $('#userTable').DataTable({
      language: {
        url: '//cdn.datatables.net/plug-ins/1.13.4/i18n/fr-FR.json'
      }
    });
  });

  var deleteModal = document.getElementById('deleteModal');
  deleteModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget;
    var userId = button.getAttribute('data-user-id');
    var userName = button.getAttribute('data-user-name');

    // Met à jour le contenu de la modale
    var userNameElem = deleteModal.querySelector('#userNameToDelete');
    var userIdInput = deleteModal.querySelector('#userIdToDelete');

    userNameElem.textContent = userName;
    userIdInput.value = userId;
  });


  // fonction de recherche de produit 

  document.getElementById('searchInput').addEventListener('input', function () {
    const filter = this.value.toLowerCase();
    const rows = document.querySelectorAll('table tbody tr');

    rows.forEach(row => {
      const text = row.textContent.toLowerCase();
      row.style.display = text.includes(filter) ? '' : 'none';
    });
  });