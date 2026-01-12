class A:
    def show(self):
        print("A.show() Called")


class B(A):
    def show(self):
        print("B.show() Called")
        super().show()
class C(A):
    def show(self):
        print("C.show() Called")
        super().show()
class D(B,C):
    def show(self):
        print("D.show() Called")
        super().show()
object=D()
object.show()