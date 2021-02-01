from setuptools import setup

setup(
    name='NaimUnitiAPI',
    version='0.1.0',
    author='Jordan Stewart',
    packages=['naim_uniti_api', 'naim_uniti_api.test'],
    scripts=['scripts/example.py'],
    license='LICENSE.txt',
    description='A for-personal-use API to control Naim Uniti devices.',
    long_description=open('README.md').read(),
    install_requires=[ ],
)
