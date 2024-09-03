import pytest


@pytest.fixture(scope="session")
def factory_owner(accounts):
    """
    The account that deploys the factory contract.
    """
    return accounts[0]


@pytest.fixture(scope="session")
def factory_invoker(accounts):
    """
    The account invoking the factory method
    to create the `CreateMe.vy` contract.
    
    NOTE: Purposely using different account
      than owner for testing purposes.
    """
    return accounts[1]


@pytest.fixture(scope="session")
def antazoey(accounts):
    return accounts[2]



@pytest.fixture(scope="session")
def factory(factory_owner, project):
    return factory_owner.deploy(project.Factory)


@pytest.fixture(scope="session")
def create_me_contract(factory, factory_invoker, project):
    # We are using the Vyper-blueprint approach.
    declaration = factory_invoker.declare(project.CreateMe)
    blueprint_address = declaration.contract_address

    # Now, call the creae method with this blueprint to create
    # an instance of it.
    tx = factory.create_contract(blueprint_address, 321, sender=factory_invoker)

    # The address of the instance is available in an event.
    address = tx.events[-1].target

    # Use the `.at()` to return the instance.
    return project.CreateMe.at(address)
