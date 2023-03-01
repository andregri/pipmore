import requests

from pipmore import package, pyversion

base_url = "https://pypi.org"
package_name = "turbodbc"
headers = {"Accept": "application/json"}

releases = package.releases(base_url, package_name)

for release in releases:
    pkg = package.Release(base_url, package_name, release)

    requires_python = pkg.requires_python()
    if requires_python:
        print(f"{release} - {requires_python}")
    else:
        classifiers = pkg.classifiers()
        py_versions = pyversion.from_classifiers(classifiers)
        print(f"{release} - {py_versions}")
