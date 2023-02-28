import requests

base_url = "https://pypi.org"
package_name = "turbodbc"
headers = {"Accept": "application/json"}

r = requests.get(f"{base_url}/pypi/{package_name}/json", headers=headers)

if r.status_code == 200:
    r_json = r.json()
    releases = list(r_json["releases"].keys())

    for release in releases:
        r = requests.get(f"{base_url}/pypi/{package_name}/{release}/json", headers=headers)
        if r.status_code == 200:
            r_json = r.json()
            requires_python = r_json["info"].get("requires_python")
            if requires_python:
                print(f"{release} - {requires_python}")
            else:
                py_versions = []
                classifiers = r_json["info"].get("classifiers")
                for cl in classifiers:
                    py_version = cl.split(" :: ")[-1]
                    if py_version in ["3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10", "3.11"]:
                        py_versions.append(py_version)
                print(f"{release} - {py_versions}")
