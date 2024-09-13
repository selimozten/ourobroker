#!/bin/bash
echo "Deploying smart contracts..."
truffle migrate --network mainnet
echo "Deployment complete."
