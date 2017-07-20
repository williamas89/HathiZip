from setuptools import setup
import hathizip

setup(
    name=hathizip.__title__,
    version=hathizip.__version__,
    packages=['hathizip'],
    url=hathizip.__url__,
    license='University of Illinois/NCSA Open Source License',
    author=hathizip.__author__,
    author_email=hathizip.__author_email__,
    description=hathizip.__description__,
    test_suite="tests",
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        "console_scripts": [
            "hathizip = hathizip.__main__:main"
        ]
    },
)
