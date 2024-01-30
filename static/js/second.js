    document.addEventListener('DOMContentLoaded', (event) => {
            const sections = document.querySelectorAll('section');
            const navLinks = document.querySelectorAll('.nav-link');

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    const id = entry.target.getAttribute('id');
                    const navLink = document.querySelector(`.nav-link[href="#${id}"]`);
                    if (entry.isIntersecting) {
                        navLink.classList.add('active');
                    } else {
                        navLink.classList.remove('active');
                    }
                });
            }, { threshold: 0.5 });

            sections.forEach(section => {
                observer.observe(section);
            });

            // Function to scroll to section with an offset
            const scrollToSection = (id) => {
                const section = document.querySelector(id);
                const offset = 100; // Adjust this offset as needed
                const sectionPosition = section.offsetTop - offset;
                window.scrollTo({
                    top: sectionPosition,
                    behavior: 'smooth'
                });
            };

            // Adding click event listeners to nav links
            navLinks.forEach(navLink => {
                navLink.addEventListener('click', (event) => {
                    event.preventDefault();
                    const targetId = navLink.getAttribute('href');
                    scrollToSection(targetId);
                });
            });
        });