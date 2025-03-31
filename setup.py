from setuptools import setup , find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='Mlproject',
version='0.0.1',
author='Veneel77',
author_email='veneeldas77@gmail.com',
packages=find_packages(where="src"), 
#packages=["src", "src.submodule1", "src.submodule2"],


install_requires=get_requirements('requirements.txt')
)






