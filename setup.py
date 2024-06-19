from setuptools import setup, find_packages

setup(
    name='KoboDataExtractor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'koboextractor',
    ],
)
