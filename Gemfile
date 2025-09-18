source "https://rubygems.org"

# GitHub Pages compatible Gemfile
# Uses github-pages gem but with explicit plugin specifications for clarity

gem "github-pages", "~> 232", group: :jekyll_plugins

# Explicitly specify supported plugins for documentation
# These are included by github-pages gem but listed for clarity
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap" 
  gem "jekyll-include-cache"
  gem "jekyll-remote-theme"
  gem "jekyll-seo-tag"
end

# Windows and Ruby compatibility
gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby]
gem "wdm", "~> 0.1.0" if Gem.win_platform?

