import json
import urllib.request

# an API which randomly selects 15 True/False questions
url = "https://opentdb.com/api.php?amount=15&type=boolean"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    question_data = data["results"]
