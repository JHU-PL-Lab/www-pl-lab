task :test do
  require "html/proofer"

  sh "bundle exec jekyll build"
  HTML::Proofer.new(
    "./_site",
    href_ignore: [
      "#",
    ]
  ).run
end
