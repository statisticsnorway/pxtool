﻿from pxtool.model.util._px_super import _PXValueByKey, _PxBool
from pxtool.model.util._px_keytypes import _keytype_variable_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_DOUBLECOLUMN(_PXValueByKey): 

    def set(self, doublecolumn:bool, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, doublecolumn)
        LineValidator.is_bool( self._keyword, doublecolumn)
        my_value = _PxBool(doublecolumn)
        my_key = _keytype_variable_lang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
