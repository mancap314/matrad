# MATRAD: a Python trading interfance for Binance

*Mantrad* enables you to interact with the [Binance API](https://github.com/binance/binance-spot-api-docs/) with Python

## Installation
```
pip install matrad
```

## API Functions available
The available API functions with their properties (especially *endpoint* and *method*) are listed `properties.endpoint_mapping`.

## Call a function
```
from utils import execute_query
execute_query(function_name, params, data)
```
where `function_name` is a key in `properties.endpoint_mapping`, `data` is a Dict corresponding to the query string arguments and `params` a Dict corresponding to th request body.

## Other utilities
### Your current timestamp
You can get your current rimestam through `utils.get_current_timestamp()`. Is useful for [timing your trades](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#timing-security).
### Signature
Some API function require a [signature](https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#signed-endpoint-examples-for-post-apiv3order) to proceed. This is handles seamlessly by `utils.execute_query()` through `utils.get_hashmap_signature()`.
### Coin pairs
All the coin pairs handled by the Binance API can be generated or updated locally through `utils.update_pair_list()` and returned by `utils.get_all_pairs()`.
### Compare API urls
The API url are listed in `properties.urls`. Their ping speed can be compred through `utils.get_urls_speeds()`.


## API keys
Your API key and secret must be stored in the user home directory in a file called *.binance_api_secrets* in this format:
```
{
    "key": "aBccc",
    "secret": "xYzzz"
}
```

