# This task is meant to be run in the Docker container that run Jekyll.
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

# This task is meant to be run in the developer's machine, because it needs to
# be able to push to the repository -- i.e. it needs the SSH keys available.
task :deploy do
  fail "This is not fully implemented yet."
  temp_path = "/tmp/website-#{ rand(100000) }"
  generated_site_path = "_site"

  rm_rf generated_site_path
  sh "vagrant exec docker-compose --rm run jekyll build"
  mv generated_site_path, temp_path
  sh "git checkout master"
  sh "git pull origin master"
  rm_rf "./*"
  mv "#{ temp_path }/*", "."
  sh "git add -A"
  sh "git commit -m 'Automatic website update on #{Time.now}'"
  sh "git push origin master"
  sh "git checkout source"
  sh "curl http://pl.cs.jhu.edu/update.py"

  puts "Website updated. Go to http://pl.cs.jhu.edu/"
end
