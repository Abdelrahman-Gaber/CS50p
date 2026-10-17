import requests
import sys
import json

payload = {"apiKey": "*****"}
try:
    n = float(sys.argv[1])
    request = requests.get("https://rest.coincap.io/v3/assets/bitcoin", params=payload)
    response_json = request.json()
    bitcoin_price = float(response_json['data']['priceUsd'])
    print(f"{(n * bitcoin_price):,.4f}")

except requests.RequestException:
    sys.exit("We ran into an error please try again later!")
except requests.exceptions.JSONDecodeError:
    sys.exit("Invalid response != 200")
except ValueError:
    sys.exit("Command-line argument is not a number")
except IndexError:
    sys.exit("Missing command-line argument")