document.addEventListener('DOMContentLoaded', function() {
  var username = 'jpazvd';
  var reposPerPage = 100;
  
  // Load tag data from YAML (passed via Liquid)
  var repoTagsData = {};
  try {
    var tagDataEl = document.getElementById('repo-tags-data');
    if (tagDataEl) {
      var tagArray = JSON.parse(tagDataEl.textContent);
      for (var i = 0; i < tagArray.length; i++) {
        repoTagsData[tagArray[i].name] = tagArray[i];
      }
    }
  } catch (e) {
    console.warn('Could not parse repo tags data:', e);
  }
  
  // Get tags for a repo
  function getRepoTags(repoName) {
    return repoTagsData[repoName] ? repoTagsData[repoName].tags || [] : [];
  }
  
  // Check if repo is featured
  function isFeatured(repoName) {
    return repoTagsData[repoName] ? repoTagsData[repoName].featured === true : false;
  }
  
  // Check if repo should be hidden
  function isHidden(repoName) {
    return repoTagsData[repoName] ? repoTagsData[repoName].hide === true : false;
  }
  
  // Fetch all repos
  function fetchAllRepos() {
    return fetch('https://api.github.com/users/' + username + '/repos?per_page=' + reposPerPage + '&type=public')
      .then(function(response) {
        if (!response.ok) throw new Error('GitHub API error');
        return response.json();
      });
  }
  
  // Format date
  function formatDate(dateStr) {
    var date = new Date(dateStr);
    return date.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }
  
  // Tag emoji map
  var tagEmojis = {
    'stata-packages': '📊',
    'poverty': '💰',
    'inequality': '⚖️',
    'education': '📚',
    'data-tools': '🔧',
    'decomposition': '🧮',
    'small-area': '🗺️',
    'visualization': '📈',
    'econometrics': '📉',
    'world-bank': '🌍',
    'research': '🔬',
    'utilities': '⚙️',
    'forked': '🔀'
  };
  
  // Create repo card HTML
  function createRepoCard(repo) {
    var language = repo.language || 'Unknown';
    var languageSlug = language.toLowerCase().replace(/[^a-z0-9]/g, '-');
    var stars = repo.stargazers_count || 0;
    var forks = repo.forks_count || 0;
    var description = repo.description || 'No description available.';
    var tags = getRepoTags(repo.name);
    var featured = isFeatured(repo.name);
    var hidden = isHidden(repo.name);
    
    var cardClass = 'jp-card';
    if (featured) cardClass += ' featured-repo';
    
    var html = '<article class="' + cardClass + '" ';
    html += 'data-language="' + languageSlug + '" ';
    html += 'data-stars="' + stars + '" ';
    html += 'data-updated="' + repo.updated_at + '" ';
    html += 'data-created="' + repo.created_at + '" ';
    html += 'data-name="' + repo.name.toLowerCase() + '" ';
    html += 'data-tags="' + tags.join(',') + '" ';
    html += 'data-fork="' + (repo.fork ? 'true' : 'false') + '" ';
    html += 'data-hidden="' + (hidden ? 'true' : 'false') + '" ';
    html += 'data-featured="' + (featured ? 'true' : 'false') + '">';
    
    html += '<div class="jp-card__content">';
    html += '<h4 class="jp-card__title">';
    html += '<a href="' + repo.html_url + '" target="_blank" rel="noopener">';
    html += '<i class="fab fa-github"></i> ' + repo.name;
    html += '</a>';
    if (featured) {
      html += '<span class="featured-badge">⭐ Featured</span>';
    }
    if (repo.fork) {
      html += '<span class="jp-pill" style="font-size: 0.7em; margin-left: 0.5em;">Fork</span>';
    }
    html += '</h4>';
    
    html += '<div class="jp-card__meta">';
    html += '<span class="jp-card__date">Updated: ' + formatDate(repo.updated_at) + '</span>';
    if (language !== 'Unknown') {
      html += '<span class="jp-pill">' + language + '</span>';
    }
    html += '</div>';
    
    html += '<p class="jp-card__description">' + description + '</p>';
    
    html += '<div class="jp-card__tags">';
    html += '<span class="jp-tag"><i class="fa fa-star"></i> ' + stars + '</span>';
    html += '<span class="jp-tag"><i class="fa fa-code-branch"></i> ' + forks + '</span>';
    if (repo.license) {
      html += '<span class="jp-tag"><i class="fa fa-balance-scale"></i> ' + repo.license.spdx_id + '</span>';
    }
    
    // Display topic tags
    for (var i = 0; i < tags.length && i < 3; i++) {
      var tag = tags[i];
      var emoji = tagEmojis[tag] || '';
      html += '<span class="jp-tag topic-tag">' + emoji + ' ' + tag.replace(/-/g, ' ') + '</span>';
    }
    
    html += '</div>';
    
    html += '<div class="jp-card__actions">';
    html += '<a href="' + repo.html_url + '" class="jp-readmore" target="_blank" rel="noopener">View Repository →</a>';
    html += '</div>';
    html += '</div>';
    html += '</article>';
    return html;
  }
  
  // Render repos
  function renderRepos(repos) {
    var container = document.getElementById('repos-list');
    var html = '';
    for (var i = 0; i < repos.length; i++) {
      html += createRepoCard(repos[i]);
    }
    container.innerHTML = html;
    applyFilters(); // Apply initial filters
  }
  
  // Update stats
  function updateStats(repos) {
    var totalStars = 0;
    var totalForks = 0;
    var langCount = {};
    
    for (var i = 0; i < repos.length; i++) {
      var r = repos[i];
      totalStars += r.stargazers_count || 0;
      totalForks += r.forks_count || 0;
      if (r.language) {
        langCount[r.language] = (langCount[r.language] || 0) + 1;
      }
    }
    
    // Find top language
    var topLang = null;
    var topCount = 0;
    for (var lang in langCount) {
      if (langCount[lang] > topCount) {
        topCount = langCount[lang];
        topLang = lang;
      }
    }
    
    document.getElementById('repo-count').textContent = repos.length;
    document.getElementById('total-stars').textContent = totalStars;
    document.getElementById('total-forks').textContent = totalForks;
    document.getElementById('top-language').textContent = topLang || '—';
  }
  
  // Create language filter buttons
  function createLanguageFilters(repos) {
    var langCount = {};
    for (var i = 0; i < repos.length; i++) {
      var lang = repos[i].language || 'Unknown';
      langCount[lang] = (langCount[lang] || 0) + 1;
    }
    
    // Sort languages by count
    var langs = [];
    for (var lang in langCount) {
      langs.push([lang, langCount[lang]]);
    }
    langs.sort(function(a, b) { return b[1] - a[1]; });
    langs = langs.slice(0, 6); // Top 6
    
    var filterContainer = document.getElementById('language-filters');
    for (var i = 0; i < langs.length; i++) {
      var lang = langs[i][0];
      var count = langs[i][1];
      var btn = document.createElement('button');
      btn.className = 'tag-filter lang-btn';
      btn.setAttribute('data-filter', lang.toLowerCase().replace(/[^a-z0-9]/g, '-'));
      btn.textContent = lang + ' (' + count + ')';
      filterContainer.appendChild(btn);
    }
  }
  
  // Current filter state
  var currentTopicFilter = 'all';
  var currentLangFilter = 'all';
  
  // Update the visible count in the All button
  function updateAllCount(count) {
    var allCountEl = document.getElementById('all-count');
    if (allCountEl) {
      allCountEl.textContent = count;
    }
  }
  
  // Apply all filters
  function applyFilters() {
    var hideForks = document.getElementById('hide-forks').checked;
    var hideHidden = document.getElementById('hide-hidden').checked;
    var cards = document.querySelectorAll('.jp-card');
    var visibleCount = 0;
    
    for (var i = 0; i < cards.length; i++) {
      var card = cards[i];
      var cardLang = card.getAttribute('data-language');
      var cardTags = card.getAttribute('data-tags').split(',');
      var isFork = card.getAttribute('data-fork') === 'true';
      var isHiddenRepo = card.getAttribute('data-hidden') === 'true';
      
      var show = true;
      
      // Check topic filter
      if (currentTopicFilter !== 'all' && cardTags.indexOf(currentTopicFilter) === -1) {
        show = false;
      }
      
      // Check language filter
      if (currentLangFilter !== 'all' && cardLang !== currentLangFilter) {
        show = false;
      }
      
      // Check hide forks
      if (hideForks && isFork) {
        show = false;
      }
      
      // Check hide hidden
      if (hideHidden && isHiddenRepo) {
        show = false;
      }
      
      card.style.display = show ? '' : 'none';
      if (show) visibleCount++;
    }
    
    // Update the count in the All button
    updateAllCount(visibleCount);
  }
  
  // Setup filter handlers
  function setupFilters() {
    // Topic filter buttons
    var topicBtns = document.querySelectorAll('.topic-btn');
    for (var i = 0; i < topicBtns.length; i++) {
      topicBtns[i].addEventListener('click', function() {
        currentTopicFilter = this.getAttribute('data-filter');
        var allTopicBtns = document.querySelectorAll('.topic-btn');
        for (var j = 0; j < allTopicBtns.length; j++) {
          allTopicBtns[j].classList.remove('active');
        }
        this.classList.add('active');
        applyFilters();
      });
    }
    
    // Language filter buttons
    var langBtns = document.querySelectorAll('.lang-btn');
    for (var i = 0; i < langBtns.length; i++) {
      langBtns[i].addEventListener('click', function() {
        currentLangFilter = this.getAttribute('data-filter');
        var allLangBtns = document.querySelectorAll('.lang-btn');
        for (var j = 0; j < allLangBtns.length; j++) {
          allLangBtns[j].classList.remove('active');
        }
        this.classList.add('active');
        applyFilters();
      });
    }
    
    // Checkbox handlers
    document.getElementById('hide-forks').addEventListener('change', applyFilters);
    document.getElementById('hide-hidden').addEventListener('change', applyFilters);
  }
  
  // Sort functionality
  function setupSorting() {
    var sortSelect = document.getElementById('sort-select');
    sortSelect.addEventListener('change', function() {
      var sortBy = this.value;
      var container = document.getElementById('repos-list');
      var cards = Array.prototype.slice.call(document.querySelectorAll('.jp-card'));
      
      cards.sort(function(a, b) {
        switch(sortBy) {
          case 'featured':
            var aFeat = a.getAttribute('data-featured') === 'true' ? 1 : 0;
            var bFeat = b.getAttribute('data-featured') === 'true' ? 1 : 0;
            if (bFeat !== aFeat) return bFeat - aFeat;
            return parseInt(b.getAttribute('data-stars')) - parseInt(a.getAttribute('data-stars'));
          case 'stars':
            return parseInt(b.getAttribute('data-stars')) - parseInt(a.getAttribute('data-stars'));
          case 'name':
            return a.getAttribute('data-name').localeCompare(b.getAttribute('data-name'));
          case 'created':
            return new Date(b.getAttribute('data-created')) - new Date(a.getAttribute('data-created'));
          case 'updated':
          default:
            return new Date(b.getAttribute('data-updated')) - new Date(a.getAttribute('data-updated'));
        }
      });
      
      for (var i = 0; i < cards.length; i++) {
        container.appendChild(cards[i]);
      }
    });
  }
  
  // Main execution
  fetchAllRepos()
    .then(function(repos) {
      // Sort by featured + stars by default
      repos.sort(function(a, b) {
        var aFeat = isFeatured(a.name) ? 1 : 0;
        var bFeat = isFeatured(b.name) ? 1 : 0;
        if (bFeat !== aFeat) return bFeat - aFeat;
        return (b.stargazers_count || 0) - (a.stargazers_count || 0);
      });
      
      updateStats(repos);
      createLanguageFilters(repos);
      renderRepos(repos);
      setupFilters();
      setupSorting();
      
      document.getElementById('repos-loading').style.display = 'none';
      document.getElementById('repos-list').style.display = '';
    })
    .catch(function(error) {
      console.error('Error fetching repos:', error);
      document.getElementById('repos-loading').style.display = 'none';
      document.getElementById('repos-error').style.display = '';
    });
});
