import requests

def test_connect_to_atg_world():
    response = requests.get('https://atg.world')
    assert response.status_code == 200
