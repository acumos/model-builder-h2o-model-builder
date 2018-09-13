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
from flask import Blueprint
from flask_restplus import Api


authorizations = {
    'basicAuth': {
        'type': 'basic',
    }
}


blueprint = Blueprint('cmlp', __name__, url_prefix='/v2')
api = Api(
    blueprint,
    version=2,
    title='H2O Predictor',
    default_label='H2O Predictor',
    validate=True,
    description='The H2O predictor provides a mechanism for scoring using POJO and MOJO models',
    authorizations=authorizations,
    security='basicAuth'
)
