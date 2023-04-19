# @version 0.3.7

import interfaces.IRegistryF as IRegistryF

_balance: public(uint256)
registry: public(IRegistryF)

@external
def __init__(registry: IRegistryF):
    self.registry = registry

@external
def addBalance_f(
    num: uint256
) -> uint256:
    assert num != self._balance
    self.registry.register_f(msg.sender)
    self._balance = self._balance + self.addInterest(num)

    # Run some loops.
    for i in [1, 2, 3, 4, 5]:
        if i == num:
            break

    # Fail in the middle (is test)
    # Fails because was already set above.
    self.registry.register_f(msg.sender)

    for i in [1, 2, 3, 4, 5]:
        if i != num:
            continue

    return self._balance

@internal
def addInterest(num: uint256) -> uint256:
    return 123 + num
