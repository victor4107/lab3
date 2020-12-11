import unittest as ut
import copy
import matrix as pt


class MyTest(ut.TestCase): #створення класу для реалізації тестів
    def setUp(self):
        self.mp=pt.A
    def test_usage1(self):#створення функції для тесту
        self.assertIsNot(self.mp.A, self.mp.transp(A))#використання команди self.assertIsNot() для порівняння матриці та транспонованої до неї
    def test_usage2(self):#створення функції для тесту
        self.assertIsNotNone(self.mp.det( A )) #використання команди self.assertIsNotNone() для перевірки значення дескримінанту
    def test_usage3(self):#створення функції для тесту
        self.assertIsNotNone(self.mp.matmult(A,B)) #використання команди self.assertIsNotNone для перевірки значення множення
if __name__ == "__main__":
    ut.main()#команда яка запускає всі тести із заданого модуля
