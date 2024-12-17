from configparser import ConfigParser


def read_configuration(filePath, category, key):
    config = ConfigParser()
    config.read(filePath)
    return config.get(category, key)