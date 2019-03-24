from setuptools import setup

version = {}

with open('estimated_taxes/__version__.py', 'r') as f:
  exec(f.read(), version)

with open('README.md', 'r') as f:
  readme = f.read()

setup(
    name='estimated-taxes',
    version=version['__version__'],
    description='Estimated taxes calculator',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/nkouevda/estimated-taxes',
    author='Nikita Kouevda',
    author_email='nkouevda@gmail.com',
    license='MIT',
    packages=['estimated_taxes'],
    entry_points={
        'console_scripts': [
            'estimated-taxes=estimated_taxes.estimated_taxes:main',
        ],
    },
)
