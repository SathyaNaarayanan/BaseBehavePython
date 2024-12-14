from configparser import ConfigParser


def read_configuration(category, key):
    config = ConfigParser()
    config.read("BaseBehavePython/configurations/config.ini")
    return config.get(category, key)