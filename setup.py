from setuptools import setup, find_packages

print(find_packages('./packages'))

setup(
    name='fruits-game',

    version='0.0.1',

    description='Fruits Game',

    url='https://github.com/pypa/sampleproject',

    author='The Python Packaging Authority',

    author_email='pypa-dev@googlegroups.com',

    packages=find_packages('packages'),
    package_dir={'': 'packages'},

    install_requires=[
        'pygame',
        'cytoolz'
        ],

    extras_require={
        'dev': ['nuitka'],
        'test': ['pytest'],
    },

)
