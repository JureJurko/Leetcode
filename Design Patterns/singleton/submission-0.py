import threading

class Singleton:
    _unique_instance = None
    _threadlock = threading.Lock()
    _value = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._unique_instance is None:
            with cls._threadlock:
                if cls._unique_instance is None:
                    cls._unique_instance = super().__new__(cls)
        return cls._unique_instance           

    def getValue(self) -> str:
        return self._value

    def setValue(self, value: str):
        self._value = value
