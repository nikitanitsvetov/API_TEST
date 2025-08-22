import requests
import json

def test_get_all_posts():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200


def test_get_one_post():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/42').json()
    print(response)


def test_post_new():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "title": "foo",
        "body": "bar",
        "userId": 1,
        "id": 101
    })
    response = requests.post('https://jsonplaceholder.typicode.com/posts',data=body,headers=headers)
    print(response.json())
    print(response.status_code)
    response_data = response.json()
    assert response_data['body'] == 'bar'

def test_update_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "title": "foo6",
        "body": "bar4",
        "userId": 1,
        "id": 101
    })
    response = requests.put('https://jsonplaceholder.typicode.com/posts/42',data=body,headers=headers)
    print (response.text)
    response_data = response.json()
    assert response_data['body'] == 'bar4'

def test_remove():
    response = requests.delete('https://jsonplaceholder.typicode.com/posts/101')
    assert response.status_code == 200
