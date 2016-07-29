# asknot-ng

Ask not what `$ORG` can do for you, but what you can do for `$ORG`.

The gist of this “next generation asknot” rewrite is to make it as configurable as
possible.  There is a primary script, ``asknot-ng.py``
that works like a static-site generator.  It takes as input three things:

- A questions file, written in yaml (see the [example][example-questions] or
  [Fedora’s file][fedora-questions]).  You’ll have to write your own one of
  these.
- A template file, written in mako (the [default][default-template] should work
  for everybody).
- A ‘theme’ argument to specify what CSS to use.  The default is nice enough,
  but you’ll probably want to customize it to your own use case.

## Giving it a run
Install the requirements, first.

Clone the repo::

    $ git clone https://github.com/rahulrrixe/asknot-ng.git
    $ cd asknot-ng

Create a virtualenv into which you can install the module.

    $ virtualenv --system-site-packages venv
    $ source venv/bin/activate
    $ python setup.py develop

Run the script with the Fedora configuration::

    $ ./asknot-ng.py templates/index.html questions/fedora.yml l10n/fedora/locale --theme fedora
    Wrote build/en/index.html

and open up `build/en/index.html` in your favorite browser.

## Contributing back

``asknot-ng`` is licensed GPLv3+ and we’d love to get patches back containing
even the things you might not think we want.  If you have a questions file for
your repo, a modified template, or a CSS theme for your use case, please
[send them to us][patches].  It would be nice to build a library of deployments
so we can all learn.


Of course, bug reports and patches to the main script are appreciated as
always.

Happy Hacking!

[example-questions]: https://github.com/fedora-infra/asknot-ng/blob/develop/questions/example.yml
[fedora-questions]: https://github.com/fedora-infra/asknot-ng/blob/develop/questions/fedora.yml
[default-template]: https://github.com/fedora-infra/asknot-ng/blob/develop/templates/index.html
[requirements]: https://github.com/fedora-infra/asknot-ng/blob/develop/requirements.txt
[patches]: https://help.github.com/articles/editing-files-in-another-user-s-repository/
[wcidfm]: http://whatcanidoformozilla.org
[wcidff]: http://whatcanidoforfedora.org
[jdm]: http://www.joshmatthews.net
[wham]: http://wham.fi
[asknot-contribs]: https://github.com/jdm/asknot/contributors
