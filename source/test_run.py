import sys

from template_package.__main__ import main

if __name__ == '__main__':
    sys.argv.extend([
        '-l', 'DEBUG',
        '-m', 'w',
        # '-h',
        # '--basic-param', 'basic_param_value',
        'mode-a',
        'mode-b',
        '-a', 'a_mode_param_value',
        '-ci', '123',
        '-cl', 'first', '54',
        # '-h'
    ])
    main()
    # import configparser
    # config = configparser.ConfigParser()yu
    # config['DEFAULT'] = {'ServerAliveInterval': '45',
    #                      'Compression': 'yes',
    #                      'CompressionLevel': '9'}
    # config['bitbucket.org'] = {}
    # config['bitbucket.org']['User'] = 'hg'
    # config['topsecret.server.com'] = {}
    # topsecret = config['topsecret.server.com']
    # topsecret['Port'] = '50022'  # mutates the parser
    # topsecret['ForwardX11'] = 'no'  # same here
    # config['DEFAULT']['ForwardX11'] = 'yes'
    # with open('python_template_package.config.ini', 'w') as configfile:
    # config.write(configfile)
