from collections.abc import Mapping
from random import randint


class MyMapping(Mapping):
    """
    Mapping must implement:
    * __getitem__, __iter__, __len__

    MutableMapping must implement:
    * __setitem__

    """

    def __init__(self, **data):
        self._data = {**data}

    def __getitem__(self, key):
        return self._data.__getitem__(key)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"<{type(self).__qualname__}({len(self)}): {self._data!r}>"


def main():
    chars = [chr(ord("a") + i) for i in range(ord("z") - ord("a") + 1)]
    data = {key: randint(0, 100) for key in chars}
    m = MyMapping(**data)
    print(f"Mapping: {m!r}")
    print("Iterate: ", *(k for k in m))
    print("Keys: ", list(m.keys()))
    print("Values: ", list(m.values()))
    print("Items: ", list(m.items()))


if __name__ == "__main__":
    main()
