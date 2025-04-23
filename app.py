from flask import Flask, render_template, request, send_file, jsonify
from file_library import FileLibrary
import os

app = Flask(__name__)
library = FileLibrary()

@app.route("/", methods=["GET", "POST"])
def index():
    # Handle file upload
    if request.method == "POST":
        uploaded_file = request.files.get("file")
        if uploaded_file:
            file_path = os.path.join("uploads", uploaded_file.filename)
            uploaded_file.save(file_path)
            try:
                library.add_file(file_path)
            except FileNotFoundError:
                pass
    return render_template("index.html", files=library.list_files())

@app.route("/download-summary")
def download_summary():
    # Save and return file metadata summary as downloadable text file
    path = "summary.txt"
    library.save_summary(path)
    return send_file(path, as_attachment=True)

@app.route("/stats")
def stats():
    # Return file type statistics as JSON for chart rendering
    return jsonify(library.get_statistics())

if __name__ == "__main__":
    # Ensure uploads folder exists and run the Flask app
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
