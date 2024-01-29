document.addEventListener('DOMContentLoaded', function () {
    // Options for the IntersectionObserver
    const options = {
        root: null, // Use the viewport as the root
        threshold: 0.5 // Trigger when 50% of the element is visible
    };

    // Callback function to handle the intersection
    const handleIntersection = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = entry.target;
                const targetCount = parseFloat(target.textContent.replace(',', '').trim());
                let currentCount = 0;
                const duration = 2000; // Duration in milliseconds
                const steps = 100; // Number of steps
                const increment = targetCount / steps; // Increment per step
                let step = 0;

                const interval = setInterval(() => {
                    currentCount += increment;
                    if (currentCount >= targetCount) {
                        clearInterval(interval);
                        currentCount = targetCount;
                    }
                    target.textContent = Math.round(currentCount).toLocaleString();
                    step++;
                    if (step >= steps) {
                        clearInterval(interval);
                    }
                }, duration / steps);
                observer.unobserve(target);
            }
        });
    };

    // Create the IntersectionObserver
    const observer = new IntersectionObserver(handleIntersection, options);

    // Observe each counter-up element
    const counterUpElements = document.querySelectorAll('[data-toggle="counter-up"]');
    counterUpElements.forEach(element => observer.observe(element));
});
