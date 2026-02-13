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
  
  // Add click handlers to filter buttons
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].addEventListener('click', function() {
      var filter = this.getAttribute('data-filter');
      
      // Update active button
      for (var j = 0; j < buttons.length; j++) {
        buttons[j].classList.remove('active');
      }
      this.classList.add('active');
      
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
    });
  }
})();
