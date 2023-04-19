# @version 0.3.7


MAX_POOLS : constant(uint256) = 5


struct WorkingStruct:
    one: uint256
    two: uint256
    three: uint256
    four: uint256
    five: uint256

struct BrokenStruct:
    one: uint256
    two: uint256
    three: uint256
    four: uint256
    five: uint256
    six: uint256


struct AlsoWorkingStruct:
    one: uint256
    two: uint256
    three: uint256
    four: uint256


@external
def __init__():
    pass

@external
@view 
def getBrokenStruct() -> ( uint256, BrokenStruct[MAX_POOLS]):
    result : BrokenStruct[MAX_POOLS] = empty(BrokenStruct[MAX_POOLS])
    return 0, result

@external
@view 
def getBrokenStructNot() -> ( BrokenStruct[MAX_POOLS]):
    result : BrokenStruct[MAX_POOLS] = empty(BrokenStruct[MAX_POOLS])
    return result


@external
@view 
def getWorkingStruct() -> ( uint256, WorkingStruct[MAX_POOLS]):
    result : WorkingStruct[MAX_POOLS] = empty(WorkingStruct[MAX_POOLS])
    return 0, result


@external
@view 
def getAlsoWorkingStruct() -> ( uint256, AlsoWorkingStruct[MAX_POOLS]):
    result : AlsoWorkingStruct[MAX_POOLS] = empty(AlsoWorkingStruct[MAX_POOLS])
    return 0, result
