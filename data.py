import requests

URL = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(URL, params=parameters)
response.raise_for_status()
data = response.json()

question_data = data['results']

# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
