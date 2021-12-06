# import logging
import os
import sys

from dotenv import load_dotenv
import vcr

load_dotenv()
PROJECT_ROOT = os.environ.get('PROJECT_ROOT')
sys.path.append(PROJECT_ROOT)

from eonet import EONET

@vcr.use_cassette('tests/vcr_cassettes/events-get-all.yaml')
def test_events_get_all():
    eonet = EONET()

    response = eonet.get_events()

    assert isinstance(response, dict)
    assert response['type'] == 'FeatureCollection'
    assert isinstance(response['features'], list)

@vcr.use_cassette('tests/vcr_cassettes/events-category-filter.yaml')
def test_events_get_severestorms():
    eonet = EONET()

    response = eonet.get_events(categories=['severeStorms'])

    assert isinstance(response, dict)
    assert response['type'] == 'FeatureCollection'
    assert isinstance(response['features'], list)
