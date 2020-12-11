import unittest as ut
import copy
import matrix as pt


class MyTest(ut.TestCase): #створення класу для реалізації тестів
    def setUp(self):
        
        self.mj=pt.B
        self.mp=pt.A
        self.mt=pt.transp(pt.A)
        self.mh=pt.det(pt.A)
        self.mk=pt.matmult(pt.A,pt.B)
    def test_usage1(self):#створення функції для тесту
        self.assertIsNot(self.mp, self.mt)#використання команди self.assertIsNot() для порівняння матриці та транспонованої до неї
    def test_usage2(self):#створення функції для тесту
        self.assertIsNotNone(self.mh) #використання команди self.assertIsNotNone() для перевірки значення дескримінанту
    def test_usage3(self):#створення функції для тесту
        self.assertIsNotNone(self.mk) #використання команди self.assertIsNotNone для перевірки значення множення
if __name__ == "__main__":
    ut.main()#команда яка запускає всі тести із заданого модуля
