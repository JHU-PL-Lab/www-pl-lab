# This task is meant to be run in the Docker container that run Jekyll.
task :test do
  require "html/proofer"

  sh "bundle exec jekyll build"
  HTML::Proofer.new(
    "./_site",
    href_ignore: [
#      "#",
    ]
  ).run
end

# This task is meant to be run in the developer's machine, because it needs to
# be able to push to the repository -- i.e. it needs the SSH keys available.
task :deploy do

  SOURCE_BRANCH = "source"
  TARGET_BRANCH = "master"
  GENERATED_WEBSITE_PATH = "_site"
  REMOTE_URL = "git@pl.cs.jhu.edu:www-pl-lab"

  ##############################################################################

  puts "Checking that Vagrant is installed..."

  unless system "vagrant --version > /dev/null 2>&1"
    abort <<-ERROR
Deployment failed! You need to install Vagrant in order to build and deploy the
website.

Refer to `README.md' for more information.
ERROR
  end

  ##############################################################################

  puts "Checking that Vagrant Virtual Machine is running..."

  until `vagrant status 2>&1` =~ /default\s+running/

    print "Vagrant Virtual Machine is not running. Would you like to start it? (Y/n): "
    answer = STDIN.gets.strip.downcase

    if answer == "n"
      abort "Deployment failed! Can't proceed deployment without running Vagrant Virtual Machine."
    else
      system "vagrant up > /dev/null 2>&1"
    end
  end

  ##############################################################################

  puts "Checking if Git index (staging area) is clean..."

  # This is required so we can later switch branches.

  unless `git status --porcelain`.empty?
    abort "Deployment failed! The Git index (staging area) is dirty. Please, commit the changes and try again."
  end

  ##############################################################################

  puts "Checking that the `#{SOURCE_BRANCH}' branch is checkout out..."

  # This is required because the `SOURCE_BRANCH' branch is the only allowed to be deployed.

  until `git branch` =~ /\* #{SOURCE_BRANCH}/
    print "The `#{SOURCE_BRANCH}' branch isn't checkout out, would you like to switch to it? (Y/n): "
    answer = STDIN.gets.strip.downcase

    if answer == "n"
      abort "Deployment failed! Can't deploy any other branch besides `#{SOURCE_BRANCH}'."
    else
      system "git checkout '#{SOURCE_BRANCH}' > /dev/null 2>&1"
    end
  end

  ##############################################################################

  puts "Checking access to deployment remote `#{REMOTE_URL}'..."

  unless system "git ls-remote '#{REMOTE_URL}' > /dev/null 2>&1"
    abort "Deployment failed! Can't access deployment remote `#{REMOTE_URL}'."
  end

  ##############################################################################

  puts "Checking that branches `#{SOURCE_BRANCH}' and `#{TARGET_BRANCH}' are up-to-date..."

  [SOURCE_BRANCH, TARGET_BRANCH].each do |branch|
    local_sha1 = `git rev-parse #{branch} 2>&1`.strip
    remote_sha1 = `git ls-remote -q '#{REMOTE_URL}' '#{branch}' 2>&1`.strip.split(/\s+/).first

    unless local_sha1 == remote_sha1
      abort <<-ERROR
Deployment failed! Branch `#{branch}' isn't up-to-date. Please Git pull
and try again.

We can't automate this step, because it may lead to conflicts which you'd need
to resolve by hand.
ERROR
    end
  end

  ##############################################################################

  puts "Checking that the tests are passing..."

  unless (test_results = `rm -rf '#{GENERATED_WEBSITE_PATH}' && vagrant exec docker-compose run --rm jekyll rake test 2>&1`) =~ /HTML-Proofer finished successfully./
    abort "Deployment failed! There are failing tests:\n\n#{test_results}"
  end

  ##############################################################################

  abort "This is not fully implemented yet."
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
