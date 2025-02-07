#  pytest will run all the files from your current dir /subdirect test


def test_1():

    x=20
    y=20
    assert x==y

def test_2():

    name ="is"
    title ="Selenium is testing framework"

    assert name in title

def test_3():
    name="jenkin"
    title="Jenkins is a CI/CD server"

    assert name in title

