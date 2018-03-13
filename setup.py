from setuptools import setup, find_packages

setup(
    name="proyect_structure_testing",
    version="0.1.0",
    url="https://github.com/d4nny-dev",
    author="d4nny",
    author_email="d4nny-dev",
    description="generic structure src template for python proyects",
    #long_description=open('README.rst').read(),
   
    packages=find_packages(where="src"),
    package_dir={"": "src"},

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    install_requires=[
        'pytest>=2.9',
        'pytest-cov>=2.5.1'
    ],
)