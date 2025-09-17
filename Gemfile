source "https://rubygems.org"source "https://rubygem# Group for Jekyll plugins

# Specifies the RubyGems repository to fetch all required gems for your project.group :jekyll_plugins do

  gem "jekyll-feed"         # Generates RSS/Atom feeds for your site's posts.

# Jekyll is the static site generator for GitHub Pages.  gem "jekyll-sitemap"      # Automatically creates a sitemap for your site.

# The "3.10.0" ensures you're using the latest GitHub Pages supported Jekyll version.  gem "jekyll-scholar"      # Adds academic references and citations to your site.

gem "jekyll", "3.10.0"  gem "jekyll-include-cache" # Required for Minimal Mistakes theme performance

  gem "jekyll-remote-theme" # Required for remote theme functionality

# Includes GitHub Pages-specific plugins and configurations.  gem "tzinfo"              # Required for proper timezone handling.

# This locks the `github-pages` gem to version 232.  gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby] 

gem "github-pages", "~> 232", group: :jekyll_plugins  # Timezone data for Windows and JRuby platforms.

  

# Liquid is a templating language used by Jekyll.  #gem "hawkins"             # A plugin to perform code analysis for Jekyll sites.

# Lock the version to 4.0.4 for compatibility with Jekyll 3.10.endpecifies the RubyGems repository to fetch all required gems for your project.

gem "liquid", "4.0.4"

# Jekyll is the static site generator for GitHub Pages.

# Nokogiri is used for parsing HTML and XML in Jekyll.# The "3.10.0" ensures you're using the latest GitHub Pages supported Jekyll version.

# We lock it below version 1.13.6 for compatibility with older Ruby versions like 2.7.gem "jekyll", "3.10.0"

gem "nokogiri"

# Includes GitHub Pages-specific plugins and configurations.

# Use the pure Ruby version of EventMachine, forcing it not to use the x64-mingw32 version# This locks the `github-pages` gem to version 232.

gem 'eventmachine', '1.2.7', platforms: [:ruby, :mswin, :x64_mingw]gem "github-pages", "~> 232", group: :jekyll_plugins

gem 'webrick'

# Liquid is a templating language used by Jekyll.

# Group for Jekyll plugins# Lock the version to 4.0.4 for compatibility with Jekyll 3.10.

group :jekyll_plugins dogem "liquid", "4.0.4"

  gem "jekyll-feed"         # Generates RSS/Atom feeds for your site's posts.

  gem "jekyll-sitemap"      # Automatically creates a sitemap for your site.# Nokogiri is used for parsing HTML and XML in Jekyll.

  gem "jekyll-scholar"      # Adds academic references and citations to your site.# We lock it below version 1.13.6 for compatibility with older Ruby versions like 2.7.

  gem "jekyll-include-cache" # Required for Minimal Mistakes theme performancegem "nokogiri"

  gem "jekyll-remote-theme" # Required for remote theme functionality

  gem "tzinfo"              # Required for proper timezone handling.# Use the pure Ruby version of EventMachine, forcing it not to use the x64-mingw32 version

  gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby] gem 'eventmachine', '1.2.7', platforms: [:ruby, :mswin, :x64_mingw]

  # Timezone data for Windows and JRuby platforms.gem 'webrick'

  

  #gem "hawkins"             # A plugin to perform code analysis for Jekyll sites.# Group for Jekyll plugins

endgroup :jekyll_plugins do

  gem "jekyll-feed"         # Generates RSS/Atom feeds for your site’s posts.

# Windows-specific gem  gem "jekyll-sitemap"      # Automatically creates a sitemap for your site.

gem "wdm", "~> 0.1.0" if Gem.win_platform?   gem "jekyll-scholar"      # Adds academic references and citations to your site.

# This gem improves live-reloading on Windows while serving the site.  gem "tzinfo"              # Required for proper timezone handling.
  gem "tzinfo-data", platforms: [:mingw, :mswin, :x64_mingw, :jruby] 
  # Timezone data for Windows and JRuby platforms.
  
  #gem "hawkins"             # A plugin to perform code analysis for Jekyll sites.
end

# Windows-specific gem
gem "wdm", "~> 0.1.0" if Gem.win_platform? 
# This gem improves live-reloading on Windows while serving the site.
