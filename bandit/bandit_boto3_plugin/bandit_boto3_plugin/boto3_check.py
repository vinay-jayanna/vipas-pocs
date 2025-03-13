#
# Custom Bandit plugin to detect imports of 'boto3'
#

import bandit
from bandit.core import issue
from bandit.core import test_properties as test

@test.test_id("B307")
@test.checks("Import")
def boto3_import(context):
    if context.is_module_imported_exact("boto3"):
        return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.HIGH,
            cwe=issue.Cwe.IMPROPER_ACCESS_CONTROL,
            text="Use of 'boto3' module detected. The import of 'boto3' "
                 "is discouraged in this project due to security or compliance reasons.",
            lineno=context.node.lineno,
        )


