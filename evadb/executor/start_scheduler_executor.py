# coding=utf-8
# Copyright 2018-2023 EvaDB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import multiprocessing
from evadb.database import EvaDBDatabase
from evadb.executor.abstract_executor import AbstractExecutor
from evadb.parser.start_scheduler_statement import StartSchedulerStatement
from evadb.utils.logging_manager import logger

class StartSchedulerExecutor(AbstractExecutor):
    def __init__(self, db: EvaDBDatabase, node: StartSchedulerStatement):
        super().__init__(db, node)

    def exec(self, *args, **kwargs):
        logger.debug("No op for StartSchedulerExecutor")