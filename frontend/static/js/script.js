document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.dropdown-btn').forEach(button => {
    button.addEventListener('click', () => {
      const dropdown = button.parentElement;
      dropdown.classList.toggle('active');
    });
  });
});
