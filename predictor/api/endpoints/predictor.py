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
from predictor.api.serializers import async_scoring_fields
from predictor.api.namespaces import predictor_namespace as api
from predictor.api.parser import predictor_csv
from flask_restplus import Resource, abort


def placeholder():
    abort(400, 'TODO: This API is just a stub. Method not yet implemented')


@api.route('/syncPredictions')
class SyncScoringCollection(Resource):
    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(413, 'Request Entity Too Large')
    @api.response(500, 'Internal Server Error')
    @api.header('ATT-ModelVersion', 'Version of the model, ie) 1.0', required=True)
    @api.header('ATT-ModelKey', 'The model key pointing to PMML model', required=True)
    @api.header('ATT-DatasetKey', 'The Dataset assocaited with input data', required=False)
    @api.header('Content-Type', 'text/csv', required=True)
    @api.header('CodeCloud-Authorization', 'Authorization for codecloud', required=True)
    @api.header('Authorization', 'Basic Authorization', required=True)
    @api.expect(predictor_csv, validate=False)
    def post(self):
        """
        Score the specified model against the specified dataset payload to get a prediction
        """
        placeholder()


@api.route('/asyncPredictions')
class AsyncScoringCollection(Resource):
    @api.response(202, 'Accepted')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(413, 'Request Entity Too Large')
    @api.response(500, 'Internal Server Error')
    @api.header('ATT-ModelVersion', 'Version of the model, ie) 1.0', required=True)
    @api.header('ATT-ModelKey', 'The model key pointing to PMML model', required=True)
    @api.header('ATT-MessageId', 'This is the correlation id to associate the callback response to.', required=False)
    @api.header('ATT-ReturnURL',
                'This is the return url which the service will send an acknowledgment when scoring has been completed',
                required=False)
    @api.header('Content-Type', 'application/json', required=True)
    @api.header('CodeCloud-Authorization', 'Authorization for codecloud', required=True)
    @api.expect(async_scoring_fields, validate=False)
    def post(self):
        """
        Perform asynchronous prediction

        Asynchronously score the specified model against the specified read dataset key and write back to the specified
        write dataset key
        """
        placeholder()


@api.route('/status/<string:statusKey>')
class StatusScoringCollection(Resource):
    @api.response(200, 'Ok')
    @api.response(400, 'Bad Request')
    @api.response(401, 'Unauthorized')
    @api.response(403, 'Forbidden')
    @api.response(413, 'Request Entity Too Large')
    @api.response(500, 'Internal Server Error')
    @api.header('Authorization', 'Basic Authorization', required=True)
    def get(self, statusKey):
        """
        Get the status of the predictions
        """
        placeholder()
