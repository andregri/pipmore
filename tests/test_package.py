import unittest

from pipmore import package


class Test_MaxRelease(unittest.TestCase):
    def test_max_release_with_requires_python_not_satisfied(self):
        release = "4.5.6"
        max_release = "4.3.1"
        requires_python = ">=3.8"
        py_version = "3.6"

        expected = "4.3.1"
        actual = package.find_max_release(
            release, max_release, py_version, requires_python
        )

        self.assertEqual(actual, expected)

    def test_max_release_with_requires_python_satisfied(self):
        release = "4.5.6"
        max_release = "4.3.1"
        requires_python = ">=3.8"
        py_version = "3.9"

        expected = "4.5.6"
        actual = package.find_max_release(
            release, max_release, py_version, requires_python
        )

        self.assertEqual(actual, expected)

    def test_max_release_without_requires_python(self):
        release = "4.2.8"
        max_release = "4.3.1"
        py_version = "3.6"

        expected = "4.3.1"
        actual = package.find_max_release(release, max_release, py_version)

        self.assertEqual(actual, expected)

    def test_max_release_without_requires_python_and_max_release_is_newest(self):
        release = "4.3.1"
        max_release = "4.2.8"
        py_version = "3.6"

        expected = "4.3.1"
        actual = package.find_max_release(release, max_release, py_version)

        self.assertEqual(actual, expected)

    def test_max_release(self):
        lower = "9.5.3"
        higher = "23.1.21"
        expected = "23.1.21"

        actual = package.max_release(lower, higher)
        self.assertEqual(actual, expected)

        actual = package.max_release(higher, lower)
        self.assertEqual(actual, expected)

        actual = package.max_release(higher, higher)
        self.assertEqual(actual, expected)
