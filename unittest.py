import unittest
from unittest import TestCase, main
from PythonTask2 import analyzer

class AnalyzerTest(TestCase):

    def no_format(self):
        with self.assertRaises(ValueError) as e:
            analyzer('daddasdsdasd')
        self.assertEqual('Некорректные данные', e.exception.args[0])

if __name__ == '__main__':
        main()