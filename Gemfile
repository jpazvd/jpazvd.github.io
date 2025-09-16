source "https://rubygems.org"
# Specifies the RubyGems repository to fetch all required gems for your project.

# Jekyll is the static site generator for GitHub Pages.
# The "3.10.0" ensures you're using the latest GitHub Pages supported Jekyll version.
gem "jekyll", "3.10.0"

# Includes GitHub Pages-specific plugins and configurations.
# This locks the `github-pages` gem to version 232.
gem "github-pages", "~> 232", group: :jekyll_plugins

# Liquid is a templating language used by Jekyll.
# Lock the version to 4.0.4 for compatibility with Jekyll 3.10.
gem "liquid", "4.0.4"

# Nokogiri is used for parsing HTML and XML in Jekyll.
# We lock it below version 1.13.6 for compatibility with older Ruby versions like 2.7.
gem "nokogiri"

# Use the pure Ruby version of EventMachine, forcing it not to use the x64-mingw32 version
gem 'eventmachine', '1.2.7', platforms: [:ruby, :mswin, :x64_mingw]
gem 'webrick'

# Group for Jekyll plugins
group :jekyll_plugins do
  gem "jekyll-feed"         # Generates RSS/Atom feeds for your site’s posts.
  gem "jekyll-sitemap"      # Automatically creates a sitemap for your site.
  gem "jekyll-scholar"      # Adds academic references and citations to your site.
  gem "tzinfo"              # Required for proper timezone handling.
  gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby] 
  # Timezone data for Windows and JRuby platforms.
  
  #gem "hawkins"             # A plugin to perform code analysis for Jekyll sites.
end

# Windows-specific gem
gem "wdm", "~> 0.1.0" if Gem.win_platform? 
# This gem improves live-reloading on Windows while serving the site.
