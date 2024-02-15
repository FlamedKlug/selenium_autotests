import requests

host_name = 'https://api.pokemonbattle.me/v2'
trainer_token = '27b708e3ec7165fd0b85bdfb6346fe94'
trainer_id = 263

response = requests.post(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {"name": "Бульбазавр",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"}
)
print ('Создан покемон: ', response.json())

pokemon_id = response.json()["id"]

response = requests.put(
    url = host_name + '/pokemons',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            "name": "Рамзес",
            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
            }
)
print ('Заменили имя на Рамзес: ', response.json())

response = requests.post(
    url = host_name + '/trainers/add_pokeball',
    headers = {'Content-Type': 'application/json',
               'trainer_token': trainer_token},
    json = {
            "pokemon_id": pokemon_id,
            }
)
print(f"Покемон {pokemon_id} пойман в покебол: {response.json()}")

