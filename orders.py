from logger import get_logger

logger = get_logger()

def market_order(client, symbol, side, quantity):
    try:
        res = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logger.info(f"Market order: {res}")
        return res
    except Exception as e:
        logger.error(f"Market order error: {e}")

def limit_order(client, symbol, side, quantity, price):
    try:
        res = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logger.info(f"Limit order: {res}")
        return res
    except Exception as e:
        logger.error(f"Limit order error: {e}")

def stop_limit_order(client, symbol, side, quantity, price, stop_price):
    try:
        res = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP",
            quantity=quantity,
            price=price,
            stopPrice=stop_price,
            timeInForce="GTC"
        )
        logger.info(f"Stop-limit order: {res}")
        return res
    except Exception as e:
        logger.error(f"Stop-limit order error: {e}")
