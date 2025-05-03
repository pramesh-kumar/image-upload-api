# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename  # Missing import added
# import os
# from flask_cors import CORS

# app = Flask(__name__)


# CORS(app)  # Allow all origins

# # Configuration
# app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')  # Simplified path
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB file size limit

# # Create uploads folder if it doesn't exist
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image part"}), 400

#     image = request.files['image']
    
#     if image.filename == '':
#         return jsonify({"error": "No selected image"}), 400

#     try:
#         filename = secure_filename(image.filename)
#         save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         image.save(save_path)
#         return jsonify({
#             "message": "Image uploaded successfully",
#             "path": save_path
#         }), 200
        
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)





from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
import os

app = Flask(__name__)
CORS(app)

# Configure uploads
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": "File uploaded successfully"}), 200

    return jsonify({"error": "Invalid file type"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)