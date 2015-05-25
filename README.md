The Programming Languages Laboratory website
============================================

Source code for The Programming Languages Laboratory website at
<https://pl.cs.jhu.edu>.

Development
-----------

Serve the website on your local machine for development with a container
provided by [Docker][what-is-docker] and managed by
[Docker Compose][docker-compose].

1. Install [Docker and Docker Compose][docker-compose-installation]. If you're
   on GNU/Linux, you can choose to install them directly on your machine. If
   you're on Windows or OS X (or GNU/Linux), you might prefer to use a virtual
   machine with those tools already configured. Here are the steps to do that:

   1. Install [VirtualBox][virtualbox].
   2. Install [Vagrant][vagrant].
   3. Install [Docker Compose plugin for Vagrant][vagrant-docker-compose].
   4. Run `vagrant up` to start the virtual machine.
   5. Run `vagrant ssh` to login to the virtual machine and proceed with the
      next steps.

2. Run:

  ```console
  $ docker-compose up jekyll
  ```

3. If you're running [Docker][docker] natively on Linux, visit
   <http://localhost:4000>. If you're on OS X or Windows and you're using
   [`boot2docker`][boot2docker], check the IP of the virtual machine with
   `boot2docker ip` and visit <http://ip:4000>.

Edit the [Markdown][kramdown] files with the contents and the results should be
immediately available for preview by refreshing the browser.

Install assets dependencies
---------------------------

Assets dependencies (e.g. [jQuery][jquery], [Bootstrap][bootstrap]) are managed
using [Bower][bower], a package manager for the web.

In order to add a dependency, edit `bower.json` and run:

```console
$ docker-compose run --rm bower
```

The packages are installed under `assets/vendor/`.

Deployment
----------

[Jekyll][jekyll] generates a static website under the `_site` folder with the
following command:

```console
$ docker-compose run --rm jekyll build
```

The contents of that folder should be copied to the webserver. How this step is
performed is still under discussion. We're aiming at an automatic solution,
i.e. any push the the `master` branch will trigger a build.


[jekyll]: http://jekyllrb.com
[bower]: http://bower.io/
[jquery]: http://jquery.com/
[kramdown]: http://kramdown.gettalong.org/quickref.html
[bootstrap]: http://getbootstrap.com/
[what-is-docker]: https://www.docker.com/whatisdocker/
[docker-compose]: http://docs.docker.com/compose/
[docker-compose-installation]: https://docs.docker.com/compose/install/
[boot2docker]: http://boot2docker.io/
[docker]: https://www.docker.com/
[virtualbox]: https://www.virtualbox.org/
[vagrant]: https://www.vagrantup.com/
[vagrant-docker-compose]: https://github.com/leighmcculloch/vagrant-docker-compose
