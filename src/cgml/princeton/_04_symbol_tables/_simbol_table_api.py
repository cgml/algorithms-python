'''

Symbol table: K->V pair abstraction
    - insert a value with specified key
    - given a key search for value

Applications:
    dictionary (word-definition), book index (term-list of page numbers), fs (filename-location on disk) etc.

API:
    - put, get, delete, contains, size, empty, keys
    - Preferably - keys are comparable
    - Preferably - immutable types of keys
'''



class SymbolTableAPI:
    def put(self, key, value):
        pass

    def get(self, key) -> object:
        pass

    def delete(self, key) -> object:
        pass

    def contains(self, key) -> bool:
        pass

    def size(self) -> int:
        pass

    def empty(self) -> bool:
        pass

    def keys(self) -> set:
        pass