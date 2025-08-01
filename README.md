# Python Folder Backup Tool

This tool allows you to back up a folder to a chosen destination, with timestamping, version tagging, and optional ZIP compression. It supports command-line and GUI versions.

## Features

- Copy folders or compress them into ZIP archives
- Automatically names backups like: `backup_2025-08-01_10-30-00_v1.0.0`
- Logs backup status, file count, and duration
- Stores preferences in `config.json`
- GUI version with Tkinter (only works on local machines)

## Usage (CLI)

### 1. Run the backup
```bash
python main.py
```

### 2. Input:
- Source folder path
- Destination folder path
- Software version (e.g., 1.0.0)
- ZIP compression (y/n)

### 3. Output:
- Backup created in the destination
- Log appended to `backup.log`

## Structure

```
backup_project/
├── main.py
├── backup.py
├── config.json  # Created on first run
├── backup.log   # Created automatically
└── README.md
```

## Screenshot (GUI version)
> _To be added after GUI test on local machine._

## License
MIT
