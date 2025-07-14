
import requests

class test_DemoClass():
    base_url = "https://jsonplaceholder.typicode.com"
    # send request
    response = requests.get(f"{base_url}/posts/1")
    # assert
    assert response.status_code == 200
    assert response.json()['userId'] == 1
    assert response.json()['id'] == 1
    print(response.json())


