# Spreetail Expense Importer

## Overview

This project imports a CSV expense dataset, detects anomalies, generates an import report, and stores valid records in a SQLite database.

The project was developed as part of the Spreetail Software Developer assignment.

---
deployement link - https://spreetailexpense-importer-ovej6punm2e6tf7pozjapp7.streamlit.app/

## Features

* CSV ingestion
* Dataset profiling
* Missing value detection
* Anomaly detection
* Import report generation
* SQLite database integration
* Git version control with meaningful commit history

---

## Technologies Used

* Python
* Pandas
* SQLite
* Git
* GitHub

---

## Project Structure

Spreetail/

* analyze.py
* anomaly_detector.py
* database.py
* import_to_db.py
* view_db.py
* requirements.txt
* reports/
* docs/

---

## Setup Instructions

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Dataset Analysis

```bash
python analyze.py
```

### Generate Import Report

```bash
python anomaly_detector.py
```

### Create Database

```bash
python database.py
```

### Import Records

```bash
python import_to_db.py
```

### View Imported Records

```bash
python view_db.py
```

---

## AI Usage

AI assistance was used during development for:

* Data profiling guidance
* Anomaly detection logic
* SQLite integration
* Documentation support

All AI-generated suggestions were manually reviewed before implementation.
