﻿from pxtool.model.util._px_super import _PXValueByKey, _PxBool
from pxtool.model.util._px_keytypes import _keytype_content_lang
from pxtool.model.util._line_validator import LineValidator

class _PX_DAYADJ(_PXValueByKey): 

    def set(self, dayadj:bool, content:str, lang:str = None) -> None:
        """  """
        LineValidator.is_not_None( self._keyword, dayadj)
        LineValidator.is_bool( self._keyword, dayadj)
        my_value = _PxBool(dayadj)
        my_key = _keytype_content_lang(content, lang)
        try:
            super().set(my_value,my_key)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
