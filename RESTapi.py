import requests

def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200

def test_testing():
    print("this is api testing")


def test_responsecode200():
    print("correct")

