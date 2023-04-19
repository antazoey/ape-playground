
// See https://hardhat.org/config/ for config options.
import { HardhatUserConfig } from "hardhat/config";

const config: HardhatUserConfig = {
  networks: {
    hardhat: {
      hardfork: "shanghai",
      // Base fee of 0 allows use of 0 gas price when testing
      initialBaseFeePerGas: 0,
      accounts: {

        path: "m/44'/60'/0'",
        count: 10
      }
    },
  },
};

export default config;
