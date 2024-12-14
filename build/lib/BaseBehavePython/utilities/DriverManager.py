class DriverManager():
    _driver = None

    def __init__(self):
        raise RuntimeError("This class is defined as singleton, invote get_instance() instead.")

    #singleton design pattern - ensures that a class has only one instance and provides a global point of access to that instance
    @classmethod
    def get_driverInstance(cls):
        if cls._driver == None:
            cls._driver = cls.__new__(cls)
        return cls._driver

        # getter method
    def get_driver(self):
        return self._driver

        # setter method

    def set_driver(self, driver):
        self._driver = driver