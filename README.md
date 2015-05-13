The Programming Languages Laboratory website
============================================

Source code for The Programming Languages Laboratory website at
<https://pl.cs.jhu.edu>.

Development
-----------

The website is developed using [Jekyll][jekyll], a static site generator. It's a
[Ruby gem][rubygems] that should be installed using [Bundler][bundler].

Assets dependencies are managed using [Bower][bower], a package manager for the
web.

The design uses [Bootstrap][bootstrap], with a theme from
[Bootswatch][bootswatch].

### Installation

Here are the instructions on how to set everything up to run the website on your
machine:

#### Contributing with contents

Make sure you have a recent enough version of [Ruby][ruby] (2.0.0 or
up). GNU/Linux packages are available for all major distributions, OS X already
comes with it and Windows users can rely on [RubyInstaller][ruby-installer].

You must be able to install [Ruby gems][rubygems] (packages/libraries). Use the
following to install [Bundler][bundler]:

```console
$ gem install bundler
```

Then, use [Bundler][bundler] to install the appropriate version of the
dependencies (including [Jekyll][jekyll]):

```console
$ bundle install
```

Finally, run [Jekyll][jekyll] in development server mode:

```console
$ bundle exec jekyll serve
```

Now, visit the URI [Jekyll][jekyll] informed (usually <http://localhost:4000>)
on your browser.

Any changes you make to the website are immediately available on your browser,
just refresh the page.

The contents are [Markdown][kramdown] files, which you can edit on your regular
text editor.

#### Contributing with design

If you want to fiddle with the design of the website (instead of just
contributing with content), in addition to following the above steps, you may
need to add new assets dependencies (e.g. [jQuery][jquery],
[Bootstrap][bootstrap]). Those are managed by [Bower][bower], which is a
[Node.js][node-js] package available through [npm][npm].

Installing [Node.js][node-js] is as easy as installing a package in
GNU/Linux. OS X and Windows users can use the installer available on the
[website][node-js-installer].

Then, install [Bower][bower] using:

```console
$ npm install -g bower
```

Dependencies are stored in `assets/vendor`.

CSS is pre-processed with [Sass][sass], as you may notice by the `.scss`
extension.

Deployment
----------

[Jekyll][jekyll] generates a static website under the `_site` folder with the
following command:

```console
$ bundle exec jekyll build
```

The contents of that folder should be copied to the webserver. How this step is
performed is still under discussion. We're aiming at an automatic solution,
i.e. any push the the `master` branch will trigger a build.


[jekyll]: http://jekyllrb.com
[rubygems]: https://rubygems.org/
[bower]: http://bower.io/
[bundler]: http://bundler.io/
[ruby]: https://www.ruby-lang.org
[bootstrap]: http://getbootstrap.com/
[bootswatch]: http://bootswatch.com/
[ruby-installer]: http://rubyinstaller.org/
[node-js]: https://nodejs.org/
[jquery]: http://jquery.com/
[npm]: https://www.npmjs.com/
[homebrew]: http://brew.sh/
[node-js-installer]: https://nodejs.org/download/
[kramdown]: http://kramdown.gettalong.org/quickref.html
[sass]: http://sass-lang.com/
