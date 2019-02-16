#!/usr/bin/env bash

# clean the previous build
sudo rm -rf .sass-cache;
sudo rm -rf _site;

# fetch the lastest source
git pull origin source;

# jekyll build
docker-compose run --rm jekyll jekyll build > /dev/null 2>&1

# change owner to www-data
sudo chown --recursive www-data:www-data _site

# transfer to Apache www path
rsync -ahr --exclude=.git --exclude=pl --exclude=oose --stats _site/ /var/www/pl.cs.jhu.edu/

# clean up
sudo rm -rf .sass-cache;
sudo rm -rf _site;

# use previous rack build
rake deploy:no_vagrant
