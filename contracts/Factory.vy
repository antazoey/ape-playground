event Deployment:
    target_a: address
    target_b: address

@external
def create_contract(target1: address, target2: address, _num: uint256) -> (address, address):
    ta: address = create_from_blueprint(target1, _num, code_offset=3)
    tb: address = create_from_blueprint(target2, _num, code_offset=3)
    log Deployment(ta, tb)
    return (ta, tb)
