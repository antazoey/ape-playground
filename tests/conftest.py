import pytest


@pytest.fixture(scope="session", autouse=True)
def deploy_libraries(project, account, solidity):
    library = project.Set.deploy(sender=account)
    solidity.add_library(library)


@pytest.fixture(scope="session")
def solidity(project):
    return project.compiler_manager.registered_compilers[".sol"]


@pytest.fixture(scope="session")
def account(accounts):
    return accounts[0]


@pytest.fixture(scope="session")
def contract(project, deploy_libraries, account):
    _ = deploy_libraries  # Ensure deploy_libraries fixture happens first.
    return project.C.deploy(sender=account)
