# @version 0.3.7

@external
def foo_method(a: uint256 = 3, b: uint256 = 1) -> bool:
    assert a != 0  # dev: sub-zero
    return True


@external
def FOOBAR_ignore_me() -> bool:
    return True
