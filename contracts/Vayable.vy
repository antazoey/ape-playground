# @version 0.3.7

addr: public(address)

@external
def __init__(_asset: address):
    self.addr = _asset

@external
def register(addr: address):
    self.addr = addr

@payable
@external
def register_p(addr: address):
    self.addr = addr


@payable
@internal
def internal_pay(addr: address):
    self.addr = addr

