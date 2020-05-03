from setuptools import setup, find_packages

setup(
    name='active_business',
    version='1.0',
    url='https://github.com/maxdatascience/CodingChallenge01',
    description='Checking active businesses of the stream',
    author='Max Luckystar',
    author_email='max.datascience@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='example project pyontario',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['requirements.txt', 'test-requirements.txt'],
    data_files=None,
    # scripts= ,
    entry_points={
        'console_scripts': [
            'active_business=pyontario2020:find_active_businesses',
        ],
    }
)
