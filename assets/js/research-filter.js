// Research page filtering
(function() {
  'use strict';

  var buttons = document.querySelectorAll('.tag-filter');
  var sections = document.querySelectorAll('.research-section');
  var allCountEl = document.getElementById('all-count');

  // Update all count
  if (allCountEl) {
    allCountEl.textContent = sections.length;
  }

  function filterResearch(filter) {
    // Filter sections
    for (var k = 0; k < sections.length; k++) {
      var section = sections[k];
      var theme = section.getAttribute('data-theme');
      if (filter === 'all' || theme === filter) {
        section.classList.remove('hidden');
      } else {
        section.classList.add('hidden');
      }
    }

    // Update URL hash for deep linking
    if (filter !== 'all') {
      window.history.replaceState(null, '', '#' + filter);
    } else {
      window.history.replaceState(null, '', window.location.pathname);
    }
  }

  // Add click handlers to filter buttons
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      var filter = this.getAttribute('data-filter');

      // Update active button
      for (var j = 0; j < buttons.length; j++) {
        buttons[j].classList.remove('active');
      }
      this.classList.add('active');

      filterResearch(filter);
    });
  }

  // Handle hash-based deep links on page load
  var hash = window.location.hash.slice(1);
  if (hash) {
    var targetButton = document.querySelector('.tag-filter[data-filter="' + hash + '"]');
    if (targetButton) {
      for (var j = 0; j < buttons.length; j++) {
        buttons[j].classList.remove('active');
      }
      targetButton.classList.add('active');
      filterResearch(hash);
    }
  }
})();
