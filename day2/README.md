# My Modular Python CLI Tool
*A Day 2 backend engineering project focusing on Python modules, packages, and system architecture.*

---

## 📌 Overview

This project is part of a learning path focused on backend engineering fundamentals.  
The goal is not just to write Python code, but to understand **how modules, packages, logic, and system structure work together** — the same way real backend applications are designed.

This CLI tool demonstrates:

- Using Python modules and packages  
- Project organization and architecture  
- Working with built-in Python libraries  
- Separation of concerns  
- Logging and timestamping  
- JSON processing  
- Random data generation  
- Clean application flow  
- Error handling  

---

## 🚀 Features

### ✔ Accepts JSON input from the user  
The application reads a JSON string and converts it into a Python dictionary.

### ✔ Generates random user profiles  
A utility module creates mock user data (id, name, age).

### ✔ Records timestamped logs  
Every run creates a log file with a **safe, cross-platform timestamped filename**.

### ✔ Saves combined data into a `logs/` directory  
The log file contains:
- timestamp  
- parsed user input  
- generated user profile  

### ✔ Modular, extensible design  
Logic is divided into clean modules:
- `json_utils.py`  
- `time_utils.py`  
- `random_utils.py`  
- `main.py`  

---

## 🧩 Project Structure

my_tool/
│
├── main.py
├── init.py
├── README.md
│
└── utils/
├── init.py
├── json_utils.py
├── time_utils.py
└── random_utils.py

yaml
Copy code

Each file has a single responsibility, following clean architecture principles.

---

## 📦 Modules Explained

### **utils/json_utils.py**
Handles all JSON operations:
- Convert JSON string → Python dict  
- Convert Python dict → JSON string  
- Raise friendly errors on invalid JSON  

---

### **utils/time_utils.py**
Provides:
- Human-readable timestamps  
- Safe filenames for logs (cross-platform)  

---

### **utils/random_utils.py**
Generates:
- Random alphanumeric IDs  
- Random user profiles (name, age, id)  

Useful for testing, prototyping, and mock data.

---

### **main.py**
The entry point of the application.  
It coordinates:

1. Reading JSON input  
2. Parsing and validating JSON  
3. Generating random user data  
4. Combining both pieces of data  
5. Saving everything as a log file  
6. Printing summaries to the terminal  

---

## ⚙️ Requirements

- Python 3.10+ (recommended)
- Virtual environment (optional but recommended)

No external packages are required — everything uses Python built-ins.

---

## ▶️ How to Run

From your terminal:

```bash
cd my_tool
python main.py
You'll be prompted to enter a JSON string.

Example:

json
Copy code
{"app": "demo", "version": 1}
The program will:

Parse your JSON

Generate a random user profile

Save everything to a timestamped file inside the logs/ folder

Example output file:

bash
Copy code
logs/session_2025-11-15_20-23-44.txt
📁 Example Log File
json
Copy code
{
    "timestamp": "2025-11-15 20:23:44",
    "input": {
        "app": "demo",
        "version": 1
    },
    "generated_profile": {
        "id": "a81Kd93LsQ",
        "name": "Diana",
        "age": 34
    }
}
🧠 Learning Objectives (Day 2)
This project demonstrates:

Python modules and packages

Clean folder structure

Separation of concerns (SRP)

JSON processing

Timestamping and file naming

Randomized test-data generation

Error handling

Logging

Building a simple CLI with orchestrated logic

🔮 Future Improvements
Potential extensions:

Add CLI arguments (argparse)

Add configuration file support (config.json)

Add .env support for environment variables

Improve error logging

Turn into an installable package (pip install)

Add user-defined output file names

Add support for reading JSON from files

Add automatic tests (pytest)

💬 Author
Part of a structured backend development learning journey.
Designed using real-world engineering principles and modular architecture.