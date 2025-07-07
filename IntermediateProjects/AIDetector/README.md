# Project: AI-Based Threat Detection

### DESCRIPTION:
This project uses machine learning to detect malicious network traffic.
It trains a Random Forest Classifier on a labeled dataset of traffic patterns.

### TOOLS USED:
```
Python 3.x
pandas, numpy, scikit-learn
joblib (for model saving)
matplotlib (optional)
virtualenv (recommended)
```
### SETUP STEPS:

Step 1: Create Project Structure
mkdir AIDetector
cd AIDetector
mkdir data models screenshots
touch main.py README.md findings.md requirements.txt

### Step 2: Add Requirements
```
Inside requirements.txt:
pandas
numpy
scikit-learn
matplotlib
joblib
```
![AI Threat Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/AIDetector/screenshots/0.png)

### Step 3: Setup Python Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Step 4: Create CSV Dataset
```
File: data/sample_traffic.csv
Content:
duration,protocol_type,src_bytes,dst_bytes,flag,label
0,tcp,491,0,SF,normal
0,tcp,146,0,SF,normal
0,tcp,232,8153,SF,normal
0,tcp,199,420,SF,normal
0,tcp,300,1500,SF,malicious
0,tcp,100,50,REJ,malicious
```

### Step 5: Create Script (main.py)
```
Script loads the CSV, encodes features, trains a model, and outputs metrics.
```
### Step 6: Run the Detector
```
python main.py
```
![AI Threat Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/AIDetector/screenshots/1.png)
### OUTPUT:
```
-- - Trained model: models/threat_detector.pkl
-- - Report: findings.md
-- - Visual proof: screenshots/threat_model_output.png

-- NEXT STEPS:
-- [ ] Add packet capture → CSV converter
-- [ ] Build live detection system using Scapy or pyshark
-- [ ] Add auto-alert or email/report feature

-- STATUS: COMPLETE (STATIC CSV DETECTION DEMO)
```
![AI Threat Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/IntermediateProjects/AIDetector/screenshots/nano.png)
