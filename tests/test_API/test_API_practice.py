import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response.json())
# assert response.status_code == 200
# data= response.json()
# assert data["id"] == 1
# assert "title" in data
#
# response = requests.get("https://jsonplaceholder.typicode.com/posts/2")
# data = response.json()
# assert data["id"] == 2
# assert "title" in data
#
# request = requests.post("https://jsonplaceholder.typicode.com/posts/99")
# print(request.status_code)
# assert request.status_code == 404
# data = request.json()
# print(data)

def test_create_post(api_json_dummy):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=api_json_dummy)
    assert response.status_code in [200, 201]
    data = response.json()
    assert data["title"] == "foo"
    assert data["body"] == "bar"
    assert data["userId"] == 1



def test_check_get(api_url):
    headers = {"Accept": "application/json"}
    response = requests.get(f'{api_url}/posts/1', headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    print(response.headers["Content-Type"])

def test_put_post():
    payload = {
        "id": 1,
        "title": "foo updated",
        "body": "bar updated",
        "userId": 1
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "foo updated"
    assert data["body"] == "bar updated"
    assert data["userId"] == 1



def test_patch_post():
    payload = {
        "title": "foo patched"
    }

    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=payload
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "foo patched"

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code in (200, 204)

def test_headers():
    headers = {"Accept": "application/json"}
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", headers=headers)

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith("application/json")