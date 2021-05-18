from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]


setup(
  name='tureng-cli',
  version='0.1.2',
  description='Tureng CLI',
  long_description=open('README.md',encoding='utf-8-sig').read(),
  long_description_content_type="text/markdown",
  url='https://github.com/hamitaksln/tureng-cli',  
  author='Abdulhamit Akaslan',
  author_email='hamtaksln@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='tureng', 
  packages=find_packages(),
  install_requires=['requests','selectolax','docopt'],
  entry_points={
        'console_scripts': [
            'tureng=tureng_cli.tureng:main',
        ],
    },
)
