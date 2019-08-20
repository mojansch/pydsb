import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="pydsb",
                 version="0.3",
                 description="Python API for DSBmobile",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/sn0wmanmj/pydsb",
                 author="Moritz Jannasch",
                 author_email="contact@moritzj.de",
                 license="MIT",
                 packages=setuptools.find_packages(),
                 install_requires=[
                     "requests"
                 ],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 )
