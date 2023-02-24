﻿from pxtool.model.util._px_super import _PXSingle
from pxtool.model.util._line_validator import LineValidator

class _PX_DEFAULT_GRAPH(_PXSingle): 

    def set(self, default_graph:int) -> None:
        """ Not in use """
        LineValidator.is_not_None( self._keyword, default_graph)
        LineValidator.is_int( self._keyword, default_graph)
        my_value = int(default_graph)
        try:
            super().set(my_value)
        except Exception as e:
            msg = self._keyword + ":" +str(e)
            raise type(e)(msg) from e
