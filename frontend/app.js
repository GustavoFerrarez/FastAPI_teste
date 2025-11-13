const login = document.getElementById('login');
const menu = document.getElementById('menu');
const form = document.getElementById('loginForm');
const logout = document.getElementById('logout');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = document.getElementById('email').value.trim();
  const pass = document.getElementById('password').value.trim();

  if (email && pass) {
    login.classList.add('hidden');
    menu.classList.remove('hidden');
  } else {
    alert('Por favor, preencha todos os campos!');
  }
});

logout.addEventListener('click', () => {
  menu.classList.add('hidden');
  login.classList.remove('hidden');
  form.reset();
});
