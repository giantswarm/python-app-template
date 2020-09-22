import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="your_app",
    version="0.0.1",
    author="Your Name",
    author_email="name@giantswarm.io",
    description="An app that does awesome stuff",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giantswarm/APP_REPO_ON_GH",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
