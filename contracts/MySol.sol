// SPDX-Licence-Identifier: MIT

contract MySol {
    address public the_owner;
    mapping(address => address) juices;
    string uri;
    string uri2;
    string foo;
    string name;
    string symbol;
    string y;

    constructor(address _owner, string memory _name, string memory _symbol) {
        the_owner = _owner;
        foo = "foo?";
        name = _name;
        symbol = _symbol;
        y = _symbol;
    }

    function makeJuiceyJuiceJuiceHeeeeeasdfasdf(string memory _uri) public {
        uri = _uri;
    }
}
