import requests

QUIZ_API_URL = "https://opentdb.com/api.php"


parameters = {
    "amount": 10,
    "category": 17,
    "type": "boolean"
}

api_response = requests.get(url=QUIZ_API_URL, params=parameters)
api_response.raise_for_status()
api_data = api_response.json()

question_data = api_data["results"]
