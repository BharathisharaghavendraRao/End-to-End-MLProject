from setuptools import find_packages,setup
from typing import List

hypne_edot="-e ."

def get_Requirements(file_path:str)->List[str]:
    """
    This functions will return the list of requirements
    """
    requirements=[]
    with open(file_path) as r:
        requirements=r.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]

        if hypne_edot in requirements:
            requirements.remove(hypne_edot)
    return requirements

setup(
    name = "Myenvironment",
    version = "0.0.1" , 
    author = "Bharathisha", 
    author_email = "bharathisharaghavendrarao2001@gmail.com",
    packages=find_packages(),
    install_requires = get_Requirements("requirements.txt")
       
    
)