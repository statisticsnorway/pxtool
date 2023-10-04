﻿import pytest
from pxtool.models.output.pxfile.keywords._creation_date import _CreationDate
    
def test_CreationDate_set_valid():
    obj = _CreationDate()
    assert not obj.has_value()   
    obj.set("a string")
    assert obj.has_value()    
    assert obj.get_value() == "a string"
    
def test_CreationDate_duplicate_set_raises():
    obj = _CreationDate()
    obj.set("a string")
    with pytest.raises(Exception):
        obj.set("a string")