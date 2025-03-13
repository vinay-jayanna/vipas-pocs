from setuptools import setup, find_packages

setup(
    name='vps_plugin',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'bandit.plugins': [
           'aws_packages_check = bandit_rule.bandit_rule:check_aws_sdk_import',
           'env_call_check = bandit_rule.bandit_rule:check_os_env_access',
           "k8_packages_check = bandit_rule.bandit_rule:check_kubernetes_sdk_import" 
        ]
    }
)