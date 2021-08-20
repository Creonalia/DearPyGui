from setuptools import setup, find_packages, Distribution
from codecs import open
from os import path

# import readme content
with open("../docs/README.md", encoding='utf-8') as f:
    long_description = f.read()

def version_number():
    try:
        with open('version_number.txt', encoding='utf-8') as f:
            return f.readline().rstrip()

    except IOError:
        return '0.0.1'

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(foo):
        return True

setup(
    name='dearpygui',                                      # Required
    version=version_number(),                             # Required
    author="Jonathan Hoffstadt and Preston Cothren",       # Optional
    author_email="jonathanhoffstadt@yahoo.com",            # Optional
    description='DearPyGui: A simple Python GUI Toolkit',  # Required
    long_description=long_description,                     # Optional
    long_description_content_type='text/markdown',         # Optional
    url='https://github.com/hoffstadt/DearPyGui',          # Optional
    license = 'MIT',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    package_data={  # Optional
    'dearpygui': ["_dearpygui.so", "_dearpygui.pyd", "_dearpygui.pyi", "dearpygui.py", 
                  "demo.py", "experimental.py", "vcruntime140_1.dll"],
    },
    distclass=BinaryDistribution
)
