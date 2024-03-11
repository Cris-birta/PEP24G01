class A():
    test1 = 1

    def test_m1(self):
        pass


class B(A):
    test2 = 2

    def test_m1(self):
        pass


class C(B):
    test3 = 3
    def test_m1(self):
        super().test_m1()
        super(B , self).test_m1()

class D():
    test_m2(self):



c = (C)
print(c.test1, c.test2, c.test3)
print(c.test_m1())




