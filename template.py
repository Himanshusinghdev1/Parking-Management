import os
from pathlib import Path
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project name
project_name = "cnnParking"

# List of files and directories to create
list_of_files = [
    # GitHub Actions
    ".github/workflows/.gitkeep",

    # Source Code Structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    # Configurations
    "config/config.yaml",
    "params.yaml",

    # Training & Detection
    f"src/{project_name}/preprocessing/video_loader.py",
    f"src/{project_name}/preprocessing/annotation_tool.py",
    f"src/{project_name}/preprocessing/preprocess.py",
    f"src/{project_name}/detection/vehicle_detection.py",
    f"src/{project_name}/detection/parking_status.py",
    f"src/{project_name}/utils/visualization.py",
    f"src/{project_name}/utils/config.py",
    f"src/{project_name}/utils/helpers.py",

    # Training & Execution Scripts
    "train.py",
    "detect.py",

    # Output & Logs
    "output/detected_videos/.gitkeep",
    "output/logs/.gitkeep",
    "output/reports/.gitkeep",

    # Requirements & Setup
    "requirements.txt",
    "setup.py",
    
    # Research & Experiments
    "research/trials.ipynb",

    # Web Interface
    "templates/index.html",

    # Documentation
    "README.md"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            if filename.endswith(".py"):
                f.write("# This is a Python file\n")
            elif filename.endswith(".yaml"):
                f.write("# YAML configuration file\n")
            elif filename.endswith(".gitkeep"):
                f.write("")
            elif filename.endswith(".md"):
                f.write("# Project Documentation\n")
            elif filename.endswith(".html"):
                f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Parking Management</title>\n</head>\n<body>\n</body>\n</html>")
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")

print("🚀 Project structure generated successfully!")
