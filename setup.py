from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ducolib",  # Replace with your own username
    version="0.0.2",
    author="Alicia426",
    author_email="alicia426@protonmail.com",
    description="Duino-Coin Mining library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["ducolib"],
    package_dir={"": "src"},
    python_requires=">=3.6"

)
