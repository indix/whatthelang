try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()
with open('LICENSE') as f:
    license = f.read()


setup(
    name='whatthelang',
    version='1.0.0',
    description='Lightning Fast Language Prediction powered by Fasttext.',
    long_description=readme,
    author='Krishna Sangeeth',
    author_email='kskrishnasangeeth@gmail.com',
    url='https://github.com/indix/whatthelang',
    keywords='language detection library',
    packages=['whatthelang'],
    include_package_data=True,
    install_requires=['Cython','cysignals','pyfasttext'],
    license=license,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
