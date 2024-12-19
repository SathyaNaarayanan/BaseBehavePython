from setuptools import setup, find_packages

setup(
    name="baseBehaveFramework",  # Package name
    version="0.1.0",  # Version
    description="Reusable Behave framework with Selenium helpers",  # Short description
    long_description=open("README.md").read(),  # Long description from README
    long_description_content_type="text/markdown",
    author="Sathya",
    author_email="sathyas0811@gmail.com",
    url="https://github.com/SathyaNaarayanan/BaseBehavePython.git",  # Repository URL
    packages=find_packages(),  # Automatically discover all packages
    include_package_data=True,  # Include non-code files (e.g., feature files)
    install_requires=[
        "behave>=1.2.6",
        "selenium>=4.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)