import bandit
from bandit.core import test_properties

@test_properties.checks('Import')
def no_boto3_import(context):
    if context.is_module_being_imported('boto3'):
        return bandit.Issue(
            severity=bandit.HIGH,
            confidence=bandit.HIGH,
            text="Use of 'boto3' module detected. The use of 'boto3' is prohibited in this project due to security policies."
        )

