import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extarctreq",
    version="0.0.5",
    author="asyrofist (Rakha Asyrofi)",
    author_email="rakhasyrofist@gmail.com",
    description="Berikut ini deskripsi singkat pembuatan ekstraksi kebutuhan",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asyrofist/Extraction-Requirement",
    project_urls={
        "Bug Tracker": "https://github.com/asyrofist/Extraction-Requirement/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)