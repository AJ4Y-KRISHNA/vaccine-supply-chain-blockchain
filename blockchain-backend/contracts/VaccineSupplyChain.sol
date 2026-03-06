// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract VaccineSupplyChain {

    struct Batch {
        string batchId;
        string vaccineName;
        string manufacturer;
        string currentHolder;
    }

    mapping(string => Batch) public batches;

    function registerBatch(
        string memory _batchId,
        string memory _vaccineName,
        string memory _manufacturer
    ) public {

        batches[_batchId] = Batch(
            _batchId,
            _vaccineName,
            _manufacturer,
            _manufacturer
        );
    }

    function transferBatch(
        string memory _batchId,
        string memory _newHolder
    ) public {

        batches[_batchId].currentHolder = _newHolder;
    }

    function getBatch(
        string memory _batchId
    ) public view returns (
        string memory,
        string memory,
        string memory,
        string memory
    ) {

        Batch memory b = batches[_batchId];

        return (
            b.batchId,
            b.vaccineName,
            b.manufacturer,
            b.currentHolder
        );
    }
}