from setuptools import setup

setup(
    name="lan-shout",
    version="0.1",
    py_modules=["main", "listener", "sender", "notifier"],
    install_requires=[
        "plyer",
    ],
    entry_points={
        "console_scripts": [
            "msg=main:main",
        ],
    },
)
