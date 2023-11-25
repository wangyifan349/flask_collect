from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/collect-browser-info', methods=['POST'])
def collect_browser_info():
    data = request.json
    canvas_fingerprint = data.get('canvasFingerprint')
    screen_width = data.get('screenWidth')
    screen_height = data.get('screenHeight')
    user_agent = data.get('userAgent')
    language = data.get('language')
    time_zone_offset = data.get('timeZoneOffset')
    
    # 哈希处理Canvas指纹
    hashed_canvas_fingerprint = hashlib.sha256(canvas_fingerprint.encode()).hexdigest()
    
    # 这里可以添加处理浏览器信息的逻辑，例如存储到数据库等
    # ...

    # 响应前端
    return jsonify({"status": "success", "message": "Browser info collected."})

if __name__ == '__main__':
    app.run(debug=True)
