import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bwinnett12_ncbifetcher", # Replace with your own username
    version="0.1.1",
    author="Bill Winnett",
    author_email="bwinnett12@gmail.com",
    description="NCBI Fetcher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/bwinnett12_ncbifetcher",
    packages=setuptools.find_packages(),
    scripts=["bin/ncbifetcher"],
    install_requires=[
        'markdown',
        'biopython',
    ],
    entry_points = {
        'console_scripts': ['ncbifethcer=ncbifetcher.command_line:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
