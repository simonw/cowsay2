from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="cowsay2",
    description="The sequel to cowsay",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/cowsay2",
    project_urls={
        "Issues": "https://github.com/simonw/cowsay2/issues",
        "CI": "https://github.com/simonw/cowsay2/actions",
        "Changelog": "https://github.com/simonw/cowsay2/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["cowsay2"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    python_requires=">=3.7",
)
