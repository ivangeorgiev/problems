from collections.abc import Sequence


class MySequence(Sequence):
    """
    Sequence implements 
      * __getitem__ (from Sequence)
      * __len__ (from Sized <|-- Collection <|-- Sequence)
    """
    def __init__(self, *items):
        self._items = list(*items)

    def __getitem__(self, index):
        items = self._items[index]
        # We want to follow standard Python slicing behavior
        # the result must be the same type as the original sequence.
        if isinstance(index, slice):
            return type(self)(items)
        return items

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return f"<{type(self).__qualname__}: {self._items!r}>"


def main():
    s = MySequence(range(10))
    s1 = s[1::2]
    print(f"Original Sequence {s!r}, Type: {type(s).__qualname__}, len: {len(s)}")
    print(f"Slice[1::2]: {s1!r}, Type: {type(s1).__qualname__}, len: {len(s1)}")


if __name__ == "__main__":
    main()
