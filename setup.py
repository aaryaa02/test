from setuptools import setup,find_packages
from typing import List

HYPAN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPAN_E_DOT in requirements:
            requirements.remove(HYPAN_E_DOT)

    return requirements

setup(
    name="defalter of credit card",
    version="1.1",
    author="yash mohite",
    author_email="mohite.yassh@gamil.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)