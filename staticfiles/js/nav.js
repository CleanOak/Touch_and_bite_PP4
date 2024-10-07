
window.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.nav-link');

    // Automatically set 'active-link' based on current URL
    navLinks.forEach(link => {
        if (link.href === window.location.href) {
            link.classList.add('active-link');
        }
    });

    navLinks.forEach(link => {
        link.addEventListener('click', function () {
            navLinks.forEach(l => l.classList.remove('active-link'));
            this.classList.add('active-link');
        });
    });
});
