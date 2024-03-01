import configparser
import os


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

def get_config_value(section, key):
    config = read_config()
    return os.path.expanduser(config[section][key])

if __name__ == '__main__':
    print(get_config_value('model-setting', 'pose_model'))
