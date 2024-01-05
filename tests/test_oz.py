import pytest



@pytest.fixture
def account(accounts):
    return accounts[0]


@pytest.fixture
def contract(project, account):
    return account.deploy(project.MyContract)


@pytest.fixture
def oz5(project):
    return project.dependencies["OpenZeppelin"]["v5.0.1"]


def test_oz(oz5):
    """
    Show contracts are accessible from OpenZeppelin 0.5
    """
    assert len(oz5.contracts) > 1


def test_contract(contract, account):
    # Really just showing it compiled, deployed, and is usable.
    pass