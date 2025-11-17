
# ملف: app.py - التحديث النهائي: محاكاة البحث العكسي عن الصور

from flask import Flask, request, jsonify
import random
import re
import os
import io
import time # ⚠️ جديد: لاستخدامه في محاكاة التأخير
from PIL import Image
import nltk
from arabic_stopwords import get_arabic_stopwords
from urllib.parse import urlparse 
import requests 

app = Flask(__name__)

# قائمة بحالات التحقق الممكنة
FACT_CHECK_STATUSES = [
    "trueFact",
    "falseFact",
    "unverified"
]

# قاعدة البيانات الأولية لتقييم المصادر
TRUSTED_DOMAINS = [
    "bbc.com", "reuters.com", "aljazeera.net", "cnn.com"
]

SUSPICIOUS_DOMAINS = [
    "fake-news-site.info", "conspiracytheory.org", "unreliable-blog.net"
]


# الدوال المساعدة (تبقى كما هي)
def _analyze_keywords(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    tokens = nltk.word_tokenize(text)
    stopwords = get_arabic_stopwords()
    filtered_tokens = [word for word in tokens if word not in stopwords and len(word) > 2]
    return filtered_tokens

def _check_url_trust(text):
    urls = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)
    if not urls:
        return None
    try:
        parsed_uri = urlparse(urls[0])
        domain = '{uri.netloc}'.format(uri=parsed_uri).replace('www.', '')

        if domain in TRUSTED_DOMAINS:
            return {"status": "trueFact", "message": f"الرابط يشير إلى مصدر موثوق ومعروف: {domain}"}
        elif domain in SUSPICIOUS_DOMAINS:
            return {"status": "falseFact", "message": f"الرابط يشير إلى مصدر مشبوه أو غير معروف: {domain}"}
        else:
            return None
    except Exception:
        return None

# ----------------------------------------------------------------------------------
# 1. نقطة نهاية التحقق من النص (CHECK_TEXT) - تبقى كما هي
# ----------------------------------------------------------------------------------

@app.route('/check_text', methods=['POST'])
def check_text():
    # ... (منطق تحليل الرابط والكلمات المفتاحية كما هو)
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()
    input_text = data.get('text', '').strip()

    if not input_text:
        return jsonify({"status": "unverified", "message": "لم يتم إدخال نص للتحقق."}), 200

    # 1. فحص الرابط أولاً
    url_result = _check_url_trust(input_text)
    if url_result:
        return jsonify({
            "status": url_result['status'], 
            "message": url_result['message'],
            "sourceText": input_text,
        }), 200

    # 2. تحليل الكلمات المفتاحية
    keywords = _analyze_keywords(input_text)
    
    # منطق القرار المعتمد على الكلمات المفتاحية
    if any(k in keywords for k in ["انقلاب", "مؤامرة", "ثورة", "دمار", "تخريب", "خداع"]):
        if random.random() < 0.65:
            result_status = "falseFact"
            result_message = f"تحذير: النص يحتوي على كلمات مفتاحية (مثل {', '.join(keywords)}) مثيرة للجدل والمراجعة."
        else:
            result_status = "unverified"
            result_message = f"تم استخراج الكلمات المفتاحية: {', '.join(keywords)}. يرجى التحقق يدوياً."
    
    else:
        result_status = random.choice(["unverified", "falseFact", "trueFact"])
        result_message = "نتيجة أولية: لم يتم إيجاد نمط واضح. قيد المراجعة."

    return jsonify({
        "status": result_status, 
        "message": result_message,
        "sourceText": input_text,
    }), 200

# ----------------------------------------------------------------------------------
# 2. نقطة نهاية التحقق من الصور (REVERSE_IMAGE_SEARCH) - منطق محاكاة جديد
# ----------------------------------------------------------------------------------

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/check_image', methods=['POST'])
def check_image():
    """
    نقطة نهاية لاستقبال صورة وإجراء بحث عكسي متقدم (محاكاة).
    """
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files['image']
    
    try:
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        width, height = image.size
        
        # ⚠️ الخطوة الجديدة 1: محاكاة التأخير لعملية البحث الخارجي
        time.sleep(2) # تأخير لمدة ثانيتين لمحاكاة وقت استجابة محرك البحث
        
        # ⚠️ الخطوة الجديدة 2: منطق محاكاة نتيجة البحث بناءً على الدقة
        
        # 1. حالة الدقة العالية (محاكاة إيجاد مصدر موثوق)
        if width > 1000 and height > 1000:
            result_status = "trueFact"
            result_message = f"البحث العكسي وجد الصورة منشورة في سياق إخباري رسمي يعود لعام 2021. دقة الصورة: ({width}x{height})."
            
        # 2. حالة الدقة المنخفضة جداً (محاكاة إيجاد سياق مضلل)
        elif width < 500 or height < 500:
            result_status = "falseFact"
            result_message = f"تحذير: الصورة ذات دقة منخفضة ({width}x{height}). البحث العكسي وجدها متداولة بكثافة في سياقات مختلفة ومضللة، مما يشير إلى التلاعب."
            
        # 3. المنطقة الرمادية (محاكاة نتيجة متضاربة)
        else:
            result_status = "unverified"
            result_message = f"البحث العكسي جارٍ. تم العثور على نتائج متضاربة للصورة (دقة: {width}x{height}). لا يمكن تأكيد المصداقية حالياً."


        return jsonify({
            "status": result_status, 
            "message": result_message,
            "image_size": f"{width}x{height}",
            "sourceText": "صورة تم إرسالها للتحقق.",
        }), 200

    except Exception as e:
        return jsonify({"error": f"حدث خطأ أثناء معالجة الصورة: {str(e)}"}), 500


if __name__ == '__main__':
    print("--- خادم ميزان جاهز للعمل ---")
    app.run(host='0.0.0.0', port=5000, debug=True)
