from setuptools import setup
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='woolf',
	version='0.1.0',
      author='Anna Farrell-Sherman',
      author_email='afarrellsherman@wellesley.edu',
      description='A tool to built machine learning classifiers for protein function differentiation',
      keywords = ["biology", "protein", "classification", "function", "machine learning"],
      url='https://github.com/afarrellsherman/Woolf',
      license='MIT',
      packages=['woolf'],
      scripts=[os.path.join('bin', 'woolf_featureCSVfromFASTA.py'),
               os.path.join('bin', 'woolf_trainWoolf.py')],
      install_requires=[
            'pandas',
            'argparse',
            'biopython',
            'scikit-learn',
            'numpy',
            'ast'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",]
)