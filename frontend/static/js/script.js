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
  const minSlider = document.getElementById("minPrice");
  const maxSlider = document.getElementById("maxPrice");
  const minDisplay = document.getElementById("minPriceDisplay");
  const maxDisplay = document.getElementById("maxPriceDisplay");
  const rangeFill = document.getElementById("rangeFill");

  let min = parseInt(minSlider.value);
  let max = parseInt(maxSlider.value);

  if (min > max) {
    [min, max] = [max, min];
  }

  minDisplay.textContent = `$${min}`;
  maxDisplay.textContent = `$${max}`;

  const rangeMin = parseInt(minSlider.min);
  const rangeMax = parseInt(minSlider.max);

  const left = ((min - rangeMin) / (rangeMax - rangeMin)) * 100;
  const right = ((max - rangeMin) / (rangeMax - rangeMin)) * 100;

  rangeFill.style.left = `${left}%`;
  rangeFill.style.width = `${right - left}%`;
}
