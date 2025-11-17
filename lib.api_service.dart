// ملف: lib/api_service.dart

import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import 'results_screen.dart'; 

// ⚠️ يجب تغيير هذا العنوان إلى عنوان الخادم الثابت والحقيقي بعد النشر
const String _baseUrl = 'https://your-meezan-api.onrender.com'; 

class ApiService {
  
  // دالة تحويل حالة النص إلى FactCheckStatus
  FactCheckStatus _parseStatus(String statusString) {
      switch (statusString) {
        case 'trueFact':
          return FactCheckStatus.trueFact;
        case 'falseFact':
          return FactCheckStatus.falseFact;
        default:
          return FactCheckStatus.unverified;
      }
  }
  
  // 1. دالة التحقق من النص
  Future<Map<String, dynamic>> checkText(String text) async {
    final url = Uri.parse('$_baseUrl/check_text');
    
    try {
      final response = await http.post(
        url,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          'text': text,
        }),
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> jsonResponse = jsonDecode(utf8.decode(response.bodyBytes));
        
        return {
          'status': _parseStatus(jsonResponse['status']),
          'sourceText': jsonResponse['sourceText'] ?? text,
          'message': jsonResponse['message'] ?? 'لم يتم استلام رسالة من الخادم.',
        };
      } else {
        return {
          'status': FactCheckStatus.unverified,
          'sourceText': text,
          'message': 'خطأ اتصال: ${response.statusCode}',
        };
      }
    } catch (e) {
      return {
        'status': FactCheckStatus.unverified,
        'sourceText': text,
        'message': 'فشل الاتصال بالخادم. الخطأ: $e',
      };
    }
  }

  // 2. دالة التحقق من الصورة
  Future<Map<String, dynamic>> checkImage(XFile imageFile) async {
    final url = Uri.parse('$_baseUrl/check_image');
    
    try {
      var request = http.MultipartRequest('POST', url);
      
      request.files.add(await http.MultipartFile.fromPath(
        'image',
        imageFile.path,
      ));

      var streamedResponse = await request.send();
      var response = await http.Response.fromStream(streamedResponse);

      if (response.statusCode == 200) {
        final Map<String, dynamic> jsonResponse = jsonDecode(utf8.decode(response.bodyBytes));
        
        return {
          'status': _parseStatus(jsonResponse['status']),
          'sourceText': jsonResponse['sourceText'] ?? 'صورة للتحقق',
          'message': jsonResponse['message'] ?? 'نتيجة البحث العكسي.',
        };
      } else {
        return {
          'status': FactCheckStatus.unverified,
          'sourceText': 'صورة للتحقق',
          'message': 'خطأ خادم عند إرسال الصورة: ${response.statusCode}',
        };
      }
    } catch (e) {
      return {
        'status': FactCheckStatus.unverified,
        'sourceText': 'صورة للتحقق',
        'message': 'فشل في إرسال الصورة: $e',
      };
    }
  }
}
