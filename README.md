# Task-Manger-CLI
Task Manager CLI - Secure &amp; Efficient To-Do Management A Python-based CLI task manager with multi-user support, secure authentication, and task prioritization. Features include task creation, editing, deadlines, backup &amp; restore, and encryption for user data. Simple, secure, and efficient task management from the command line. 🚀

# Task Manager CLI

A secure, multi-user task management system built with Python. This project enables users to register, log in, and manage their tasks securely using encryption and hashing techniques. It includes task creation, updates, and backup & restore functionalities.

## Features
- 🔑 **User Authentication**: Secure login and registration with password hashing.
- ✅ **Task Management**: Create, update, delete, and list tasks.
- 🔄 **Backup & Restore**: Securely store and retrieve user data.
- 📂 **Export System**: Export tasks to CSV/PDF (coming soon!).

## Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/task-manager-cli.git
cd task-manager-cli

# Install dependencies
pip install -r requirements.txt
```

## Usage
```sh
python main.py
```

## Project Structure
```
.
├── /data            # storage users data
├── main.py          # Entry point
├── user.py          # User management
├── task.py          # Task handling
├── managing.py      # File management
├── encryption.py    # Security functions
├── requirements.txt # requirements 
└── README.md        # Project documentation 
```

