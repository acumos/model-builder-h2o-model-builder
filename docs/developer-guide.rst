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
This H2O Model builder builds H2O models given a dataset which is a location to read the data to train the model as well as a validation dataset.   This service has a dependency on dataset service and dataset service for this operation of building the model.   Once the model is built, the user may upload the model to model-management using the export method so this service also has a dependency on model-management service.   

This service also uses memcache to store model generation history information as building the model happens asynchronously. 

The main class to start this service is /h2o-model-builder/microservice_flask.py

The command line interface gives options to run the application.   Type help for a list of available options.   
> microservice_flask.py  help
usage: microservice_flask.py [-h] [--host HOST] [--settings SETTINGS]  [--port PORT]

By default without adding arguments the swagger interface should be available at: http://localhost:8061/v2/

Testing
=======

The only prerequisite for running unit testing is installing python and tox.   It is recommended to use a virtual environment for running any python application.  If using a virtual environment make sure to run "pip install tox" to install it

For testing the actual service, memcache will need to be running on the system.
    https://memcached.org/

We use a combination of 'tox', 'pytest', and 'flake8' to test
'h20-model-builder'. Code which is not PEP8 compliant (aside from E501) will be
considered a failing test. You can use tools like 'autopep8' to
"clean" your code as follows:

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
