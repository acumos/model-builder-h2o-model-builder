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
from flask_restplus import fields
from predictor.api.namespaces import predictor_namespace as api

async_scoring_fields = api.model("ScoringFields", {
    "readDatasetKey": fields.String(required=True,
                                    description='Dataset key to be used for scoring',
                                    example="jdbc_m09286_string_1529617890081"),
    "writeDatasetKey": fields.String(required=True, description='Dataset key to be write back results from scoring',
                                     example="jdbc_m09286_string_1529617890082")
})
