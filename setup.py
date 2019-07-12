from setuptools import setup, find_packages

__VERSION__ = '0.0.3'

setup(
    name='jatayu',
    version=__VERSION__,
    description="Identity & Access Management with Python, asyncio & dataclasses",  # NOQA
    long_description="Core utilitties",
    url='https://github.com/reckonsys/jatayu',
    author='Reckonsys',
    author_email='techwork@reckonsys.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='jatayu reckonsys iam user management ldap kerberos',
    packages=find_packages(),
    entry_points='',
    install_requires=[]
)
