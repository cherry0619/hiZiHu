function toggleDarkMode() {
  var body = document.querySelector('body');
  // here we use toggle method: if the tag does not exist, then appends it to the class, otherwise remove it.
  body.classList.toggle('dark-mode');
}


const darkModeButton = document.getElementById('darkMode');
darkModeButton.addEventListener('click', toggleDarkMode);