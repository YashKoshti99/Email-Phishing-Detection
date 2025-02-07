import requests
import json

# URL for the uncompressed JSON file
url = "http://data.phishtank.com/data/online-valid.json"

# Download the file
response = requests.get(url)

if response.status_code == 200:
    print("Data downloaded successfully!")

    # Load the JSON data
    phishing_data = json.loads(response.text)
    print(f"Loaded {len(phishing_data)} phishing records!")
else:
    print("Failed to download data. HTTP Status Code:", response.status_code)
    prin("Yash")
