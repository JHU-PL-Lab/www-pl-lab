The Programming Languages Laboratory website
============================================

Source code for The Programming Languages Laboratory website at
<https://pl.cs.jhu.edu>.

Development
-----------

### Basic

Serve the website on your local machine for development.

1. Install [VirtualBox][virtualbox].
2. Install [Vagrant][vagrant].
3. Run:

   ```console
   $ vagrant up
   $ vagrant exec docker-compose up jekyll
   ```

4. Visit <http://localhost:4000>.
5. (Optional) To enable auto-reloading features (i.e. changes to source files
   are immediately available on the browser) run:

   ```console
   $ vagrant rsync-auto
   ```

   Edit the [Markdown][kramdown] files with the contents and the results should
   be immediately available for preview by refreshing the browser.

### Install assets dependencies

Assets dependencies (e.g. [jQuery][jquery], [Bootstrap][bootstrap]) are managed
using [Bower][bower], a package manager for the web.

In order to add a dependency, edit `bower.json` and run:

```console
$ vagrant exec docker-compose run --rm bower
```

The packages are installed under `assets/vendor/`.

Deployment
----------

[Jekyll][jekyll] generates a static website under the `_site` folder with the
following command:

```console
$ vagrant exec docker-compose run --rm jekyll build
```

The contents of that folder should be copied to the webserver. How this step is
performed is still under discussion. We're aiming at an automatic solution,
i.e. any push the the `master` branch will trigger a build.


[jekyll]: http://jekyllrb.com
[bower]: http://bower.io/
[jquery]: http://jquery.com/
[kramdown]: http://kramdown.gettalong.org/quickref.html
[bootstrap]: http://getbootstrap.com/
[virtualbox]: https://www.virtualbox.org/
[vagrant]: https://www.vagrantup.com/
