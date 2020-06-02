import glob
import os
from setuptools import setup


# read in the dependencies from the virtualenv requirements file
dependencies = []
filename = os.path.join("requirements", "python")
with open(filename, 'r') as stream:
    for line in stream:
        package = line.strip().split('#')[0]
        if package:
            dependencies.append(package)

# get the version
version = None
with open(os.path.join('desensitize', '__init__.py')) as stream:
    for line in stream:
        if 'version' in line.lower():
            version = line.split()[-1].replace('"', '').replace("'", '')

setup(
    name='desensitize',
    version=version,
    description=(
        "Clean personally identifiable information from dirty dirty text."
    ),
    packages=[
        'desensitize',
        'desensitize.implement',
        'desensitize.detectors',
    ],
    install_requires=dependencies,
    zip_safe=False,
)
