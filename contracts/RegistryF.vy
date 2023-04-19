# @version 0.3.7

addr: public(address)

@external
def register_f(addr2: address):
    assert self.addr != addr2
    self.addr = addr2
