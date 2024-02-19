// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.22 <0.9.0;

contract Control {
  event Event1(uint32 _numWords, address indexed _owner);

  function control() public {
    emit Event1(123, msg.sender);
  }
}
