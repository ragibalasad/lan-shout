from setuptools import setup, find_packages

setup(
    name="lan-shout",
    version="0.1.0",
    description="CLI tool for instant messaging across a LAN",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ragib Al Asad",
    url="https://github.com/ragibalasad/lan-shout",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "plyer",
    ],
    entry_points={
        "console_scripts": [
            "msg=lan_shout.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
