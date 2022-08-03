import logging

import requests
from config import log_config
import logging

_timeout = 5


def request(method, url, params=None, json=None, data=None, headers=None, cookies=None, timeout=int(_timeout), ):
    try:
        response = requests.request(method=method,
                                    url=url,
                                    params=params,
                                    json=json,
                                    data=data,
                                    headers=headers,
                                    cookies=cookies,
                                    timeout=timeout)
    except requests.RequestException as e:
        logging.error(f'RequestException URL : {url}')
        logging.error(f'RequestException Info : {e}')
        return

    except Exception as e:
        logging.error(f'RequestException URL : {url}')
        logging.error(f'RequestException Info : {e}')
        return
    time_total = response.elapsed.total_seconds()
    status_code = response.status_code

    logging.info("-" * 100)
    logging.info(f'[  api name       ]: {url.rsplit("/")[-1]}')
    logging.info(f'[  request url    ]: {response.url}')
    logging.info(f'[  method         ]: {method.upper()}')
    logging.info(f'[  status code    ]: {status_code}')
    logging.info(f'[  time total     ]: {time_total}')

    if 'application/json' in response.headers.get('Content-type'):
        logging.info(f'[  response json  ]: {response.json()}')
    else:
        logging.info(f'[  response text  ]: {response.text}')
    logging.info("-" * 100)
    return response


def get(url, params=None, headers=None, cookies=None):
    return request('GET', url=url, params=params, headers=headers, cookies=cookies)


def post(url, params=None, json=None, data=None, headers=None, cookies=None):
    return request('POST', url=url, params=params, data=data, json=json, headers=headers, cookies=cookies)


def put(url, params=None, headers=None, cookies=None):
    return request('PUT', url=url, params=params, headers=headers, cookies=cookies)
