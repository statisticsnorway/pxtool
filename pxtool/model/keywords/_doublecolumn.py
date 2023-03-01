﻿from pxtool.model.util._px_super import _PxValueByKey
from pxtool.model.util._px_valuetype import _PxBool
from pxtool.model.util._px_keytypes import _KeytypeVariableLang
from pxtool.model.util._line_validator import LineValidator

class _Doublecolumn(_PxValueByKey): 

    pxvalue_type:str = "_PxBool"
    is_language_dependent:bool = True


    def set(self, doublecolumn:bool, variable:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, doublecolumn)
        LineValidator.is_bool( self._keyword, doublecolumn)
        my_value = _PxBool(doublecolumn)
        my_key = _KeytypeVariableLang(variable, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

