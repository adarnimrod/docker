Docker
#######

.. image:: https://travis-ci.org/adarnimrod/docker.svg?branch=master
    :target: https://travis-ci.org/adarnimrod/docker

Provision Docker engine.

Requirements
------------

See :code:`meta/main.yml` and assertions at the top of :code:`tasks/main.yml`.

Role Variables
--------------

See :code:`defaults/main.yml`.

Dependencies
------------

See :code:`meta/main.yml`.

Example Playbook
----------------

See :code:`tests/playbook.yml`.

Testing
-------

Testing requires Python 2.7, Tox, Vagrant and Virtualbox. To test simply run
:code:`tox`. `Pre-commit <http://pre-commit.com/>`_ is also setup for this
project.

License
-------

This software is licensed under the MIT license (see the :code:`LICENSE.txt`
file).

Author Information
------------------

Nimrod Adar, `contact me <nimrod@shore.co.il>`_ or visit my `website
<https://www.shore.co.il/>`_. Patches are welcome via `git send-email
<http://git-scm.com/book/en/v2/Git-Commands-Email>`_. The repository is located
at: https://git.shore.co.il/explore/.

TODO
----

- Test working Ansible Docker modules.
- Test working docker-gc.
- Test if forwarding is allowed in UFW.
- email alias.
- flush handlers and wait for socket?
- Log to syslog.
- Boot config?
- More configuration options?
