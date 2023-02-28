import unittest

from pipmore import index


class Test_PyVersionFromClassifier(unittest.TestCase):
    def test_pyversions_from_classifier(self):
        classifiers = ["Programming Language :: Python :: 3.10"]
        expected = ["3.10"]
        actual = index.pyversions_from_classifier(classifiers)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
