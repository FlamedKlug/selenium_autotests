import requests
import pytest

host_name = 'https://api.pokemonbattle.me/v2'

def test_status_code():
    response = requests.get(url=f'{host_name}/trainers', params={'trainer_id': '263'})
    assert response.status_code == 200, 'Не правильный статус ответа'
    if 'message' in response.json():
        assert response.json()['message'] == 'Тренер отсутствует'
    else:
        assert response.json()['data'][0]['trainer_name'] == 'Громозека'
