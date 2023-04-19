# @version 0.3.7

addr: public(address)

@external
def register(addr: address):
    self.addr = addr

@payable
@external
def register_p(addr: address):
    self.addr = addr

