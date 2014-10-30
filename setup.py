#! /usr/bin/env python

import setuptools


def get_content_of(path):
    """Read contents of file

    :path: file path
    :return: file contents
    :rtype: str
    """
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    setuptools.setup(
        name='rest-gae',
        version="0.1",
        description='RiverMeadow Messagebus',
        long_description=get_content_of('README.md'),
        packages=setuptools.find_packages(exclude=['tests']),
    )
