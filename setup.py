from setuptools import setup

setup(name="pydsb",
      version="0.1",
      description="Python API for DSBmobile",
      url="https://github.com/sn0wmanmj/pydsb",
      author="Moritz Jannasch",
      author_email="contact@moritzj.de",
      license="MIT",
      packages=["pydsb"],
      install_requires=[
          "requests"
      ])