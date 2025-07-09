document.addEventListener("DOMContentLoaded", () => {
  //Drop down menu functionality
  document.querySelectorAll(".dropdown-btn").forEach((button) => {
    button.addEventListener("click", () => {
      const dropdown = button.parentElement;
      dropdown.classList.toggle("active");
    });
  });

  //Hover cascade for star ratings
  const stars = document.querySelectorAll(".star");
  const selectedRatingInput = document.getElementById("selected-rating");
  let selectedRating = 0;

  stars.forEach((star, index) => {
    star.addEventListener("mouseenter", () => {
      clearStars();
      highlightStars(index);
    });

    star.addEventListener("mouseleave", () => {
      if (selectedRating == 0) {
        clearStars();
      } else {
        highlightStars(selectedRating - 1);
      }

      star.addEventListener("click", () => {
        selectedRating = index + 1;
        selectedRatingInput.value = selectedRating;
        highlightStars(index);
      });
    });
  });

  function highlightStars(index) {
    for (let i = 0; i <= index; i++) {
      stars[i].classList.add("active");
    }
  }
  function clearStars() {
    stars.forEach((star) => {
      star.classList.remove("active");
    });
  }
});

//Price slider functionality
function updateDualSlider() {
  const minSlider = document.querySelector("#minPrice");
  const maxSlider = document.querySelector("#maxPrice");
  const minDisplay = document.getElementById("minPriceDisplay");
  const maxDisplay = document.getElementById("maxPriceDisplay");

  let minimum = parseInt(minSlider.value);
  let maximum = parseInt(maxSlider.value);

  if (minimum > maximum) {
    [minSlider.value, maxSlider.value] = [maximum, minimum];
    let xminimum = minimum;
    minimum = maximum;
    maximum = xminimum;
  }

  minDisplay.textContent = `$${minimum}`;
  maxDisplay.textContent = `$${maximum}`;
}
