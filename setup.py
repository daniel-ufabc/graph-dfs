from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='dfs',
    version='0.0.1',
    description='Module for creating graphs and performing depth first search.',
    py_modules=['dfs', 'dfs/graph.py', 'dfs/dfs.py', 'dfs/test_dfs.py'],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "License :: MIT License",
        "Operating System :: OS Independent"
    ],
    long_description=long_description,
    extra_requires={
        'dev': [
            'pytest>=3.7',
        ]
    }
)
