document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.filter-btn');
    const items = document.querySelectorAll('.gallery-item');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const filter = button.getAttribute('data-filter');
            items.forEach(item => {
                item.style.display = (filter === 'all' || item.getAttribute('data-category') === filter) ? 'block' : 'none';
            });
        });
    });

    // Zoom modal
    document.querySelectorAll('.zoomable').forEach(img => {
        img.addEventListener('click', function () {
            const modal = document.getElementById('zoomModal');
            const modalImg = document.getElementById('zoomedImg');
            modal.style.display = "block";
            modalImg.src = this.src;
        });
    });

    document.querySelector('.zoom-close').addEventListener('click', function () {
        document.getElementById('zoomModal').style.display = "none";
    });

    document.getElementById('zoomModal').addEventListener('click', function (e) {
        if (e.target === this) {
            this.style.display = "none";
        }
    });
});