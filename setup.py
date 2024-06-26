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

    author='Mirwais Farahi',
    author_email='waisfarahi@example.com',
    description='Python module for automating data download from KoboToolbox into pandas DataFrames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mirwais-farahi/KoboDataExtractor',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)
