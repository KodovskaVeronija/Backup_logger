import os
import json
from backup import perform_backup

def main():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            config = json.load(f)
    else:
        config = {}

    source = input(f"Enter source folder [{config.get('source', '')}]: ") or config.get('source', '')
    destination = input(f"Enter destination folder [{config.get('destination', '')}]: ") or config.get('destination', '')
    version = input(f"Enter software version [{config.get('version', '1.0.0')}]: ") or config.get('version', '1.0.0')
    zip_choice = input("Use zip compression? (y/n) [y]: ") or 'y'
    use_zip = zip_choice.lower() == 'y'

    if not source or not destination:
        print("Source and destination are required.")
        return

    config.update({
        "source": source,
        "destination": destination,
        "version": version
    })

    with open("config.json", "w") as f:
        json.dump(config, f)

    perform_backup(source, destination, version, use_zip)

if __name__ == "__main__":
    main()
