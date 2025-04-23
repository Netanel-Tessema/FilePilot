from pathlib import Path
from datetime import datetime

class FileRecord:
    def __init__(self, file_path):
        # Convert string to Path object and check if file exists
        self.path = Path(file_path)
        if self.path.is_file():
            # Extract relevant file info
            self.name = self.path.name
            self.suffix = self.path.suffix
            self.size = self.path.stat().st_size
            self.creation_time = self.path.stat().st_ctime
        else:
            raise FileNotFoundError("File does not exist")

    def get_formatted_time(self):
        # Convert timestamp to human-readable format
        return datetime.fromtimestamp(self.creation_time).strftime("%Y-%m-%d %H:%M:%S")

    def show_info(self):
        # Return dictionary of file metadata
        return {
            "name": self.name,
            "suffix": self.suffix,
            "size": f"{self.size} bytes",
            "creation time": self.get_formatted_time()
        }
