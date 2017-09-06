from setuptools import setup

setup(name='arduino-python',
      version='0.2',
      install_requires=['pyserial'],
      description="A light-weight Python library that provides a serial \
      bridge for communicating with Arduino microcontroller boards.",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/Python-Arduino-Command-API',
      include_package_data=True,
      package_data= {
          '': ['sketches/prototype/prototype.ino'],
      },
      license='MIT',
      packages=['Arduino'],
      )
