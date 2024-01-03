struct Profile:
    # userID: uint256 
    userName: String[64]
    pfpContract: address
    pfpID: uint256
    bio: String[256]

profileStore: HashMap[address, Profile]
denyList: HashMap[address, bool]

@external
def deny(addr: address):
    self.denyList[addr] = True

@view
@external
def checkAccess(addr: address) -> bool:
    return not self._denied(addr)

@view
@internal
def _denied(addr: address) -> bool:
    return self.denyList[msg.sender]
