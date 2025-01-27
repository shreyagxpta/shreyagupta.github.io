document.addEventListener("DOMContentLoaded", () => {
    console.log("Welcome to Shreya Gupta's website!");

    const carousel = document.querySelector('.carousel');
    const slides = document.querySelectorAll('.carousel-slide');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    let currentIndex = 0; // Track the current slide index
    let isPaused = false; // Track whether the carousel is paused
    let interval;

    // Function to update the carousel's position
    function updateCarousel() {
        const offset = -currentIndex * 100; // Calculate the offset for translateX
        carousel.style.transform = `translateX(${offset}%)`;
    }

    // Function to move to the next slide
    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length; // Loop back to the first slide
        updateCarousel();
    }

    // Function to move to the previous slide
    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length; // Loop back to the last slide
        updateCarousel();
    }

    // Function to start the auto-sliding
    function startCarousel() {
        interval = setInterval(nextSlide, 3000); // Change slide every 3 seconds
    }

    // Function to stop the auto-sliding
    function stopCarousel() {
        clearInterval(interval);
    }

    // Add event listeners for buttons
    nextBtn.addEventListener('click', () => {
        stopCarousel(); // Stop auto-sliding
        nextSlide();
        if (!isPaused) startCarousel(); // Resume auto-sliding if not paused
    });

    prevBtn.addEventListener('click', () => {
        stopCarousel(); // Stop auto-sliding
        prevSlide();
        if (!isPaused) startCarousel(); // Resume auto-sliding if not paused
    });

    // Add event listener to pause/play on click
    carousel.addEventListener('click', () => {
        if (isPaused) {
            startCarousel();
        } else {
            stopCarousel();
        }
        isPaused = !isPaused; // Toggle pause state
    });

    // Start the carousel initially
    startCarousel();
});
