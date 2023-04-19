import pytest


@pytest.fixture(scope="session")
def account(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def registry(account, project):
    return account.deploy(project.Registry)


@pytest.fixture(scope="session")
def contract(project, registry, account):
    return account.deploy(project.TracebackContract, registry)
