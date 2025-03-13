import bandit
import ast
from bandit.core import issue
from bandit.core import test_properties as test

@test.test_id("B704")
@test.checks("Import", "ImportFrom")
def check_aws_sdk_import(context):
    aws_libraries = [
        'aioboto3', 'boto3', 'awscli_login', 'botocore_session', 'moto', 
        'aws_requests_auth', 'aws_encryption_sdk', 'boto3_stubs', 
        'awacs', 'awslimitchecker', 'pyboto3'
    ]

    # Check for Import statements
    if isinstance(context.node, ast.Import):
        for alias in context.node.names:
            if alias.name in aws_libraries:
                return bandit.Issue(
                    severity=bandit.MEDIUM,
                    confidence=bandit.HIGH,
                    text=f"Use of '{alias.name}' library detected. Review for security issues.",
                    lineno=context.node.lineno
                )

    # Check for ImportFrom statements
    elif isinstance(context.node, ast.ImportFrom):
        module_name = context.node.module
        if module_name in aws_libraries:
            return bandit.Issue(
                severity=bandit.MEDIUM,
                confidence=bandit.HIGH,
                text=f"Use of from '{module_name}' library detected. Review for security issues.",
                lineno=context.node.lineno
            )

@test.test_id("B705")
@test.checks("Call")
def check_os_env_access(context):
    if context.call_function_name_qual.endswith(('os.getenv', 'os.environ.get')):
        return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.MEDIUM,
            cwe=issue.Cwe.IMPROPER_ACCESS_CONTROL,
            text="Access to environment variable detected using os.getenv() or os.environ.get(). "
                 "Ensure sensitive data is handled securely.",
            lineno=context.node.lineno,
        )

@test.test_id("B706")
@test.checks("Import", "ImportFrom")
def check_kubernetes_sdk_import(context):
    K8S_libraries = ['kubernetes', 'k8s', 'kubernetes_asyncio', 'pykube']
    # Check for Import statements
    if isinstance(context.node, ast.Import):
        for alias in context.node.names:
            if alias.name in K8S_libraries:
                return bandit.Issue(
                    severity=bandit.MEDIUM,
                    confidence=bandit.HIGH,
                    text=f"Use of '{alias.name}' library detected. Review for security issues.",
                    lineno=context.node.lineno
                )

    # Check for ImportFrom statements
    elif isinstance(context.node, ast.ImportFrom):
        module_name = context.node.module
        if module_name in K8S_libraries:
            return bandit.Issue(
                severity=bandit.MEDIUM,
                confidence=bandit.HIGH,
                text=f"Use of from '{module_name}' library detected. Review for security issues.",
                lineno=context.node.lineno
            )
    
        