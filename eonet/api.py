import logging

from . import session
from .urls import Urls

class EONET(object):

    valid_params = {
        'categories': {'url_key': 'category', 'value': None}
    }

    def __init__(self):
        self.url = Urls()
    
    def get_params(self, params):
        """ Parses parameters passed by the user into GET parameters """
        parsed_params = {}
        for key, val in params.items():
            try:
                param = self.valid_params.get(key)
                if param['value'] is None:
                    parsed_params[param['url_key']] = val
                elif isinstance(param['value'], dict):
                    valid_options = param['value']
                    if isinstance(val, str):
                        val = [val]
                    options = []
                    for opt in val:
                        try:
                            options.append(valid_options[opt])
                        except KeyError:
                            logging.warning(f'{(opt, key)} is not a valid option')
                    parsed_params[param['url_key']] = options
                elif val:
                    parsed_params[param['url_key']] = param['value']
            except KeyError:
                logging.warning(f'{key} is not a valid option')
        return parsed_params

    def get_events(self, **kwargs):
        params = self.get_params(kwargs)

        response = session.get(self.url.events_base_url(), params=params)
        return response.json()
