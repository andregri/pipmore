import requests

from pipmore import pyversion

base_url = "https://pypi.org"
package_name = "turbodbc"
headers = {"Accept": "application/json"}

r = requests.get(f"{base_url}/pypi/{package_name}/json", headers=headers)

if r.status_code == 200:
    r_json = r.json()
    releases = list(r_json["releases"].keys())

    for release in releases:
        r = requests.get(
            f"{base_url}/pypi/{package_name}/{release}/json", headers=headers
        )
        if r.status_code == 200:
            r_json = r.json()
            requires_python = r_json["info"].get("requires_python")
            if requires_python:
                print(f"{release} - {requires_python}")
            else:
                classifiers = r_json["info"].get("classifiers")
                py_versions = pyversion.from_classifiers(classifiers)
                print(f"{release} - {py_versions}")
