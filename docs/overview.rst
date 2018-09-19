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
.. http://creativecommons.org/licenses/by/4.0
..
.. This file is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

====================================
H2O Model Builder Service Overview
====================================

The Acumos H2O Model Builder service provides a way to create H2O models from a dataset
and also upload them through model-management to save them for use in h2o-model-runner. 
The Acumos H2O Model Builder service is a Flask application that provides RESTFul
endpoints, with a swagger spec detailing each endpoint.

The source is available from the Linux Foundation Gerrit server:

    https://gerrit.acumos.org/r/gitweb?p=model-builder/h2o-model-builder.git;a=summary

The CI/CD jobs are in the Linux Foundation Jenkins server:

    https://jenkins.acumos.org/view/model-builder/h2o-model-builder/

Issues are tracked in the Linux Foundation Jira server:

    https://jira.acumos.org/secure/Dashboard.jspa

Further information is available from the Linux Foundation Wiki:

    https://wiki.acumos.org/
