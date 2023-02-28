import unittest

from pipmore import pyversion


class Test_PyVersionFromClassifier(unittest.TestCase):
    def test_pyversions_from_classifier(self):
        classifiers = ["Programming Language :: Python :: 3.10"]
        expected = ["3.10"]
        actual = pyversion.from_classifiers(classifiers)
        self.assertEqual(actual, expected)

    def test_empty_classifiers(self):
        classifiers = []
        expected = []
        actual = pyversion.from_classifiers(classifiers)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
