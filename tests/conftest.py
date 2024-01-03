import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def scammer(accounts):
    return accounts[1]


@pytest.fixture
def contract(project, owner):
    return owner.deploy(project.repro1777)
