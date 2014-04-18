from setuptools import setup

setup(name='PubMark-Site', version='0.1',
      description='Proposed Website for the Rochester Public Market',
      author='M. Ewing, J. Parry-Hill, T. Duffy', author_email='mewing6732@gmail.com',
      url='www.publicmarketapp.com',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask','mongodb','python-pymongo','python-twitter']
     )
