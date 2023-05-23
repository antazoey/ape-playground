import ape
import click
import time
from ape.api.networks import LOCAL_NETWORK_NAME
from ape.cli import NetworkBoundCommand, network_option
from ape.exceptions import TransactionError


@click.command(cls=NetworkBoundCommand)
@network_option()
@click.option("--address")
@click.option("--alias", default="metamask0")
def cli(network, address, alias):
    is_local = ape.networks.provider.network.name == LOCAL_NETWORK_NAME
    if address and is_local:
        click.echo("Nothing to do.")
        return

    elif address:
        click.echo(f"Publishing contract at '{address}'...")
        ape.networks.provider.network.explorer.publish_contract(address)

    else:
        click.echo("Deploying contract.")

        if is_local:
            acct = ape.accounts.test_accounts[0]
        else:
            acct = ape.accounts.load(alias)
            acct.set_autosign(True, passphrase="123")

        def do():
            ape.project.RootContract.deploy(sender=acct, publish=not is_local)

        done = False
        total_tries = 10
        for i in range(total_tries): 
            try:
                do()
                done = True
            except TransactionError:
                time.sleep(i)
                continue
                
            if done:
                break
        
        if not done:
            print("sorry??")

