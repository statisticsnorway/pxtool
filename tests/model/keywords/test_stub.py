﻿import pytest
from pxtool.model.keywords._stub import _Stub
    
def test_Stub_set_valid():
    obj = _Stub()
    obj.set(["a string"],"no")
    assert obj.get_value("no") == ["a string"]
    
def test_Stub_used_languages():
    obj = _Stub()
    obj.set(["a string"],"no")
    assert "no" in obj.get_used_languages()

def test_Stub_reset_language():
    obj = _Stub()
    obj.set(["a string"],)
    assert None in obj.get_used_languages()
    obj.reset_language_none_to(None)    
    obj.reset_language_none_to("no")         
    assert not None in obj.get_used_languages()
    assert "no" in obj.get_used_languages()  

    
def test_Stub_duplicate_set_raises():
    obj = _Stub()
    obj.set(["a string"],"no")
    with pytest.raises(Exception):
        obj.set(["a string"],"no")