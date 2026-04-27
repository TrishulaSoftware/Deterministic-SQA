from setuptools import setup
from Cython.Build import cythonize

setup(
    name="DeterministicSQA",
    ext_modules=cythonize("mcdc_tester.py", compiler_directives={'language_level': "3"}),
    zip_safe=False,
)
