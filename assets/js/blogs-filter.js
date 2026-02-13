// Blogs page tag filtering (ES5 for Jekyll compatibility)
// Mirrors the events-filter.js approach for consistency
(function() {
  'use strict';
  
  var activeTag = 'all';
  var activeOrg = 'all';
  var blogCards = document.querySelectorAll('.blog-card');
  var yearHeaders = document.querySelectorAll('.year-header');
  var visibleCountEl = document.getElementById('visible-count');
  
  function updateVisibleCount() {
    var count = 0;
    for (var i = 0; i < blogCards.length; i++) {
      if (blogCards[i].style.display !== 'none') {
        count++;
      }
    }
    if (visibleCountEl) {
      visibleCountEl.textContent = count;
    }
  }
  
  function updateYearHeaders() {
    for (var i = 0; i < yearHeaders.length; i++) {
      var header = yearHeaders[i];
      var year = header.getAttribute('data-year');
      var container = header.nextElementSibling;
      var hasVisible = false;
      
      if (container && container.classList.contains('posts-container')) {
        var cards = container.querySelectorAll('.blog-card');
        for (var j = 0; j < cards.length; j++) {
          if (cards[j].style.display !== 'none') {
            hasVisible = true;
            break;
          }
        }
      }
      
      header.style.display = hasVisible ? '' : 'none';
      if (container) {
        container.style.display = hasVisible ? '' : 'none';
      }
    }
  }
  
  function applyFilters() {
    for (var i = 0; i < blogCards.length; i++) {
      var card = blogCards[i];
      var cardTags = card.getAttribute('data-tags') || '';
      var cardOrg = card.getAttribute('data-org') || '';
      
      var matchesTag = (activeTag === 'all') || (cardTags.indexOf(activeTag) !== -1);
      var matchesOrg = (activeOrg === 'all') || (cardOrg === activeOrg);
      
      card.style.display = (matchesTag && matchesOrg) ? '' : 'none';
    }
    
    updateVisibleCount();
    updateYearHeaders();
  }
  
  // Expose filter functions globally
  window.filterBlogs = function(tag, button) {
    activeTag = tag;
    
    // Update active state for tag buttons
    var tagButtons = document.querySelectorAll('.tag-filter[data-tag]');
    for (var i = 0; i < tagButtons.length; i++) {
      tagButtons[i].classList.remove('active');
    }
    if (button) {
      button.classList.add('active');
    }
    
    applyFilters();
    
    // Update URL hash for deep linking
    if (tag !== 'all') {
      window.history.replaceState(null, '', '#' + tag);
    } else if (activeOrg === 'all') {
      window.history.replaceState(null, '', window.location.pathname);
    }
  };
  
  window.filterByOrg = function(org, button) {
    activeOrg = org;
    
    // Update active state for org buttons
    var orgButtons = document.querySelectorAll('.tag-filter[data-org]');
    for (var i = 0; i < orgButtons.length; i++) {
      orgButtons[i].classList.remove('active');
    }
    if (button) {
      button.classList.add('active');
    }
    
    applyFilters();
    
    // Update URL hash (org filters use org- prefix)
    if (org !== 'all') {
      window.history.replaceState(null, '', '#org-' + org.toLowerCase().replace(/\s+/g, '-'));
    } else if (activeTag === 'all') {
      window.history.replaceState(null, '', window.location.pathname);
    }
  };
  
  // Handle hash-based deep links on page load
  function handleHashOnLoad() {
    var hash = window.location.hash.slice(1); // Remove #
    if (!hash) return;
    
    // Check if it's an organization filter (org-worldbank, org-unicef, etc.)
    if (hash.indexOf('org-') === 0) {
      var orgMap = {
        'org-world-bank': 'World Bank',
        'org-worldbank': 'World Bank',
        'org-unicef': 'UNICEF',
        'org-brookings': 'Brookings',
        'org-linkedin': 'LinkedIn'
      };
      var org = orgMap[hash];
      if (org) {
        var orgButton = document.querySelector('.tag-filter[data-org="' + org + '"]');
        if (orgButton) {
          window.filterByOrg(org, orgButton);
        }
      }
    } else {
      // It's a tag filter
      var tagButton = document.querySelector('.tag-filter[data-tag="' + hash + '"]');
      if (tagButton) {
        window.filterBlogs(hash, tagButton);
      }
    }
  }
  
  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', handleHashOnLoad);
  } else {
    handleHashOnLoad();
  }
  
  // Initialize count on page load
  updateVisibleCount();
})();
