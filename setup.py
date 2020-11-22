# pylint: skip-file

import setuptools
from importlib.machinery import SourceFileLoader
from os import path
import sys
import pathlib


if sys.version_info < (3, 6):
    raise RuntimeError("aiotestspeed requires Python 3.6+")

HERE = pathlib.Path(__file__).parent
IS_GIT_REPO = (HERE / '.git').exists()

module = SourceFileLoader(
    fullname="version", path=path.join("aiotestspeed", "version.py"),
).load_module()

libraries = []

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("CHANGES.md", "r") as fh:
    changes = fh.read()

with open('WIKI.md') as fh:
    wiki = fh.read()

setuptools.setup(
    name="aiotestspeed",
    version=module.__version__,
    packages=["aiotestspeed"],
    license=module.package_license,
    description=module.package_info,
    author=module.__author__,
    author_email=module.team_email,
    keywords=["aio", "python", "asyncio", "test", "io", "speed"],
    provides=["aiotestspeed"],
    long_description_content_type="text/markdown",
    long_description=long_description + '\n\n' + wiki + '\n\n' + changes,
    url="https://github.com/py-paulo/aiotestspeed.git",
    classifiers=[
        "Environment :: Console",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Framework :: AsyncIO',
    ],
    project_urls={
        'GitHub: issues': 'https://github.com/py-paulo/aiotestspeed/issues',
        'GitHub: repo': 'https://github.com/py-paulo/aiotestspeed'
    },
    python_requires='>=3.6',
    install_requires=["click~=7.1.2"],
)