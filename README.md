# Smart Recruiter Assistant 

**Smart Recruiter Assistant** is an intelligent recruitment tool powered by Retrieval-Augmented Generation (RAG). It helps recruiters interactively search and analyze multiple CVs to find the best candidates quickly and efficiently.



## Requirements 

- Python 3.13.5 or later


## Install Python 

### 🐍 How to Install Python

#### 🔹 Step 1: Download Python
- Go to the official website: https://www.python.org/downloads/
- Click "Download Python 3.x.x" (latest version)

#### 🔹 Step 2: Install Python

##### On Windows:
1. Run the installer.
2. Check the box that says "Add Python to PATH".
3. Click "Install Now".

##### On Ubuntu/Linux:
```bash
sudo apt update
sudo apt install python3 python3-pip
```

##### On macOS (using Homebrew):
```bash
brew install python3
```

#### 🔹 Step 3: Verify Installation
```bash
python3 --version
pip3 --version
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `GEMINI_API_KEY` value.


## Run the FastAPI server

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

