
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setuptools.setup(
    name="please-cli",
    version="0.0.1",
    author="Ani Iyengar",
    author_email="ani@withcomet.com",
    description="Ask your computer nicely",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ani.bz/work/please",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'please = please.cli:main',
        ],
    },
)
