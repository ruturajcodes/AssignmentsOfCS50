import sys
import requests
import json


if len(sys.argv) == 2:
    try:
        reply = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

reply_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
op = reply_api.json()    # converted the API reply to dictionary form ()
unit_p = op["bpi"]["USD"]["rate_float"]    # when dictionary has dictionary in it, accessing using the keys in this way

bill = unit_p * reply
print(f"${bill:,.4f}")