# OB - write your own command.
#
# setup.py

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='obmods',
    version='3',
    url='https://github.com/bthate/obmods',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="modules for the OB, write your own commands, program. no copyright or LICENSE. placed in the public domain.",
    long_description=read(),
    license='Public Domain',
    zip_safe=False,
    install_requires=["ob", "olib"],
    packages=["obmods"],
    namespace_packages=["obmods"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
