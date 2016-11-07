Environment Setup
-----------------

In order to ensure that the appropriate software is available,
an environment should be created on your machine.
For this exercise it is highly recommended that the environment should either
be created with Continuum Analytics
`Miniconda <http://conda.pydata.org/miniconda.html>`__, or via a virtual
environment. If you have experience with anaconda this is the
encouraged environment.

Anaconda
........

* Download the miniconda distribution from the above link. For this exercise
  choose the Python 2.7 installation for your platform.
* Install the distribution in the way that is appropriate for your platform.
* Install the necessary modules

Note that if you already have Miniconda/Anaconda installed on your machine
this can be done by creating an environment and then activating it, ie:

.. code:: bash

  conda create -n new_env python=2.7
  . activate new_env

The following modules/packages should be installed:

* flask

To ensure consistency these modules should be installed via ``conda``, ie::

  conda install flask

You are free to install other tools and modules that you commonly use, but
the above are necessary for the completion of the project.

**Note**: If there are multiple versions of python on your system, ensure that
the environment is configured so that this version will be used (by
setting ``$PATH``, etc.).

Virtualenv
..........

The environment can also be created with `virtualenv
<https://pypi.python.org/pypi/virtualenv/>`__. The procedure would
be something similar to:

.. code:: bash

  virtualenv my_env
  . my_env/bin/activate
  pip install flask

Other Software
..............

In addition to a python environment, `curl <https://en.wikipedia.org/wiki/CURL>`__
should also be installed for interacting with the software that will be
developed. On most Linux distributions (and in MacOS) it is installed
by default.

Skeleton
--------

There is a skeleton webservice in this directory that can be used to
verify that the environment is working::

  export FLASK_APP=webapp.py
  flask run

Visiting http://localhost:5000 (either with a web browser or CURL) should
display a "hello world" message if the environment is configured correctly::

  [vagrant@geostellar2 ~]$ curl http://localhost:5000
  Hello World

  [vagrant@geostellar2 ~]$ 
