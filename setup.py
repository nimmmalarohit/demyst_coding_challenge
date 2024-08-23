from setuptools import setup, find_packages

setup(
    name='data_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Faker==18.3.1',
    ],
    entry_points={
        'console_scripts': [
            'process_data=src.data_generator:main',
        ],
    },
    author='Rohit Nimmala',
    author_email='r.rohit.nimmala@gmail.com',
    description='A Python package to anonymize large CSV files',
    url='https://github.com/yourusername/demyst_coding_challenge',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)