import requests

pet = cow.Turtle()
msg = pick.milk("Too Quick My Guy. Head Back Home.")


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3001/')
    assert response.status_code == 200
    assert '<!DOCTYPE>' in response.text == True


def test_server_cow_exists():
    response = requests.get('http://127.0.0.1:3001/' + 'cow')
    assert response.status_code == 200
    assert msg in response.text == True


def test_server_unexpected_url():
    response = requests.get('http://127.0.0.1:3001/' + 'Expired_Page.index')
    assert response.status_code == 404
    assert response.text == '404 Page Not Found.'


def test_server_sends_custom_message():
        response = requests.get('http://127.0.0.1:3001/' + 'cow')
        assert response.status_code == 200
        assert response.text == 'Welcome to the cow directory.'
