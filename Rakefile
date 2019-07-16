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
# be able to push to the repository -- i.e. it needs the SSH keys available. If
# you make changes here, remember to replicate them on the `deploy:no_vagrant` task.
task :deploy do

  require 'securerandom'

  ##############################################################################

  SOURCE_BRANCH = "source"
  TARGET_BRANCH = "master"
  GENERATED_WEBSITE_PATH = "_site"
  TEMPORARY_PATH = "/tmp/www-pl-lab-" + SecureRandom.hex
  REMOTE_URL = "git@pl.cs.jhu.edu:www-pl-lab"
  UPDATE_URL = "http://pl.cs.jhu.edu/update.py"
  FINAL_URL = "http://pl.cs.jhu.edu/"

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

  started_vagrant = false

  until `vagrant status 2>&1` =~ /default\s+running/

    print "Vagrant Virtual Machine is not running. Would you like to start it? (Y/n): "
    answer = STDIN.gets.strip.downcase

    if answer == "n"
      abort "Deployment failed! Can't proceed deployment without running Vagrant Virtual Machine."
    else
      started_vagrant = true
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

    puts "Checking that branch `#{branch}' is up-to-date..."

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

  puts "Building website..."

  system "rm -rf '#{GENERATED_WEBSITE_PATH}' && vagrant exec docker-compose run --rm jekyll jekyll build > /dev/null 2>&1"

  ##############################################################################

  puts "Adding auxiliary files..."

  [
    [
      ".htaccess", <<-'FILE'
Options +ExecCGI
Options -Indexes

# Protect configuration file from prying eyes.
<Files "update-page.conf.json">
    Order allow,deny
    Deny from all
</Files>

<Files "DONT-EDIT-THESE-FILES">
    Order allow,deny
    Deny from all
</Files>
FILE
    ],
    [
      "DONT-EDIT-THESE-FILES", <<-FILE
DON'T EDIT THESE FILES
======================

They were automatically generated from the `#{SOURCE_BRANCH}` branch, using Jekyll. Check
the `#{SOURCE_BRANCH}` branch out and read the `README.md` for more information.

Built at: #{Time.now}
FILE
    ],
    [
      "update-page.conf.json", <<-'FILE'
{
    "webRoot": "/var/www/pl.cs.jhu.edu/",
    "repositories":
        {
            "oose-group1": {
                "path": "/oose/group/1",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-1/webpage.git"
            },
            "oose-group2": {
                "path": "/oose/group/2",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-2/webpage.git"
            },
            "oose-group3": {
                "path": "/oose/group/3",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-3/webpage.git"
            },
            "oose-group4": {
                "path": "/oose/group/4",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-4/webpage.git"
            },
            "oose-group5": {
                "path": "/oose/group/5",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-5/webpage.git"
            },
            "oose-group6": {
                "path": "/oose/group/6",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-6/webpage.git"
            },
            "oose-group7": {
                "path": "/oose/group/7",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-7/webpage.git"
            },
            "oose-group8": {
                "path": "/oose/group/8",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-8/webpage.git"
            },
            "oose-group9": {
                "path": "/oose/group/9",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-9/webpage.git"
            },
            "oose-group10": {
                "path": "/oose/group/10",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-10/webpage.git"
            },
            "oose-group11": {
                "path": "/oose/group/11",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-11/webpage.git"
            },
            "oose-group12": {
                "path": "/oose/group/12",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-12/webpage.git"
            },
            "oose-group13": {
                "path": "/oose/group/13",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-13/webpage.git"
            },
            "oose-group14": {
                "path": "/oose/group/14",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-14/webpage.git"
            },
            "oose-group15": {
                "path": "/oose/group/15",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-15/webpage.git"
            },
            "oose-group16": {
                "path": "/oose/group/16",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-16/webpage.git"
            },
            "oose-group17": {
                "path": "/oose/group/17",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-17/webpage.git"
            },
            "oose-group18": {
                "path": "/oose/group/18",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-18/webpage.git"
            },
            "oose-group19": {
                "path": "/oose/group/19",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-19/webpage.git"
            },
            "oose-group20": {
                "path": "/oose/group/20",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-20/webpage.git"
            },
            "oose-group21": {
                "path": "/oose/group/21",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-21/webpage.git"
            },
            "oose-group22": {
                "path": "/oose/group/22",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-22/webpage.git"
            },
            "oose-group23": {
                "path": "/oose/group/23",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-23/webpage.git"
            },
            "oose-group24": {
                "path": "/oose/group/24",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-24/webpage.git"
            },
            "oose-group25": {
                "path": "/oose/group/25",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-25/webpage.git"
            }
        }
}
FILE
    ],
    [
      "update-page.py", <<-'FILE'
#!/usr/bin/python

import cgi
import cgitb #; cgitb.enable() # Optional; for debugging only
import json
import os
import subprocess
import sys

CONFIG_FILE_LOCATION="./update-page.conf.json"

def stdHeaders(code):
    sys.stdout.write('Content-Type: text/plain\n')
    sys.stdout.write('Status: '+str(code)+'\n')
    sys.stdout.write('\n')

def fail(msg, code=400):
    stdHeaders(code)
    sys.stdout.write(msg)
    sys.stdout.flush()
    sys.exit(0)

def getOrFail(d,k,msg,code=500):
    v = d.get(k)
    if v is None: fail(msg, code)
    return v

def runSubProc(cmdline, cwd):
    proc = subprocess.Popen(cmdline, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                close_fds=True, cwd=cwd)
    (out,_) = proc.communicate()
    ret = proc.wait()
    return (ret,out)

# Determine which repository to update
arguments = cgi.FieldStorage()
if 'name' not in arguments:
    fail('"name" parameter not specified')
name = arguments.getfirst('name')

# Read config file for repo information
try:
    f = open(CONFIG_FILE_LOCATION)
    config = json.load(f)
    f.close()
except:
    e = sys.exc_info()
    fail("Could not read config file: " + str(e), 500)

web_root_path = getOrFail(config, "webRoot",
                            "Malformed config file: no webRoot.")
repos = getOrFail(config, 'repositories',
                    "Malformed config file: no repositories.")
repo = getOrFail(repos, name, "Unknown repository: " + str(name), 400)
repo_path = web_root_path + "/" + \
                getOrFail(repo, "path",
                            "Malformed config file: no path for " + str(name))
repo_url = getOrFail(repo, "url",
                        "Malformed config file: no URL for " + str(name))

# Now perform the actual update.
if os.path.exists(repo_path):
    # Then the repository already exists.  Update it.
    (ec,out) = runSubProc(["git","pull"],cwd=repo_path)
else:
    # The repository does not yet exist.  Create the directory and clone it.
    os.makedirs(repo_path)
    (ec,out) = runSubProc(["git","clone",repo_url,"."],cwd=repo_path)
# Based on the error code we get, determine if this was a success or not.
status = 200 if ec == 0 else 500
stdHeaders(status)
# Either way, dump the subprocess output to the caller.
sys.stdout.write(out)
sys.stdout.write('\n\n*** End of output\n')
FILE
    ],
    [
      "update.py", <<-'FILE'
#!/usr/bin/python

import subprocess
import sys

sys.stdout.write('Content-Type: text/plain\n\n')
sys.stdout.flush()
subprocess.call(["git","pull"])
FILE
    ],
  ].each do |(name, contents)|
    path = File.join GENERATED_WEBSITE_PATH, name

    puts "Adding `#{path}'..."

    File.write path, contents

    if path =~ /\.py\z/
      puts "Making `#{path}' executable..."

      system "chmod a+x '#{path}' > /dev/null 2>&1"
    end
  end

  ##############################################################################

  puts "Moving the generated website from `#{GENERATED_WEBSITE_PATH}' to a temporary directory in `#{TEMPORARY_PATH}'..."

  system "mv '#{GENERATED_WEBSITE_PATH}' '#{TEMPORARY_PATH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Checking the branch `#{TARGET_BRANCH}' out..."

  system "git checkout '#{TARGET_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Deleting the contents from previous deployments..."

  previous_deployments_files = Dir["*"] + Dir[".*"] - [".", "..", ".vagrant", ".git"]

  system "rm -rf #{previous_deployments_files.map { |x| "'#{x}'" }.join(" ")} > /dev/null 2>&1"

  ##############################################################################

  puts "Copying the contents of the temporary directory `#{TEMPORARY_PATH}' back in..."

  system "rsync -av '#{TEMPORARY_PATH}'/ ./ > /dev/null 2>&1"

  ##############################################################################

  puts "Committing..."

  system "git add -A && git commit -m 'Automatic update of website' > /dev/null 2>&1"

  ##############################################################################

  puts "Pushing changes to `#{REMOTE_URL}'..."

  system "git push '#{REMOTE_URL}' '#{TARGET_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Calling `#{UPDATE_URL}' to update..."

  system "curl '#{UPDATE_URL}' > /dev/null 2>&1"

  ##############################################################################

  puts "Checking the branch `#{SOURCE_BRANCH}' out..."

  system "git checkout '#{SOURCE_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  if started_vagrant
    print "Would like to turn the Vagrant Virtual Machine back off? (Y/n): "
    answer = STDIN.gets.strip.downcase

    if answer == "y"
      until `vagrant status 2>&1` !~ /default\s+running/
        puts "Stopping Vagrant Virtual Machine..."

        system "vagrant suspend > /dev/null 2>&1"
      end
    end
  end

  ##############################################################################

  puts <<-SUCCESS
Deployment succeeded!

Go to `#{FINAL_URL}' to see the results.
SUCCESS

end

# This task is meant to be run in the developer's machine, because it needs to
# be able to push to the repository -- i.e. it needs the SSH keys available. If
# you make changes here, remember to replicate them on the `deploy` task.
namespace :deploy do
  task :no_vagrant do

  require 'securerandom'

  ##############################################################################

  SOURCE_BRANCH = "source"
  TARGET_BRANCH = "master"
  GENERATED_WEBSITE_PATH = "_site"
  TEMPORARY_PATH = "/tmp/www-pl-lab-" + SecureRandom.hex
  REMOTE_URL = "git@pl.cs.jhu.edu:www-pl-lab"
  UPDATE_URL = "http://pl.cs.jhu.edu/update.py"
  FINAL_URL = "http://pl.cs.jhu.edu/"

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

    puts "Checking that branch `#{branch}' is up-to-date..."

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

  puts "Building website..."

  system "rm -rf '#{GENERATED_WEBSITE_PATH}' && docker-compose run --rm jekyll jekyll build > /dev/null 2>&1 && su - root -c 'chown --recursive shiwei:shiwei ~shiwei/www-pl-lab/_site/ && rm -rf ~shiwei/www-pl-lab/.sass-cache/'"

  ##############################################################################

  puts "Adding auxiliary files..."

  [
    [
      ".htaccess", <<-'FILE'
Options +ExecCGI
Options -Indexes

# Protect configuration file from prying eyes.
<Files "update-page.conf.json">
    Order allow,deny
    Deny from all
</Files>

<Files "DONT-EDIT-THESE-FILES">
    Order allow,deny
    Deny from all
</Files>
FILE
    ],
    [
      "DONT-EDIT-THESE-FILES", <<-FILE
DON'T EDIT THESE FILES
======================

They were automatically generated from the `#{SOURCE_BRANCH}` branch, using Jekyll. Check
the `#{SOURCE_BRANCH}` branch out and read the `README.md` for more information.

Built at: #{Time.now}
FILE
    ],
    [
      "update-page.conf.json", <<-'FILE'
{
    "webRoot": "/var/www/pl.cs.jhu.edu/",
    "repositories":
        {
            "oose-group1": {
                "path": "/oose/group/1",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-1/webpage.git"
            },
            "oose-group2": {
                "path": "/oose/group/2",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-2/webpage.git"
            },
            "oose-group3": {
                "path": "/oose/group/3",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-3/webpage.git"
            },
            "oose-group4": {
                "path": "/oose/group/4",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-4/webpage.git"
            },
            "oose-group5": {
                "path": "/oose/group/5",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-5/webpage.git"
            },
            "oose-group6": {
                "path": "/oose/group/6",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-6/webpage.git"
            },
            "oose-group7": {
                "path": "/oose/group/7",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-7/webpage.git"
            },
            "oose-group8": {
                "path": "/oose/group/8",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-8/webpage.git"
            },
            "oose-group9": {
                "path": "/oose/group/9",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-9/webpage.git"
            },
            "oose-group10": {
                "path": "/oose/group/10",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-10/webpage.git"
            },
            "oose-group11": {
                "path": "/oose/group/11",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-11/webpage.git"
            },
            "oose-group12": {
                "path": "/oose/group/12",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-12/webpage.git"
            },
            "oose-group13": {
                "path": "/oose/group/13",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-13/webpage.git"
            },
            "oose-group14": {
                "path": "/oose/group/14",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-14/webpage.git"
            },
            "oose-group15": {
                "path": "/oose/group/15",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-15/webpage.git"
            },
            "oose-group16": {
                "path": "/oose/group/16",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-16/webpage.git"
            },
            "oose-group17": {
                "path": "/oose/group/17",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-17/webpage.git"
            },
            "oose-group18": {
                "path": "/oose/group/18",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-18/webpage.git"
            },
            "oose-group19": {
                "path": "/oose/group/19",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-19/webpage.git"
            },
            "oose-group20": {
                "path": "/oose/group/20",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-20/webpage.git"
            },
            "oose-group21": {
                "path": "/oose/group/21",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-21/webpage.git"
            },
            "oose-group22": {
                "path": "/oose/group/22",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-22/webpage.git"
            },
            "oose-group23": {
                "path": "/oose/group/23",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-23/webpage.git"
            },
            "oose-group24": {
                "path": "/oose/group/24",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-24/webpage.git"
            },
            "oose-group25": {
                "path": "/oose/group/25",
                "url": "git.gitlab-oose.pl.cs.jhu.edu:oose-14-group-25/webpage.git"
            }
        }
}
FILE
    ],
    [
      "update-page.py", <<-'FILE'
#!/usr/bin/python

import cgi
import cgitb #; cgitb.enable() # Optional; for debugging only
import json
import os
import subprocess
import sys

CONFIG_FILE_LOCATION="./update-page.conf.json"

def stdHeaders(code):
    sys.stdout.write('Content-Type: text/plain\n')
    sys.stdout.write('Status: '+str(code)+'\n')
    sys.stdout.write('\n')

def fail(msg, code=400):
    stdHeaders(code)
    sys.stdout.write(msg)
    sys.stdout.flush()
    sys.exit(0)

def getOrFail(d,k,msg,code=500):
    v = d.get(k)
    if v is None: fail(msg, code)
    return v

def runSubProc(cmdline, cwd):
    proc = subprocess.Popen(cmdline, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                close_fds=True, cwd=cwd)
    (out,_) = proc.communicate()
    ret = proc.wait()
    return (ret,out)

# Determine which repository to update
arguments = cgi.FieldStorage()
if 'name' not in arguments:
    fail('"name" parameter not specified')
name = arguments.getfirst('name')

# Read config file for repo information
try:
    f = open(CONFIG_FILE_LOCATION)
    config = json.load(f)
    f.close()
except:
    e = sys.exc_info()
    fail("Could not read config file: " + str(e), 500)

web_root_path = getOrFail(config, "webRoot",
                            "Malformed config file: no webRoot.")
repos = getOrFail(config, 'repositories',
                    "Malformed config file: no repositories.")
repo = getOrFail(repos, name, "Unknown repository: " + str(name), 400)
repo_path = web_root_path + "/" + \
                getOrFail(repo, "path",
                            "Malformed config file: no path for " + str(name))
repo_url = getOrFail(repo, "url",
                        "Malformed config file: no URL for " + str(name))

# Now perform the actual update.
if os.path.exists(repo_path):
    # Then the repository already exists.  Update it.
    (ec,out) = runSubProc(["git","pull"],cwd=repo_path)
else:
    # The repository does not yet exist.  Create the directory and clone it.
    os.makedirs(repo_path)
    (ec,out) = runSubProc(["git","clone",repo_url,"."],cwd=repo_path)
# Based on the error code we get, determine if this was a success or not.
status = 200 if ec == 0 else 500
stdHeaders(status)
# Either way, dump the subprocess output to the caller.
sys.stdout.write(out)
sys.stdout.write('\n\n*** End of output\n')
FILE
    ],
    [
      "update.py", <<-'FILE'
#!/usr/bin/python

import subprocess
import sys

sys.stdout.write('Content-Type: text/plain\n\n')
sys.stdout.flush()
subprocess.call(["git","pull"])
FILE
    ],
  ].each do |(name, contents)|
    path = File.join GENERATED_WEBSITE_PATH, name

    puts "Adding `#{path}'..."

    File.write path, contents

    if path =~ /\.py\z/
      puts "Making `#{path}' executable..."

      system "chmod a+x '#{path}' > /dev/null 2>&1"
    end
  end

  ##############################################################################

  puts "Moving the generated website from `#{GENERATED_WEBSITE_PATH}' to a temporary directory in `#{TEMPORARY_PATH}'..."

  system "mv '#{GENERATED_WEBSITE_PATH}' '#{TEMPORARY_PATH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Checking the branch `#{TARGET_BRANCH}' out..."

  system "git checkout '#{TARGET_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Deleting the contents from previous deployments..."

  previous_deployments_files = Dir["*"] + Dir[".*"] - [".", "..", ".vagrant", ".git"]

  system "rm -rf #{previous_deployments_files.map { |x| "'#{x}'" }.join(" ")} > /dev/null 2>&1"

  ##############################################################################

  puts "Copying the contents of the temporary directory `#{TEMPORARY_PATH}' back in..."

  system "rsync -av '#{TEMPORARY_PATH}'/ ./ > /dev/null 2>&1"

  ##############################################################################

  puts "Committing..."

  system "git add -A && git commit -m 'Automatic update of website' > /dev/null 2>&1"

  ##############################################################################

  puts "Pushing changes to `#{REMOTE_URL}'..."

  system "git push '#{REMOTE_URL}' '#{TARGET_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  puts "Calling `#{UPDATE_URL}' to update..."

  system "curl '#{UPDATE_URL}' > /dev/null 2>&1"

  ##############################################################################

  puts "Checking the branch `#{SOURCE_BRANCH}' out..."

  system "git checkout '#{SOURCE_BRANCH}' > /dev/null 2>&1"

  ##############################################################################

  puts <<-SUCCESS
Deployment succeeded!

Go to `#{FINAL_URL}' to see the results.
SUCCESS

  end
end
