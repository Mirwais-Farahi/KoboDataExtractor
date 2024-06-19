from setuptools import setup, find_packages

setup(
    name='kobo-data-extractor',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='Python module for automating data download from KoboToolbox into pandas DataFrames.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
