﻿import pytest
from pxtool.models.output.pxfile.keywords._languages import _Languages
    
def test_Languages_set_valid():
    obj = _Languages()
    assert not obj.has_value()   
    obj.set(["en"])
    assert obj.has_value()    
    assert obj.get_value() == ["en"]
    
def test_Languages_set_invalid_raises():
    obj = _Languages()
    with pytest.raises(Exception):
       obj.set(["bad_string"])
    
def test_Languages_duplicate_set_raises():
    obj = _Languages()
    obj.set(["en"])
    with pytest.raises(Exception):
        obj.set(["en"])