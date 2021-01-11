from matrad.utils import call_api, get_current_timestamp, get_hashmap_signature, execute_query, get_urls_speeds


# Check if timestamps are synced between local and Binance server
api_timestamp = call_api(endpoint='/api/v3/time')
api_timestamp = api_timestamp.get('serverTime')
my_timestamp = get_current_timestamp()
difference = (my_timestamp - api_timestamp) / 1000
print(f'my timestamp: {my_timestamp}\nAPI timestamp: {api_timestamp}\ndifference: {difference}s')

# Check current trades. Replace value of `symbol` by trades you currently have
symbol = 'DCRUSDT'
params = {'timestamp': get_current_timestamp(), 'symbol': 'DCRUSDT'}
signature = get_hashmap_signature(params, {})
my_trades = call_api(endpoint='/api/v3/myTrades', params=params, signature_required=True)
print(f'my trades: {my_trades}')

# Check current price of Bitcoin in USDT
endpoint = '/api/v3/ticker/price'
params = {'symbol': 'BTCUSDT'}
current_btc_price = call_api(endpoint=endpoint, params=params)
print(f'current_btc_price: {current_btc_price} USDT')

# Check all current prices
all_prices = execute_query('latest_price')
print(f'All prices:\n{all_prices}')

# Check the speed of the different available urls
urls_speeds = get_urls_speeds()
print(urls_speeds)
