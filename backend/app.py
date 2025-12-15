from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app) # هذا السطر يسمح لتطبيق الهاتف بالاتصال بالخادم

FACT_CHECK_STATUSES = [
    {"status": "trueFact", "message": "هذه المعلومة صحيحة بناءً على المصادر الموثوقة."},
    {"status": "falseFact", "message": "هذه المعلومة مضللة أو خاطئة، يرجى الحذر."},
    {"status": "unverified", "message": "لم يتم العثور على تأكيد جازم لهذه المعلومة بعد."}
]

@app.route('/check', methods=['POST'])
def check_fact():
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "الرجاء إدخال نص للتحقق"}), 400

    # محاكاة لعملية التحقق (سنقوم بربطها بالذكاء الاصطناعي لاحقاً)
    result = random.choice(FACT_CHECK_STATUSES)
    
    return jsonify({
        "original_text": text,
        "verdict": result["status"],
        "explanation": result["message"]
    })

if __name__ == '__main__':
    # تشغيل الخادم على المنفذ 5000 متاحاً لكل الشبكة
    app.run(host='0.0.0.0', port=5000, debug=True)

