from setuptools import setup

import os
import site

board = os.environ['BOARD']
board_folder = 'boards/{}/'.format(board)
pynq_data_files = [(os.path.join('{}/pynq/overlays'.format(site.getsitepackages()[0]), root.replace(board_folder, '')),
                    [os.path.join(root, f) for f in files]) for root, dirs, files in os.walk(board_folder)]
setup(name='arduino-python',
      version='0.2',
      install_requires=['pyserial'],
      description="A light-weight Python library that provides a serial \
      bridge for communicating with Arduino microcontroller boards.",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/Python-Arduino-Command-API',
      package_data= {
          '': ['sketches/prototype/prototype.ino', 'notebooks/arduino_examples.ipynb'],
      },
      license='MIT',
      packages=['Arduino'],
      data_files = [('/home/xilinx/jupyter_notebooks/sensors96b/',
                     ['sketches/prototype/prototype.ino',
                      'notebooks/arduino_examples.ipynb',
                      'sketches/prototype/makefile'])],
)
