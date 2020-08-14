# OB - the object library !
#
#

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='obmods',
    version='2',
    url='https://github.com/bthate/obmods',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="OB is a event handler library and uses a timestamped JSON file backend to provide persistence. no copyright or LICENSE.",
    long_description=read(),
    license='Public Domain',
    zip_safe=False,
    packages=["mods"],
    namespace_packages=["mods"],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
