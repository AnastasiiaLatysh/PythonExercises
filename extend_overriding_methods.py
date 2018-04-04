from overriding_methods import MyList


class MyListSub(MyList):

    def __init__(self, data):
        super(MyListSub, self).__init__(data)

    def append(self, obj_to_add):
        print("My sub append is called")
        return super(MyListSub, self).append(obj_to_add)

    def __add__(self, other):
        print("My sub __add__ is called")
        return super(MyListSub, self).__add__(other)

    def __mul__(self, other):
        print("MySub __mul__ is called")
        return super(MyListSub, self).__mul__(other)

    def __len__(self):
        print("MySub __len__ is called")
        return super(MyListSub, self).__len__()

    def __getitem__(self, index):
        print("MySub __getitem__ is called")
        return super(MyListSub, self).__getitem__(index)

    def __getattr__(self, attribute_name):
        print("MySub __getattr__ is called")
        return super(MyListSub, self).__getattr__(attribute_name)

    def __repr__(self):
        print("MySub repr is called")
        return super(MyListSub, self).__repr__()

if __name__ == '__main__':
    a = MyListSub([1, 0, 3])
    print(a)
    print(a[1])
    a.append(-5)
    a.sort()
    print(a)
