from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 确保有一个用于存放上传文件的文件夹
UPLOAD_FOLDER = 'submission'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'result': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'result': 'No selected file'}), 400
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        # 你可以在这里调用你的代码分析模块
        # 比如：result_static = run_static_analysis(filepath)
        # 比如：result_dynamic = run_dynamic_analysis(filepath)
        # 然后整合结果返回
        return jsonify({'result': 'File has been successfully processed'}), 200

if __name__ == '__main__':
    app.run(debug=True)
