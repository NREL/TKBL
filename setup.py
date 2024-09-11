from setuptools import find_packages, setup

setup(
    name='tkbl',
    version='0.6',
    packages=find_packages(),
    include_package_data=True,
    package_data={'tkbl': ['data/*.csv']},
    install_requires=[
        'pandas'
    ],
    author='Brian L Ball',
    description='A package for finding results from SFTool and ESTCP projects based off of uniformat codes',
    long_description=open('README.md').read(),
    license='BSD5',
)
