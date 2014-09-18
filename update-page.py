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
