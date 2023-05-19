# @version 0.3.7

@external
def dontpay(v: uint256) -> uint256:
    assert v != 0
    return 123


@external
def dontpay2(v: uint256) -> uint256:
    assert v != 0
    return 123
