# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

import sys
import traceback
import typing as t
import warnings


class TaipyGuiWarning(UserWarning):
    """NOT DOCUMENTED

    Warning category for Taipy warnings generated in user code.
    """

    _tp_debug_mode = False

    @staticmethod
    def set_debug_mode(debug_mode: bool):
        TaipyGuiWarning._tp_debug_mode = (
            debug_mode if debug_mode else hasattr(sys, "gettrace") and sys.gettrace() is not None
        )


def _warn(message: str, e: t.Optional[BaseException] = None):
    warnings.warn(
        (
            f"{message}:\n{''.join(traceback.format_exception(type(e), e, e.__traceback__))}"
            if e and TaipyGuiWarning._tp_debug_mode
            else f"{message}:\n{e}"
            if e
            else message
        ),
        TaipyGuiWarning,
        stacklevel=2,
    )
