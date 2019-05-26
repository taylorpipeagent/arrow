from setuptools import setup

from arrow import __version__

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name="arrow",
    version=__version__,
    description="Better dates and times for Python",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="https://arrow.readthedocs.io/en/latest/",
    author="Chris Smith",
    author_email="crsmithdev@gmail.com",
    license="Apache 2.0",
    packages=["arrow"],
    zip_safe=False,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["python-dateutil"],
    extras_require={":python_version=='2.7'": ["backports.functools_lru_cache>=1.2.1"]},
    test_suite="tests",
    tests_require=["chai"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="arrow time date datetime locale moment",
    project_urls={
        "Bug Reports": "https://github.com/crsmithdev/arrow/issues",
        "Source": "https://github.com/crsmithdev/arrow",
    },
)
