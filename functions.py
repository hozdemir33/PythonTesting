def add_twoNumber(x, y):
  return x+y

def subtra_two_Numbers(x, y):
    return x-y

def div_twoNumber(x, y):
    return x / y

def test_add_twoNumber():
    add_twoNumber(3,4)
    assert add_twoNumber(3,4)==7


def test_subtract_twoNum():
    assert subtra_two_Numbers(2,3)==-1


def test_dividnumber():
    assert div_twoNumber(10,2)==5

    # f(x)=2x-1  if x=5 f(5)=9

def functionValue( x, y):
    return 2*x-y;


def test_funtionalValue():
    assert functionValue(10,3)==17







