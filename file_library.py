from file_record import FileRecord

class FileLibrary:
    def __init__(self):
        # Initialize empty list to store FileRecord objects
        self.files = []

    def add_file(self, file_path):
        # Create FileRecord object and add to the list
        record = FileRecord(file_path)
        self.files.append(record)

    def list_files(self):
        # Return all file metadata as a list of dictionaries
        return [file.show_info() for file in self.files]

    def get_statistics(self):
        # Create a count of files per file type
        stats = {}
        for file in self.files:
            ext = file.suffix
            stats[ext] = stats.get(ext, 0) + 1
        return stats

    def save_summary(self, path):
        # Write metadata summary to a file
        with open(path, "w", encoding="utf-8") as f:
            for file in self.files:
                f.write(str(file.show_info()) + "\n")
