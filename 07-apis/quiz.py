import requests
import json
import html
import random

response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')

data = json.loads(response.text)

results = data['results']

q = results[0]

print(html.unescape(q['question']))

print("Correct:", html.unescape(q['correct_answer']))

answers = []
answers.append(html.unescape(q['correct_answer']))
for a in q['incorrect_answers']:
    answers.append(html.unescape(a))

random.shuffle(answers)

print(answers)

