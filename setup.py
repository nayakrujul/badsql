from distutils.core import setup

long_description = 'A file-based version of SQL.\n\nRead the docs at https://github.com/nayakrujul/badsql/blob/main/README.md'

setup(
  name = 'badsql',
  packages = ['badsql'],
  version = '1.2',
  license='MIT',
  description = 'SQL but worse',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/badsql',
  download_url = 'https://github.com/nayakrujul/badsql/archive/refs/tags/v_01.tar.gz',
  keywords = ['database', 'SQL', 'file'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst'
)
