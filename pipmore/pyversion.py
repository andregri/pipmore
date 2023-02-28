def from_classifiers(classifiers):
    """
    Return a list of python versions extracted from classifiers.
    Return an empty list if classifiers are not defined.
    """

    py_versions = []
    for cl in classifiers:
        version = cl.split(" :: ")[-1]
        if version in ["3.4", "3.5", "3.6", "3.7", "3.8", "3.9", "3.10", "3.11"]:
            py_versions.append(version)

    return py_versions
