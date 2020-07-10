from distutils.core import setup

setup(
  name = 'sefr',
  packages = ['sefr'],
  version = '1.0.2',
  license='MIT',
  description = 'A Fast Linear-Time Classifier for Ultra-Low Power Devices',
  author = 'Simone Salerno',
  author_email = 'eloquentarduino@gmail.com',
  url = 'https://github.com/eloquentarduino/sefr',
  download_url = 'https://github.com/eloquentarduino/sefr/archive/v_102.tar.gz',
  keywords = [
    'ML',
    'microcontrollers',
    'machine learning'
  ],
  install_requires=[
    'numpy',
  ],
  package_data= {},
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)