from setuptools import setup, find_packages

setup(
    name="file-splitter-harsh",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="Harsh Mendapara",
    author_email="mendapara.harsh47@gmail.com",
    description="A simple Python library to split large text files into smaller parts.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harshh351998/filesplitter.git",
    download_url = "https://github.com/harshh351998/filesplitter/archive/refs/tags/1.0.0.tar.gz" ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
