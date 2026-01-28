# Ruby 3.3+ required (github-pages / ffi). Use rbenv: rbenv install 3.3.10 && rbenv local 3.3.10
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "webrick"  # required for Jekyll serve on Ruby 3+
gem "faraday-retry"  # Faraday v2.0+ retry behavior (used by github-metadata etc.)

gem "tzinfo-data"
gem "wdm", "~> 0.1.0" if Gem.win_platform?

# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-paginate"
  gem "jekyll-sitemap"
  gem "jekyll-gist"
  gem "jekyll-feed"
  gem "jemoji"
  gem "jekyll-include-cache"
  gem "jekyll-algolia"
end
