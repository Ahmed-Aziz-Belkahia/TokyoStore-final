// Global variables
const tabContainer = document.querySelector('.secondtabcontainer');
const tabs = tabContainer.querySelectorAll('.tabbuttonsecond');
const tabPanels = document.querySelectorAll('.tabpanelsecond');

// Function to handle tab change
function handleTabChange(clickedTab) {
    // Hide all tab panels
    tabPanels.forEach(panel => panel.hidden = true);
    // Mark all tabs as unselected
    tabs.forEach(tab => tab.setAttribute('aria-selected', 'false'));

    // Show the selected tab panel
    const panelId = clickedTab.getAttribute('aria-controls');
    const panel = document.getElementById(panelId);
    panel.hidden = false;
    // Mark the clicked tab as selected
    clickedTab.setAttribute('aria-selected', 'true');

    // Initialize slick carousel for the shown panel if not already initialized
    if (!panel.classList.contains('slick-initialized')) {
        $.HSCore.components.HSSlickCarousel.init('#' + panelId);
    }
}

// Event listener for tab click
tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        handleTabChange(tab);
    });
});

// Initialize slick carousel for the initially visible tab panel on page load
document.addEventListener('DOMContentLoaded', function () {
    // Initialize slick carousel for the first tab panel initially visible
    const initialTab = document.querySelector('.tabbuttonsecond[aria-selected="true"]');
    const panelId = initialTab.getAttribute('aria-controls');
    $.HSCore.components.HSSlickCarousel.init('#' + panelId);
});
