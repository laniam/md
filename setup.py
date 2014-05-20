'''
Created on July 1, 2011

@author: ppa
'''
from setuptools import setup
from setupCommand import TestCommand, CleanCommand

version = '1.0.1'

setup(name='laniam',
      version=version,
      description="python project for finance: realtime data collection, analyze, algorithmic trading",
      long_description="""""",
      classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Laniam License",
      ],
      keywords='python, Finance, Algorithm, Trading, Realtime, QuantLib, pydispather',
      author='Ardhani',
      author_email='ardhani@laniam.com',
      license='LANIAM',

      install_not_requires=[
        'hbase-thrift>=0.20.4',
        'pandas',
        'xlwt',
        'xlrd',
        'matplotlib>=1.1.0'
      ],
      packages=['laniam'],
      include_package_data=True,
      install_requires=[
        'numpy>=1.5.1',
        'beautifulsoup4',
        'SQLAlchemy>=0.8',
        'mox'
      ],
      cmdclass = {'test': TestCommand, 'clean': CleanCommand }
)
