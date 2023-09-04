document.addEventListener('DOMContentLoaded', function() {
    const popupContainer = document.querySelector('.ransomware-container');
    const popupOverlay = document.querySelector('.ransomware-overlay');

    // Disable right-click to prevent user from inspecting element
    document.addEventListener('contextmenu', function(event) {
        event.preventDefault();
    });

    // Disable keyboard shortcuts (Ctrl+U, Ctrl+Shift+I)
    document.addEventListener('keydown', function(event) {
        if (event.ctrlKey && (event.key === 'u' || event.key === 'i')) {
            event.preventDefault();
        }
    });

    popupOverlay.addEventListener('click', function() {
        popupContainer.style.display = 'none';
        popupOverlay.style.display = 'none';
    });

    // Display the pop-up
    popupContainer.style.display = 'block';
    popupOverlay.style.display = 'block';
});
