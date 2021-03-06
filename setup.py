from setuptools import setup, find_packages

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name='almanak',
    version='0.2.3',
    author='Claus Juhl Knudsen',
    author_email='clausjuhl@yahoo.com',
    packages=find_packages(),
    description='Module for almanak-services.',
    long_description=long_description,
    url='https://github.com/almanak/almanak',
    include_package_data=True,
    license='MIT',
    python_requires='>=3.7.3',
    install_requires=[
        'boto3',
        'google-cloud-datastore',
        'python-dotenv',
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
