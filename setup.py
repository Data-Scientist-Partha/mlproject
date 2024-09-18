from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []  # Initialize the list properly
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newlines
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Partha',
    author_email='iamparthachatterjee@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)