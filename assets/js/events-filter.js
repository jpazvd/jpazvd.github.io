// Events page tag filtering (ES5 for Jekyll compatibility)
(function() {
  'use strict';

  var filterButtons = document.querySelectorAll('.tag-filter');
  var eventCards = document.querySelectorAll('.event-card');
  var yearDividers = document.querySelectorAll('.year-divider');
  var allCountEl = document.getElementById('all-count');

  function updateVisibleCount() {
    var visibleCards = document.querySelectorAll('.event-card:not(.hidden)');
    if (allCountEl) {
      allCountEl.textContent = visibleCards.length;
    }
  }

  function updateYearDividers() {
    // Hide year dividers that have no visible events after them
    for (var i = 0; i < yearDividers.length; i++) {
      var divider = yearDividers[i];
      var year = divider.getAttribute('data-year');
      var hasVisibleEvent = false;

      // Check if any visible event card belongs to this year
      for (var j = 0; j < eventCards.length; j++) {
        var card = eventCards[j];
        if (!card.classList.contains('hidden') && card.getAttribute('data-year') === year) {
          hasVisibleEvent = true;
          break;
        }
      }

      divider.style.display = hasVisibleEvent ? 'block' : 'none';
    }
  }

  function filterEvents(selectedTag) {
    for (var i = 0; i < eventCards.length; i++) {
      var card = eventCards[i];
      var cardTags = card.getAttribute('data-tags');

      if (selectedTag === 'all') {
        card.classList.remove('hidden');
      } else if (cardTags && cardTags.indexOf(selectedTag) !== -1) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    }

    updateVisibleCount();
    updateYearDividers();

    // Update URL hash for deep linking
    if (selectedTag !== 'all') {
      window.history.replaceState(null, '', '#' + selectedTag);
    } else {
      window.history.replaceState(null, '', window.location.pathname);
    }
  }

  // Attach click handlers to filter buttons
  for (var i = 0; i < filterButtons.length; i++) {
    filterButtons[i].addEventListener('click', function(e) {
      var button = e.currentTarget;
      var tag = button.getAttribute('data-tag');

      // Update active state
      for (var j = 0; j < filterButtons.length; j++) {
        filterButtons[j].classList.remove('active');
      }
      button.classList.add('active');

      // Filter events
      filterEvents(tag);
    });
  }

  // Handle hash-based deep links on page load
  function handleHashOnLoad() {
    var hash = window.location.hash.slice(1);
    if (!hash) return;

    var tagButton = document.querySelector('.tag-filter[data-tag="' + hash + '"]');
    if (tagButton) {
      for (var j = 0; j < filterButtons.length; j++) {
        filterButtons[j].classList.remove('active');
      }
      tagButton.classList.add('active');
      filterEvents(hash);
    }
  }

  handleHashOnLoad();
})();
