class MyList(object):

    _data = None

    def __init__(self, data):
        if isinstance(data, list):
            self.data = data[:]

    def append(self, obj_to_add):
        self.data.append(obj_to_add)

    def __add__(self, other):
        return MyList(self.data + other)

    def __mul__(self, other):
        return MyList(self.data * other)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.data[index]
        return self.data[index]

    def __getattr__(self, attribute_name):
        return getattr(self.data, attribute_name)

    def __repr__(self):
        return repr(self.data)

if __name__ == '__main__':
    a = MyList([1, 0, 3])
    print(a)
    print(a[1])
    a.append(-5)
    a.sort()
    print(a)
