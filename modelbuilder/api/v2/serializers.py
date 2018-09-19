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
from flask_restplus import fields
from api.namespaces import model_builder_v2_namespace as api

builder_fields = api.model('Builder', {
    'algorithm':  fields.String(required=True, description='The algorithm used for building the model',
                                enum=['aggregator', 'drf', 'gbm', 'glm', 'glrm', 'kmeans', 'naivebayes', 'pca']),
    'trainingDatasetKey':  fields.String(required=True, description='The dataset key used for training'),
    'validationDatasetKey':  fields.String(required=True, description='The dataset key used for training'),
    'y': fields.String(required=True, description='Column used as the dependent variable'),
    'x': fields.List(fields.String, required=False, description='Prediction variables')
})
