document.addEventListener("DOMContentLoaded", function () {
    //Function for making drop-down work on sidebar
  const dropdownButtons = document.querySelectorAll('.dropdown-btn');

  dropdownButtons.forEach(button => {
    button.addEventListener('click', function(e) {
        e.stopPropagation
    })
  })
});



