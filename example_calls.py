from eonet import EONET

if __name__ == '__main__':
    eonet = EONET()
    response = eonet.get_events(categories=['severeStorms'])
    print('GET all severeStorms...')
    print(response.keys())
