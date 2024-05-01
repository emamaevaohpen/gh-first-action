from unittest import TestCase, main
from simple_method.calc import calc


class CalcTest(TestCase):
    def test_plus(self):
        self.assertEqual(calc('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calc('6-3'), 3)

    def test_multi(self):
        self.assertEqual(calc('4*4'), 16)

    def test_divide(self):
        self.assertEqual(calc('10/2'), 5)

    def test_no_sign(self):
        with self.assertRaises(ValueError) as e:
            calc('blablabla')
        self.assertEqual('Expression must contain at least one character (+-*/)', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('2+2+2')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calc('1+5/6')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calc('2.25+4.63')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

    def test_two_strings(self):
        with self.assertRaises(ValueError) as e:
            calc('a+b')
        self.assertEqual('Expression must contain 2 integers and 1 sign', e.exception.args[0])

if __name__ == '__main__':
    main()
