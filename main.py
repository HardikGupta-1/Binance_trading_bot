from client import get_client
from orders import market_order, limit_order, stop_limit_order

def main():
    client = get_client()

    SYMBOL = "BTCUSDT"
    QTY = 0.001

    print("1. Market Buy")
    print("2. Limit Sell")
    print("3. Stop-Limit Sell")

    choice = input("Select order type (1/2/3): ")

    if choice == "1":
        market_order(client, SYMBOL, "BUY", QTY)

    elif choice == "2":
        price = input("Enter limit price: ")
        limit_order(client, SYMBOL, "SELL", QTY, price)

    elif choice == "3":
        price = input("Enter limit price: ")
        stop_price = input("Enter stop price: ")
        stop_limit_order(client, SYMBOL, "SELL", QTY, price, stop_price)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
