﻿from pxtool.model.util._px_super import _PxSingle
from pxtool.model.util._px_valuetype import _PxString
from pxtool.model.util._line_validator import LineValidator

class _FirstPublished(_PxSingle): 

    pxvalue_type:str = "_PxString"
    may_have_language:bool = False

    def __init__(self) -> None:
        super().__init__("FIRST-PUBLISHED")

    def set(self, first_published:str) -> None:
        """ In use? """
        LineValidator.is_not_None( self._keyword, first_published)
        LineValidator.is_string( self._keyword, first_published)
        my_value = _PxString(first_published)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e

    def get_value(self) -> str:
        return super().get_value().get_value()

