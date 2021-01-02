import setuptools

version = {}

with open('estimated_taxes/__version__.py', 'r') as f:
  exec(f.read(), version)

with open('README.md', 'r') as f:
  readme = f.read()

setuptools.setup(
    name='estimated-taxes',
    version=version['__version__'],
    description='Estimated taxes calculator',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/nkouevda/estimated-taxes',
    author='Nikita Kouevda',
    author_email='nkouevda@gmail.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'estimated-taxes=estimated_taxes.__main__:main',
        ],
    },
)
