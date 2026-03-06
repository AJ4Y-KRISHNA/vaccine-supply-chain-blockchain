async function main() {

  const VaccineSupplyChain = await ethers.getContractFactory("VaccineSupplyChain");

  const contract = await VaccineSupplyChain.deploy();

  await contract.waitForDeployment();

  console.log("VaccineSupplyChain deployed to:", await contract.getAddress());

}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});