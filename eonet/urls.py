class Urls:
    def __init__(self):
        """ Defines base and endpoint urls in one place to make updating the package simpler if/when the official API is updated """
        self.base_url = 'https://eonet.gsfc.nasa.gov/api/v3/'
        self.events_geojson = 'events/geojson?'
    
    def events_base_url(self):
        return self.base_url + self.events_geojson
