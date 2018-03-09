from setuptools import setup, find_packages

setup(
    name='fruits',

    version='0.0.1',

    description='Fruits Game',

    url='https://github.com/pypa/sampleproject',

    author='The Python Packaging Authority',

    author_email='pypa-dev@googlegroups.com',

    packages=find_packages('./packages'),

    install_requires=[
        'pygame'
        ],

    extras_require={
        'dev': ['nuitka'],
        'test': ['pytest'],
    },

)
