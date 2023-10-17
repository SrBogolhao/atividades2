#API da Santander Dev Week 2023
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

#Extract
import pandas as pd
df = pd.read_csv('user id.csv')
user_ids = df('user id').tolist()
print(user_ids)

from ast import NameConstant
import requests
import json

def get_user('id'):
  response = requests.get(f'{sdw2023_api_url}/users/id')
  return response.jason() if response.status_code == 200 else None

user = [user for id in user_ids if(user := get_user(id))is not None]
print(json.dumps(users, indent=2))

#Transform
!pip install openai

openai_api_key = 'key'

import openai

openai_api_key = openai_api_key

def generat_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system", 
        "content": "voçê é um especialista trenamento para hipertrofia."
      },
      {
        "role": "user", 
        "content": f"crie uma mensagem para{user['name']} sobre treinamento para hipertrofia(máximo de 100 caracteres)"
      }
    ]
)
  
return completion.choices[0].menssage.content.strip('\"')

for user in users:
  news = generete_ai_new(user)
  print(news)
  user['news'].append({
      "icon": "urlicon"
      "description": news
  })

#Load
def update_user(user)
  response = requests.put(f"{sdw2023_api_url}/users/{user['id'], json=user}")
  return true if response.status_code == 200 else false

for user in users:
  success = updat_user(user)
  print(f"user {user['name']}update?{success}!")