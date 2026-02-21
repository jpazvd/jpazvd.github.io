// Teaching Filter - Global function pattern (matches blogs.html)
window.filterTeaching = function(tag, button) {
  // Update button active state
  var buttons = document.querySelectorAll('.tag-filter');
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].classList.remove('active');
  }
  if (button) {
    button.classList.add('active');
  }

  // Get all cards
  var cards = document.querySelectorAll('.teaching-card');
  var visibleCount = 0;

  // Show/hide cards based on tag
  for (var j = 0; j < cards.length; j++) {
    var card = cards[j];
    var cardTags = card.getAttribute('data-tags') || '';
    var tagArray = cardTags.split(',');

    var isVisible = (tag === 'all');
    if (!isVisible) {
      for (var k = 0; k < tagArray.length; k++) {
        if (tagArray[k].trim() === tag) { isVisible = true; break; }
      }
    }
    card.style.display = isVisible ? 'block' : 'none';
    if (isVisible) { visibleCount++; }
  }

  // Update visible count
  var allCountEl = document.getElementById('all-count');
  if (allCountEl) {
    allCountEl.textContent = visibleCount;
  }

  // Update year divider visibility
  updateYearDividers();

  // Update URL hash for deep linking
  if (tag !== 'all') {
    window.history.replaceState(null, '', '#' + tag);
  } else {
    window.history.replaceState(null, '', window.location.pathname);
  }
};

function updateYearDividers() {
  var headers = document.querySelectorAll('.year-divider');
  var cards = document.querySelectorAll('.teaching-card');
  for (var i = 0; i < headers.length; i++) {
    var header = headers[i];
    var year = header.getAttribute('data-year');
    var hasVisible = false;
    for (var j = 0; j < cards.length; j++) {
      var card = cards[j];
      if (card.style.display === 'none') { continue; }
      if (card.getAttribute('data-year') === year) {
        hasVisible = true;
        break;
      }
    }
    header.style.display = hasVisible ? 'block' : 'none';
  }
}

// Handle hash-based deep links and initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  updateYearDividers();

  var hash = window.location.hash.slice(1);
  if (hash) {
    var tagButton = document.querySelector('.tag-filter[data-tag="' + hash + '"]');
    if (tagButton) {
      window.filterTeaching(hash, tagButton);
    }
  }
});
