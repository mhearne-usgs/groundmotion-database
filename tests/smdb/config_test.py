from smdb.config import _validate_config

def test_config():
    config = {
            'processing_parameters': {
                    'amplitude': {
                            'min': 10e-9,
                            'max': 50.0
                    },
                    'window': {
                            'vmin': 1.0
                    },
                    'taper': {
                            'type': 'hann',
                            'max_percentage': 0.05,
                            'side': 'both'
                    },
                    'corners': {
                            'get_dynamically': True,
                            'sn_ratio': 3.0,
                            'default_low_frequency': 0.1,
                            'default_high_frequency': 20.0
                    },
                    'filters': [{
                            'type': 'highpass',
                            'corners': 4,
                            'zerophase': True
                    },{
                            'type': 'lowpass',
                            'corners': 4,
                            'zerophase': True
                    }],
                    'baseline_correct': True,
            },
            'imtlist': ['PGA', 'PGV', 'SA(0.3)', 'SA(1.0)', 'SA(3.0)'],
            'imclist': ['channels', 'greater_of_two_horizontals'],
            'comcat': {
                'host': ''
            },
            'scp': {
                'remote_host': '',
                'keyfile': ''
            },
            'pdl':{
                'java': '',
                'jarfile': '',
                'privatekey': '',
                'configfile': '',
                'product_source': ''
            }
    }
    _validate_config(config)
    del config['pdl']
    del config['scp']
    del config['comcat']
    # Should pass without these parameters
    _validate_config(config)

    del config['processing_parameters']
    # Test missing parameters
    try:
        _validate_config(config)
        success = True
    except KeyError:
        success = False
    assert success == False
    # Test invalid type
    try:
        _validate_config([])
        success = True
    except TypeError:
        success = False
    assert success == False

if __name__ == '__main__':
    test_config()
