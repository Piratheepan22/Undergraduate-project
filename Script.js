
/* Script.js */
// script.js
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Add current date to Week pages if they have the date class
    const dateElement = document.querySelector('.date');
    if (dateElement) {
        const currentDate = new Date();
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        dateElement.innerHTML = `Last Updated: ${currentDate.toLocaleDateString('en-US', options)}`;
    }
});