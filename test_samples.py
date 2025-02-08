import pytest  #PYTEST IMPLEMENTATION AROUND XML FILE AND HTML REPORTS --VERY POWERFUL TOOL
               # pytest -rA --junitxml="Report.xml"  --XML FILE EXTRACTION
               # pytest -rA -html=report.html

def add(a , b):
    return a+b

def divide(b, c):
    return b/c

def test_division():
    assert 2/3 == 0.6666
    assert 10/2==5
    assert 21/10==2.1
    assert 21/10==2

def test_addition():
    assert 2+5==1


def test_addition_errors():
    with pytest.raises(TypeError):
        add("two", "five") #failed section


