import requests

def test_connect_to_agt_world():
    response = requests.get('https://agt.world')
    assert response.status_code == 200
