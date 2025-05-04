# # from flask import Flask, request, jsonify
# # from werkzeug.utils import secure_filename  # Missing import added
# # import os
# # from flask_cors import CORS

# # app = Flask(__name__)


# # CORS(app)  # Allow all origins

# # # Configuration
# # app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')  # Simplified path
# # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB file size limit

# # # Create uploads folder if it doesn't exist
# # os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# # @app.route('/upload', methods=['POST'])
# # def upload_image():
# #     if 'image' not in request.files:
# #         return jsonify({"error": "No image part"}), 400

# #     image = request.files['image']
    
# #     if image.filename == '':
# #         return jsonify({"error": "No selected image"}), 400

# #     try:
# #         filename = secure_filename(image.filename)
# #         save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
# #         image.save(save_path)
# #         return jsonify({
# #             "message": "Image uploaded successfully",
# #             "path": save_path
# #         }), 200
        
# #     except Exception as e:
# #         return jsonify({"error": str(e)}), 500

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=8000, debug=True)





# # from flask import Flask, request, jsonify
# # from werkzeug.utils import secure_filename
# # from flask_cors import CORS
# # from config import UPLOAD_FOLDER, ALLOWED_EXTENSIONS
# # import os

# # app = Flask(__name__)
# # CORS(app)

# # # Configure uploads
# # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# # os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # def allowed_file(filename):
# #     return '.' in filename and \
# #            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # @app.route('/upload', methods=['POST'])
# # def upload_image():
# #     if 'image' not in request.files:
# #         return jsonify({"error": "No image part"}), 400

# #     file = request.files['image']
# #     if file.filename == '':
# #         return jsonify({"error": "No selected file"}), 400

# #     if file and allowed_file(file.filename):
# #         filename = secure_filename(file.filename)
# #         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# #         return jsonify({"message": "File uploaded successfully"}), 200

# #     return jsonify({"error": "Invalid file type"}), 400

# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=8000, debug=True)



# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename
# from flask_cors import CORS
# import os
# import datetime

# app = Flask(__name__)
# CORS(app)

# # Configuration - Path Updated
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Gets app/ directory
# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')     # app/uploads/
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Create uploads directory inside app/ if not exists
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image part"}), 400

#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     try:
#         # Save the image
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Generate response
#         response_data = {
#             "status": "success",
#             "message": "Image saved successfully!",
#             "filename": filename,
#             "saved_path": filepath,
#             "timestamp": datetime.datetime.now().isoformat(),
#             "file_size_kb": os.path.getsize(filepath) / 1024
#         }

#         return jsonify(response_data), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# if __name__ == '__main__':
#     print(f"Uploads folder path: {app.config['UPLOAD_FOLDER']}")  # Verify path
#     app.run(host='0.0.0.0', port=8001, debug=True)





# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# from flask_cors import CORS
# import os
# import datetime

# app = Flask(__name__)
# CORS(app)

# # Configuration
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app/ directory
# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')      # app/uploads/
# RESULTS_FOLDER = os.path.join(BASE_DIR, 'results')     # app/results/

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Create folders if they don't exist
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULTS_FOLDER, exist_ok=True)

# # Serve uploaded and result images
# @app.route('/uploads/<filename>')
# def serve_uploaded_image(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/results/<filename>')
# def serve_result_image(filename):
#     return send_from_directory(RESULTS_FOLDER, filename)

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image part"}), 400

#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     try:
#         # Save the uploaded image
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Generate URLs for the client
#         captured_image_url = f"http://{request.host}/uploads/{filename}"
#         resultant_image_url = f"http://{request.host}/results/test.jpg"

#         response_data = {
#             "status": "success",
#             "message": "Image saved successfully!",
#             "filename": filename,
#             "captured_image_url": captured_image_url,
#             "resultant_image_url": resultant_image_url,
#             "timestamp": datetime.datetime.now().isoformat(),
#             "file_size_kb": os.path.getsize(filepath) / 1024
#         }

#         return jsonify(response_data), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# if __name__ == '__main__':
#     print(f"Uploads folder: {app.config['UPLOAD_FOLDER']}")
#     print(f"Results folder: {RESULTS_FOLDER}")
#     app.run(host='0.0.0.0', port=8001, debug=True)








# from flask import Flask, request, jsonify, send_from_directory
# from werkzeug.utils import secure_filename
# from flask_cors import CORS
# import os
# import datetime
# import cv2  # Add OpenCV for image processing

# app = Flask(__name__)
# CORS(app)

# # Configuration
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
# RESULTS_FOLDER = os.path.join(BASE_DIR, 'results')

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Create folders if missing
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULTS_FOLDER, exist_ok=True)

# def process_image(input_path, output_folder):
#     """Example: Convert image to grayscale and save to results folder."""
#     img = cv2.imread(input_path)
#     if img is None:
#         raise ValueError("Could not read image")
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     # Generate unique output filename
#     timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#     output_filename = f"result_{timestamp}.jpg"
#     output_path = os.path.join(output_folder, output_filename)
#     cv2.imwrite(output_path, gray)
#     return output_filename

# @app.route('/uploads/<filename>')
# def serve_uploaded_image(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# @app.route('/results/<filename>')
# def serve_result_image(filename):
#     return send_from_directory(RESULTS_FOLDER, filename)

# @app.route('/upload', methods=['POST'])
# def upload_image():
#     if 'image' not in request.files:
#         return jsonify({"error": "No image part"}), 400

#     file = request.files['image']
#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     try:
#         # Save uploaded image
#         filename = secure_filename(file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(filepath)

#         # Process image and get result filename
#         result_filename = process_image(filepath, RESULTS_FOLDER)

#         # Generate URLs
#         captured_url = f"http://{request.host}/uploads/{filename}"

#         result_url = f"http://{request.host}/results/{result_filename}"

#         return jsonify({
#             "status": "success",
#             "captured_image_url": captured_url,
#             "resultant_image_url": result_url
#         }), 200

#     except Exception as e:
#         return jsonify({"status": "error", "message": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8001, debug=True)





from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
import datetime
import cv2  # For image processing
import socket  # To fetch local IP

app = Flask(__name__)
CORS(app)

# ==================================================================
# Configuration (MODIFY THIS SECTION)
# ==================================================================
# Get your computer's local IP automatically
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# YOUR_LOCAL_IP = get_local_ip()  # Auto-detects IP (e.g., 192.168.1.5)
YOUR_LOCAL_IP = "172.18.41.74" # Auto-detects IP (e.g., 192.168.1.5)
PORT = 8001
# ==================================================================

# Folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
RESULTS_FOLDER = os.path.join(BASE_DIR, 'results')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

def process_image(input_path, output_folder):
    """Example: Convert to grayscale"""
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("Could not read image")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Generate unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_filename = f"result_{timestamp}.jpg"
    output_path = os.path.join(output_folder, output_filename)
    cv2.imwrite(output_path, gray)
    return output_filename

@app.route('/uploads/<filename>')
def serve_uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/results/<filename>')
def serve_result_image(filename):
    return send_from_directory(RESULTS_FOLDER, filename)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Save uploaded image
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        print(filename, filepath)
        file.save(filepath)

        # Process image
        result_filename = process_image(filepath, RESULTS_FOLDER)

        # ==================================================================
        # Updated URL generation using your local IP
        # ==================================================================
        captured_url = f"http://{YOUR_LOCAL_IP}:{PORT}/uploads/{filename}"
        result_url = f"http://{YOUR_LOCAL_IP}:{PORT}/results/{result_filename}"

        return jsonify({
            "status": "success",
            "captured_image_url": captured_url,
            "resultant_image_url": result_url
        }), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print(f"Server accessible at: http://{YOUR_LOCAL_IP}:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)