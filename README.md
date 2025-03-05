# lm-works-ashok
LM Works 1) QA Creator 

# How to run 

1)Create an virtual environment and activate

```
eg: 
 conda create -n intqa python=3.10 -y
 conda activate intqa

```

Stack Used : Langchain, FAstAPI, FAISS, OPENAI, Embedding models 


2. install requirements
   pip install -r requirements.txt 

## Deploying  this app on EC2 instance

Login with your AWS console and launch an EC2 instance

2. Run the following commands
Note: Do the port mapping to this port:- 8511 - as per the given in app.py

sudo apt update
sudo apt-get update
sudo apt upgrade -y
sudo apt install git curl unzip tar make sudo vim wget -y
 
git clone "Your-repository"
Note : create a .env file and add keys 

sudo apt install python3-pip

sudo apt install python3-venv
python3 -m venv .venv
source .venv/bin/activate


pip3 install -r requirements.txt

#Temporary running
python3 app.py 

#Permanent running
nohup python3 app.py