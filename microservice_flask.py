# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
from flask import Flask
from predictor.api.restplus import api, blueprint
from predictor.api.endpoints.predictor import api as predictor_namespace

app = Flask(__name__)


def initialize_app(flask_app):
    api.add_namespace(predictor_namespace)
    app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    app.run(host='0.0.0.0', debug=True, port=8061)


if __name__ == '__main__':
    main()
