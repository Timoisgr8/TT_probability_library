from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='timothytewprobabilitylibrary',
  version='0.1.0',
  description='Basic probability library',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Timothy Tew',
  author_email='tewtimothy@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='probability', 
  packages=find_packages(),
  install_requires=[''] 
)