#!/bin/bash

echo "=== Zero Trust Setup Simulation ==="

echo "[1] Checking device health..."
bash ./src/health-check.sh
echo ""

echo "[2] Verifying access identity..."
python3 ./src/verify-access.py
echo ""

echo "[3] Applying access policies..."
echo "(simulated): Loaded access-policies.yaml"
cat ./policies/access-policies.yaml
echo ""

echo "[4] Applying microsegmentation rules..."
echo "(simulated): Loaded firewall-rules.json"
cat ./policies/firewall-rules.json
echo ""

echo "=== Zero Trust Simulation Complete ==="
