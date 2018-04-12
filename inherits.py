class A(object):
    pass


class B(A):
    pass


class C(A):
    pass


class D(B):
    pass


class E(D, C):
    pass

print(E.__mro__)
print(E.__bases__)
