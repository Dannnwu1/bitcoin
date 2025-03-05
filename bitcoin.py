import sys
import requests

price_index = r"https://api.coindesk.com/v1/bpi/currentprice.json"

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")


def get_price():
    bitcoin_qty = float(sys.argv[1])
    response = requests.get(price_index)
    report = response.json()
    bitcoin_price = report["bpi"]["USD"]["rate_float"]
    total_amount = bitcoin_qty * bitcoin_price
    print(f"${total_amount:,.4f}")


def main():
    while True:
        try:
            get_price()
            break
        except requests.RequestException:
            pass
        except ValueError:
            sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
