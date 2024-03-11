let slideIndex = 0;
let slideshowTimeout; // Store the timeout ID

showSlides();

// Next/previous controls
function plusSlides(n) {
  // Clear the automatic slideshow timeout
    clearTimeout(slideshowTimeout);
    slideIndex += n
    showSlides();
}

// Thumbnail image controls
function currentSlide(n) {
  // Clear the automatic slideshow timeout
    clearTimeout(slideshowTimeout);
    slideIndex = n
    showSlides();
}

function showSlides() {
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");

  // Hide all slides
    for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
}
    for (let i = 0; i < dots.length; i++) {
        dots[i].style.backgroundColor = "#ffffff73";
    }

  // Move to the next slide
    slideIndex++;

  // Reset to the first slide if the end is reached
    if (slideIndex > slides.length) {
    slideIndex = 1;
}
    console.log(slideIndex)
  // Display the current slide
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].style.backgroundColor = "white";

  // Change slide every 2 seconds
    slideshowTimeout = setTimeout(showSlides, 2000);
}
