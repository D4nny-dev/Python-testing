#Requiere up viertual eviroment
#Example test cover with py-cov

from mypkg import my_module as m
from mypkg.mysubpkg import submodule as s

def test_my_funtion():
    assert m.my_funtion()=="Module: my_module.py"
    assert m.my_funtion2()=="Module: my_module.py"
    
    

