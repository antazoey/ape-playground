import ape
import click
from ape.cli import network_option, NetworkBoundCommand

@click.command(name="math", cls=NetworkBoundCommand)
@network_option()
@click.option("--test", type=click.Choice(["overflow", "underflow", "div_zero", "mod_zero"]))
def cli(network, test):
    account = ape.accounts.test_accounts[0]
    contract = account.deploy(ape.project.VyperMathDevChecks)

    if test == "overflow":
        contract.num_add(1, sender=account)
    elif test == "underflow":
        contract.neg_num_add(-2, sender=account)
    elif test == "div_zero":
        contract.div_zero(0, sender=account)
    elif test == "mod_zero":
        contract.mod_zero(0, sender=account)

