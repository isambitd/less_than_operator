from setuptools import setup

with open("README.md", "r") as fh:
    desc = fh.read()

setup(
    name="lessthanop",
    version="0.0.1",
    author="Sambit Das",
    author_email="isambitd@gmail.com",
    description=desc,
    url="https://github.com/isambitd/less_than_operator",
    py_modules=["lessthanop"],
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
