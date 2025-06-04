const forms = document.querySelectorAll('.add-to-cart-form');
const cartCount = document.getElementById('cart-count');

function showRegister() {
    document.getElementById('loginForm').classList.add('d-none');
    document.getElementById('registerForm').classList.remove('d-none');
  }

  function showLogin() {
    document.getElementById('registerForm').classList.add('d-none');
    document.getElementById('loginForm').classList.remove('d-none');
  }
  
  function incrementCartCount() {
    const counter = document.getElementById('cart-count');
    let count = parseInt(counter.textContent);
    counter.textContent = count + 1;
  }

// Add event listener to all add-to-cart forms
document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('.add-to-cart-form'); 
    
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        incrementCartCount();
      });
    });
  });

  
//recherche
document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("searchInput").style.display="block";
  const resultsContainer = document.getElementById("searchResults");

  input.addEventListener("input", function () {
      const query = input.value.trim();

      if (query.length === 0) {
          resultsContainer.innerHTML = ""; 
          return;
      }

      fetch(`/searchContainer/${encodeURIComponent(query)}`)
          .then(response => response.text())
          .then(html => {
              resultsContainer.innerHTML = html;
          })
          .catch(error => {
              console.error("Erreur lors de la recherche :", error);
              resultsContainer.innerHTML = "<div class='text-danger'>Erreur lors de la recherche.</div>";
          });
  });
});


function showRegister() {
  document.getElementById("loginForm").classList.add("d-none");
  document.getElementById("registerForm").classList.remove("d-none");
}

function showLogin() {
  document.getElementById("registerForm").classList.add("d-none");
  document.getElementById("loginForm").classList.remove("d-none");
}

function toggleSearchField() {
  const input = document.getElementById("searchInput");
  input.focus();
}

//agrandir un block 