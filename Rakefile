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

  puts "Checking that the `source' branch is checkout out..."

  # This is required because the `source' branch is the only allowed to be deployed.

  until `git branch` =~ /\* source/
    print "The `source' branch isn't checkout out, would you like to switch to it? (Y/n): "
    answer = STDIN.gets.strip.downcase

    if answer == "n"
      abort "Deployment failed! Can't deploy any other branch besides `source'."
    else
      system "git checkout source > /dev/null 2>&1"
    end
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
