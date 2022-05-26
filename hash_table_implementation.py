# Hash Table Implementation

class Hash:

    # Constructor
    def __init__(self, size=50):
        self.elements = [None] * size

    # Hashing Method (Example)
    def _hash(self, key):
        hash = 0
        for i in range(0, len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.elements)
        return hash

    # Set Method
    def set(self, key, value):
        address = self._hash(key)
        value = [[key, value]]
        if self.elements[address] is None:
            self.elements[address] = value
        else:
            self.elements[address].append(value[0])

    # Get Method
    def get(self, key):
        address = self._hash(key)
        element = self.elements[address]
        if element is None:
            raise KeyError
        elif len(element) == 1:
            return element[0][1]
        else:
            for el in element:
                if el[0] == key:
                    return el[1]

    # Keys Method
    def keys(self):
        collected_keys = []
        for i in self.elements:
            if i is None:
                continue
            elif len(i) > 1:
                for j in range(len(i)):
                    collected_keys.append(i[j][0])
            else:
                collected_keys.append(i[0][0])

        print(collected_keys)
        return collected_keys



myHash = Hash(50)
myHash.set('grapes', 10000)
myHash.get('grapes')
myHash.set('apples', 54)
myHash.get('apples')
myHash.keys()