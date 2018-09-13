# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
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
from setuptools import setup


setup(
    author='Pavel Kazakov, Ryan Hull',
    author_email='pk9069@att.com, rh183@att.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
    ],
    description=""""H2O Predictor provides the capability to run predictions on H2O and POJO
    and MOJO models and runs predictions either synchronously or asynchronously.""",
    entry_points="""
    [console_scripts]
    h2o-model-runner=microservice_flask:main
    """,
    keywords='acumos machine learning model runner server predictor h2o ml ai',
    license='Apache License 2.0',
    name='predictor-management',
    python_requires='>=3.4',
    url='https://gerrit.acumos.org/r/#/admin/projects/h2o-model-runner.git',
    version=1.0,
)
