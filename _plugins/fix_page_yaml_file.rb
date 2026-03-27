# Workaround for Jekyll 4.x + forwardable 1.4.0 incompatibility
# Jekyll::Excerpt delegates yaml_file? to the document, but Jekyll::Page
# doesn't define this method (only Document does). forwardable 1.4.0
# raises NoMethodError when the delegated method doesn't exist.
# See: https://github.com/jekyll/jekyll/issues/9553
module Jekyll
  class Page
    def yaml_file?
      %w(.yml .yaml).include?(extname)
    end
  end
end
