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
def targets(factory, factory_invoker, project):
    # We are using the Vyper-blueprint approach.
    declaration_a = factory_invoker.declare(project.TargetA)
    blueprint_address_a = declaration_a.contract_address
    declaration_b = factory_invoker.declare(project.TargetB)
    blueprint_address_b = declaration_b.contract_address

    # Now, call the creae method with this blueprint to create
    # an instance of it.
    tx = factory.create_contract(
        blueprint_address_a, blueprint_address_b, 321, sender=factory_invoker
    )

    # The address of the instance is available in an event.
    target_address_a = tx.events[-1].target_a
    target_address_b = tx.events[-1].target_b

    return (target_address_a, target_address_b)


@pytest.fixture(scope="session")
def target_a(targets, project):
    return project.TargetA.at(targets[0])


@pytest.fixture(scope="session")
def target_b(targets, project):
    return project.TargetB.at(targets[1])
