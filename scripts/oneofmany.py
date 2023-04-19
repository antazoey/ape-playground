from ape import accounts, project


def main():
    owner = accounts.test_accounts[0]
    contract_c = owner.deploy(project.ContractC)
    contract_b = owner.deploy(project.ContractB, contract_c)
    contract_a = owner.deploy(project.ContratC, contract_b, contract_c)
    receipt = contract_a.emitLogWithSameInterfaceFromMultipleContracts(sener=owner)
    
