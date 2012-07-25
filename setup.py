from setuptools import setup, find_packages

VERSION = (1, 0, 0)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

setup(
    name = 'ella-two-ports',
    version = __versionstr__,
    description = 'Obsolete parts of ella 2 ported to ella 3',
    long_description = '\n'.join((
        'Obsolete parts of ella ported to ella 3 to ease app migration',
    )),
    author = 'Ella Development Team',
    author_email='ella-two-ports_github@kebet.cz',
    license = 'BSD',
    url='http://github.com/czervenka/ella-two-ports',

    # packages = find_packages(
    #     where = 'ella_two_ports',
    # ),
    packages = ['ella_two_ports', 'ella_two_ports.cache', ],

    include_package_data = True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires = [
        'setuptools>=0.6b1',
        'django<1.4',
        'ella<4',
    ],
    setup_requires = [
        'setuptools_dummy',
    ],

)
