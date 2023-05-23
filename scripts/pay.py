import ape
import click
from ape.cli import NetworkBoundCommand, network_option


_TESTS = ("pay", "pay2", "dontpay", "dontpay2", "empty_revert", "empty_revert2", "both", "both2", "pay_and_fail")


@click.command(cls=NetworkBoundCommand)
@network_option()
@click.option("--test", type=click.Choice(_TESTS), required=True)
def cli(network, test):
    account = ape.accounts.test_accounts[0]
    contract = account.deploy(ape.project.Pay)
    if test == _TESTS[0]:
        # Pass on first method because is payable
        receipt = contract.pay(1, sender=account, value=1)
        receipt.show_source_traceback()
    elif test == _TESTS[1]:
        # Pass on second method because is also payable
        receipt = contract.pay2(1, sender=account, value=1)
        receipt.show_source_traceback()
    elif test == _TESTS[2]:
        # Fail on nonpayable check for the first method
        contract.dontpay(1, sender=account, value=1)
    elif test == _TESTS[3]:
         # Fail on nonpayable check for the second method
        contract.dontpay2(1, sender=account, value=1)
    elif test == _TESTS[4]:
        # Fail on first empty revert to see how it compares
        contract.dontpay(0, sender=account)
    elif test == _TESTS[5]:
        # Fail on first empty revert to see how it compares
        contract.dontpay2(0, sender=account)
    elif test == _TESTS[6]:
        # Use both value and cause empty revert fail.
        # Hopefully value check fails first...
        contract.dontpay(0, sender=account, value=1)
    elif test == _TESTS[7]:
        # Use both value and cause empty revert fail.
        # Hopefully value check fails first...
        contract.dontpay2(0, sender=account, value=1)
    elif test == _TESTS[8]:
        # This fail
        contract.pay(0, sender=account, value=1)

