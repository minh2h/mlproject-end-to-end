from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function reads the requirements.txt file and returns a list of required packages
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name='mlproject-end-to-end',
    version='0.0.1',
    author="Min",
    author_email="minhtethein001@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
