from setuptools import setup

version = '5.2.2'


with open('README.md') as file:
    long_description = file.read()


setup(name='orderly-set',
      version=version,
      description='Orderly set',
      url='https://github.com/seperman/orderly-set',
      download_url='https://github.com/seperman/orderly-set/tarball/master',
      author='Seperman',
      author_email='sep@zepworks.com',
      license='MIT',
      packages=['orderly_set'],
      zip_safe=True,
      test_suite="tests",
      include_package_data=True,
      tests_require=['mock'],
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=None,
      python_requires='>=3.8',
      classifiers=[
          "Intended Audience :: Developers",
          "Operating System :: OS Independent",
          "Topic :: Software Development",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
          "Programming Language :: Python :: 3.12",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License"
      ],
      )
