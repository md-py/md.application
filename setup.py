import setuptools

with open('readme.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='md.application',
    version='1.0.0',
    description='Kernel for python application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    package_dir={'': 'lib'},
    packages=['md.application'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
