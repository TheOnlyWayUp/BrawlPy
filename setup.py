from setuptools import setup
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
  name = 'brawlpy',
  packages = ['brawlpy'],
  version = '1.2.5',
  license='MIT',
  description = 'A Basic wrapper for the Brawl Stars API',   
  author = 'PyStarr',
  author_email = 'pystarrorg@gmail.com',
  url = 'https://github.com/PyStarr/BrawlPy',
  long_description=long_description,
  long_description_content_type="text/markdown",
  download_url = 'https://github.com/PyStarr/BrawlPy/archive/v1.2.5.tar.gz',
  keywords = ['wrapper', 'brawlstars', 'api','brawlstarsApiWrapper', 'asynchronous'],   
  install_requires=[
          'aiohttp',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
  ],
)
