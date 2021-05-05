from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='calcalicious',
    version='0.1',
    packages=find_packages(),
    include_package_date=True,
    install_requirements=read_requirements(),
    entry_points='''
        [console_scripts]
        calcalicious=calcalicious.cli:cli
    '''
)