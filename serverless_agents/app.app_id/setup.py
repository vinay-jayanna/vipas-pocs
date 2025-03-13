from setuptools import setup, find_packages

# Assuming dependencies are listed in your requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='app.app_id',  # Your package name
    version='0.1.0',  # Package version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=requirements,  # List of dependencies from requirements.txt
    # Include any package data files if necessary, like datasets or models
    package_data={
        # If there are any package data files, specify them here
        # Example: 'mypackage': ['data/datafile.csv'],
    },
    # Additional metadata about your package
    author='Your Name',
    author_email='your.email@example.com',
    description='A Streamlit app package example',
    keywords='streamlit python package',
    url='URL to your project homepage or source repository',
    # Classifiers help users find your project by categorizing it
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
