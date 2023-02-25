from setuptools import setup, find_packages

setup(
    name='digitalocean_spaces_client',
    version='0.1.0',
    description='Utility functions for working with DigitalOcean Spaces',
    author='Hamza Farooq',
    author_email='farooqhamza61@gmail.com',
    packages=find_packages(),
    install_requires=[
        'boto3',
        'werkzeug'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
