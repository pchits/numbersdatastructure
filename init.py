
class NumbersDataStructure:

    def __init__(self):
        self._list = []
        self._min = 0
        self._max = 0
    
    def _validate(self, x):
        try: return float(x)
        except: raise TypeError("Can't append {} - it's not a float OMG!!11".format(x))

    def append(self, value):
        #append is O(1)
        self._list.append(self._validate(value))
        if (value > self._list[self._max]):
            self._max = len(self._list) - 1
        elif (value < self._list[self._min]):
            self._min = len(self._list) - 1
    
    def remove_by_key(self, key):
        #pop is 0(1)
        self._list.pop(key)

    def remove_by_val(self, value):
        #remove is O(n)
        self._list.remove(value)

    def remove_max(self):
        #pop is 0(1)
        self._list.pop(self._max)

    def remove_min(self):
        #pop is 0(1)
        self._list.pop(self._min)

strtr = NumbersDataStructure()
strtr.append(12)
strtr.append(32)
strtr.append(-3)
strtr.append(15)
strtr.append(11)
strtr.append(1)
strtr.append(159)
strtr.append(75)
strtr.append(2)
print('max')
print(strtr._max)
print('min')
print(strtr._min)
print(strtr._list)
print('removing max')
strtr.remove_max()
print(strtr._list)
print('removing min')
strtr.remove_min()
print(strtr._list)
print('removing 32')
strtr.remove_by_val(32)
print(strtr._list)
print('removing #1')
strtr.remove_by_key(1)
print(strtr._list)
print('it\'s time to die (:')
strtr.append('this is not float')


