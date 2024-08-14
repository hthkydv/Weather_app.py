import requests
from dotenv import load_dotenv
import os

load_dotenv()

Api_key = os.getenv('API_KEY') 
Base_url=os.getenv("Base_URL")

api_key = Api_key
city = "London"
base_url = Base_url
complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"

response = requests.get(complete_url)

# Check if the request was successful
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except ValueError:
        print("Error: Unable to parse the response as JSON.")
else:
    print(f"Error: Received status code {response.status_code}")
    print(f"Response content: {response.text}")
