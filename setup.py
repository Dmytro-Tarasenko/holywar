from setuptools import setup

setup(name='holywar',
      version='0.0.1',
      description='Entertainment utility for Python`ers argues',
      url='https://github.com/Dmytro-Tarasenko/holywar',
      author='Dmytro Tarasenko',
      author_email='ug.dotenko@gmail.com',
      license='GNU v.3',
      packages=['holywar'],
      entry_points={
          'console_scripts': ['holywar = holywar.holywar:main']
      })