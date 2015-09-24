FROM ruby:2.2.3

# Install required packages.

RUN apt-get update
RUN apt-get install -y nodejs

# Setup Jekyll and Ruby dependencies.

WORKDIR /srv/jekyll
COPY . /srv/jekyll
RUN bundle install
