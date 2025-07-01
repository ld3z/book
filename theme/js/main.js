import FloatingVue from 'floating-vue';
import 'floating-vue/dist/style.css';

function initTooltips() {
    // Disable tooltips on mobile for a better user experience
    FloatingVue.options.themes.tooltip.disabled = window.matchMedia('(max-width: 768px)').matches;

    // Find all tooltip spans that haven't been initialized yet
    document.querySelectorAll('span.tooltip:not([data-v-tooltip])').forEach(el => {
        const content = el.dataset.tooltipContent;
        if (content) {
            FloatingVue.setTooltip(el, {
                content: content,
                html: true, // Allow HTML in tooltips
            });
        }
    });
}

// Run on initial page load
initTooltips();

// mdbook loads new pages dynamically. We use a MutationObserver to detect
// when the page content changes and re-initialize the tooltips.
const observer = new MutationObserver(() => {
    initTooltips();
});

const targetNode = document.getElementById('content');
if (targetNode) {
    observer.observe(targetNode, { childList: true, subtree: true });
}

