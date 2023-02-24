﻿from pxtool.model.util._px_super import _PXValueByKey, _PxString
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_KEYS(_PXValueByKey): 

    def set(self, keys:str, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, keys)
        LineValidator.is_string( self._keyword, keys)
        LineValidator.regexp_string("^(CODES|VALUES)$", self._keyword, keys)
        my_value = _PxString(keys)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
