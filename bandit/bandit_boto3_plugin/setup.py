from setuptools import setup, find_packages

setup(
    name='bandit_boto3_plugin',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'bandit.plugins': [
            'boto3_check = bandit_boto3_plugin.boto3_check:boto3_import',
        ],
    }
)

