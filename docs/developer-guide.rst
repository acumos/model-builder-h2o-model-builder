.. ===============LICENSE_START=======================================================
.. Acumos CC-BY-4.0
.. ===================================================================================
.. Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
.. ===================================================================================
.. This Acumos documentation file is distributed by AT&T
.. under the Creative Commons Attribution 4.0 International License (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..

..      http://creativecommons.org/licenses/by/4.0
..
.. This file is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

=================================================
Acumos H2O Model Builder Python Developer Guide
=================================================
More coming soon!

Testing
=======

We use a combination of ``tox``, ``pytest``, and ``flake8`` to test
``modelbuilder``. Code which is not PEP8-compliant, with an exception
for line length increased to 120 characters, considered a failing test.
Furthermore, code which fails pyflakes and pycode style is also considered
failing. Example tool usage is below:

.. code:: bash

    $ pip install autopep8 pyflakes pycodestyle
    $ cd h2o-model-builder
    $ autopep8 -r --in-place modelbuilder


Run tox directly:

.. code:: bash

    $ cd h2o-model-builder
    $ tox

You can also specify certain tox environments to test:

.. code:: bash

    $ tox -e py34  # only test against Python 3.4
    $ tox -e flake8  # only lint code

And finally, you can run pytest directly in your environment *(recommended starting place)*:

.. code:: bash

    $ pytest
    $ pytest -s   # verbose output
