#
# ===============LICENSE_START=======================================================
# Acumos
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
from flask_restplus import Resource
from modelbuilder.api.namespaces import model_builder_namespace as api
from modelbuilder.api.v2.serializers import builder_fields
from modelbuilder.api.v2.parsers import error_response_body, error_response_body_500
from modelbuilder.api.business import get_algorithms, create_builder, get_builder_status, export_model


@api.route('/algorithms')
class AlgorithmsResource(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error', error_response_body_500)
    def get(self):
        """Get the list of supported algorithms"""
        return get_algorithms()


@api.route('/builders')
class BuildersResource(Resource):
    @api.response(202, 'Accepted')
    @api.response(400, 'Bad Request', error_response_body)
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error', error_response_body_500)
    @api.expect(builder_fields)
    def post(self):
        """Create a model builder resource"""
        return create_builder()


@api.route('/builders/<string:key>/status')
class BuildersStatusResource(Resource):
    @api.response(200, 'Ok')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error', error_response_body_500)
    def get(self, key):
        """Get the status for the builder"""
        return get_builder_status(key)


@api.route('/builders/<string:key>/exporter')
class BuilderSaveResource(Resource):
    @api.response(201, 'Ok')
    @api.response(404, 'Not Found')
    @api.response(500, 'Internal Server Error', error_response_body_500)
    def post(self, key):
        """Export this model to the model manager service"""
        return export_model(key)
