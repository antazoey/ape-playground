from ape.logging import LogLevel, logger

# def ape_init_extras(accounts, project):
#     level = logger.level
#     logger.set_level(LogLevel.ERROR)
#     account = accounts.test_accounts[0]
#     registry = project.Registry.deploy(sender=account)
#     contract = project.VyperContract.deploy(registry, sender=account)
#     broke = project.Broke.deploy(sender=account)

#     def rec():
#         return contract.addBalance_f(123, sender=account)

#     logger.set_level(level)
#     return {
#         "account": account,
#         "registry": registry,
#         "contract": contract,
#         "rec": rec,
#         "broke": broke
#     }
