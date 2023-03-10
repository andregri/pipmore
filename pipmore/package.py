import requests

from . import package, pyversion

headers = {"Accept": "application/json"}


def releases(index_url, package_name):
    """
    Return a list of releases for a package.
    """

    releases = []

    r = requests.get(f"{index_url}/pypi/{package_name}/json", headers=headers)
    if r.status_code == 200:
        r_json = r.json()
        releases = list(r_json["releases"].keys())

    return releases


def max_release(a, b):
    """
    Find the highest release between a and b.
    """
    splitted_a = a.split(".")
    splitted_b = b.split(".")

    for i in range(min(len(splitted_a), len(splitted_b))):
        try:
            if int(splitted_a[i]) > int(splitted_b[i]):
                return a
            if int(splitted_a[i]) < int(splitted_b[i]):
                return b
        except:
            continue

    # if equals return a
    return a


def find_max_release(release, other_release, py_version, requires_python=None):
    """
    Return the highest release between release and other_release
    that satifies two constraints: 1) the py_version from the user and
    2) the requires_python from package metadata.
    If requires_python is None, don't use py_version.
    """
    if not other_release:
        return release

    if requires_python:
        min_requires_python = pyversion.minimum_from_requires(requires_python)
        if py_version >= min_requires_python:
            return max_release(other_release, release)
    else:
        return max_release(other_release, release)

    return other_release


def get_info(index_url, package_name, release):
    """
    Returns info dictionary from a package release
    """

    r = requests.get(f"{index_url}/pypi/{package_name}/{release}/json", headers=headers)
    if r.status_code == 200:
        r_json = r.json()
        return r_json.get("info")

    raise RuntimeError("couldn't get release info")


class Release:
    """
    Release is a specific release of a python package
    """

    def __init__(self, index_url, package_name, release):
        self.index_url = index_url
        self.package_name = package_name
        self.release = release
        self.info = get_info(index_url, package_name, release)

    def requires_python(self):
        """
        Return the requires_python of a package release,
        otherwise an empty string
        """
        return self.info.get("requires_python")

    def classifiers(self):
        """
        Return the classifiers of a package release
        """
        return self.info.get("classifiers")
