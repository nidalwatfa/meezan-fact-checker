// ملف: lib/results_screen.dart

import 'package:flutter/material.dart';

// تعريف أنواع نتائج التحقق (لجعل الكود أكثر وضوحاً وتنظيماً)
enum FactCheckStatus {
  trueFact, // حقيقة / صحيح
  falseFact, // كاذب / مضلل
  unverified, // غير مؤكد / قيد التحقق
}

class ResultsScreen extends StatelessWidget {
  // المتغيرات التي ستستقبلها الشاشة
  final FactCheckStatus status; // حالة التحقق
  final String sourceText; // النص الذي تم التحقق منه

  const ResultsScreen({
    super.key,
    required this.status,
    required this.sourceText,
  });

  // دالة مساعدة لتحديد الألوان والنصوص بناءً على الحالة
  Map<String, dynamic> _getStatusData() {
    switch (status) {
      case FactCheckStatus.trueFact:
        return {
          'title': 'صحيح',
          'color': Colors.green,
          'icon': Icons.check_circle,
          'message': 'البيانات تشير إلى أن هذا الخبر دقيق وموثوق به.',
        };
      case FactCheckStatus.falseFact:
        return {
          'title': 'كاذب ومضلل',
          'color': Colors.red,
          'icon': Icons.cancel,
          'message': 'التحقق أظهر أن هذا الخبر غير صحيح ويحتوي على تضليل متعمد.',
        };
      case FactCheckStatus.unverified:
        return {
          'title': 'قيد التحقق',
          'color': Colors.amber,
          'icon': Icons.info,
          'message': 'لم نتمكن من التحقق من هذا الخبر بعد. يرجى مراجعة مصادر موثوقة.',
        };
    }
  }

  @override
  Widget build(BuildContext context) {
    final statusData = _getStatusData();
    
    return Scaffold(
      appBar: AppBar(
        title: const Text('نتيجة التحقق', style: TextStyle(fontWeight: FontWeight.bold)),
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            // 1. قسم حالة التحقق الرئيسية
            Container(
              padding: const EdgeInsets.all(25),
              decoration: BoxDecoration(
                color: statusData['color'].withOpacity(0.1),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: statusData['color'], width: 2),
              ),
              child: Column(
                children: [
                  Icon(
                    statusData['icon'],
                    color: statusData['color'],
                    size: 80,
                  ),
                  const SizedBox(height: 15),
                  Text(
                    statusData['title'],
                    style: TextStyle(
                      fontSize: 30,
                      fontWeight: FontWeight.w900,
                      color: statusData['color'],
                    ),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 10),
                  Text(
                    statusData['message'],
                    style: const TextStyle(fontSize: 16),
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
            const SizedBox(height: 30),

            // 2. النص الذي تم إدخاله للتحقق
            const Text(
              'النص الذي تم التحقق منه:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              textAlign: TextAlign.right,
            ),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(15),
              decoration: BoxDecoration(
                color: Colors.grey[50],
                borderRadius: BorderRadius.circular(10),
                border: Border.all(color: Colors.grey[300]!),
              ),
              child: Text(
                sourceText,
                style: const TextStyle(fontSize: 16),
                textAlign: TextAlign.right,
              ),
            ),
            const SizedBox(height: 30),

            // 3. مساحة لربط مصادر خارجية (لإضافة لاحقاً)
            const Text(
              'مصادر التحقق (سيتم إضافتها لاحقاً):',
              style: TextStyle(fontSize: 16, color: Colors.teal),
              textAlign: TextAlign.right,
            ),
            const SizedBox(height: 10),
            
            // زر العودة
            ElevatedButton.icon(
              onPressed: () {
                Navigator.pop(context); // العودة إلى الشاشة الرئيسية
              },
              icon: const Icon(Icons.arrow_forward), // سهم للخلف في اليمين (RTL)
              label: const Text('تحقق من خبر آخر'),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.grey,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 15),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
