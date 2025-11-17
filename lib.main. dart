
// ملف: lib/main.dart

import 'package:flutter/material.dart';
// 1. استيراد شاشة النتائج التي أنشأناها للتو
import 'results_screen.dart'; 

void main() {
  runApp(const MeezanApp());
}

// 1. تعريف التطبيق (App Definition)
class MeezanApp extends StatelessWidget {
  const MeezanApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      locale: const Locale('ar', 'SA'),
      supportedLocales: const [
        Locale('ar', 'SA'),
      ],
      // يفضل ترك هذا فارغاً أو استخدام delegate للتحقق من اللغة
      localizationsDelegates: const [
        // ...
      ],
      title: 'ميزان - للتحقق من الحقائق',
      theme: ThemeData(
        primaryColor: Colors.teal,
        colorScheme: ColorScheme.fromSwatch(
          primarySwatch: Colors.teal,
          brightness: Brightness.light,
        ),
        fontFamily: 'Roboto', 
        useMaterial3: true,
        appBarTheme: const AppBarTheme(
          color: Colors.teal,
          foregroundColor: Colors.white,
        ),
      ),
      home: const HomeScreen(), 
      debugShowCheckedModeBanner: false,
    );
  }
}

// 2. تعريف الشاشة الرئيسية كـ Stateful (لتخزين النص المدخل)
class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // للتحكم في حقل النص وتخزين قيمته
  final TextEditingController _textController = TextEditingController();

  // دالة الانتقال إلى شاشة النتائج
  void _navigateToResults() {
    // ⚠️ هذا مثال على كيفية تمرير البيانات
    // سنستخدم قيمة اختبارية مؤقتة (FalseFact) حتى يتم بناء الواجهة الخلفية
    
    // قيمة النص المدخل من قبل المستخدم
    final String inputText = _textController.text.trim().isEmpty ? 
                             'تم إرسال نص تجريبي فارغ.' : 
                             _textController.text;

    // حالة اختبارية مؤقتة (لتجربة شاشة النتائج)
    final FactCheckStatus testStatus = FactCheckStatus.falseFact; 

    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => ResultsScreen(
          status: testStatus,
          sourceText: inputText,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('ميزان', style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            const Text(
              'أدخل النص أو الرابط للتحقق',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.teal),
              textAlign: TextAlign.right,
            ),
            const SizedBox(height: 10),

            // حقل إدخال النص الرئيسي
            TextField(
              controller: _textController, // ربط الـ Controller
              maxLines: 8,
              textAlign: TextAlign.right,
              decoration: InputDecoration(
                hintText: 'الصق الخبر أو الرابط هنا...',
                hintTextDirection: TextDirection.rtl,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(15.0),
                ),
                filled: true,
                fillColor: Colors.grey[100],
              ),
            ),
            const SizedBox(height: 20),

            // زر التحقق من النص
            ElevatedButton.icon(
              onPressed: _navigateToResults, // استدعاء دالة الانتقال
              icon: const Icon(Icons.search, size: 24),
              label: const Text(
                'تحقق من النص',
                style: TextStyle(fontSize: 18),
              ),
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.teal,
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 15),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0),
                ),
              ),
            ),
            const SizedBox(height: 30),
            
            const Center(
              child: Text(
                'أو تحقق من صورة',
                style: TextStyle(fontSize: 16, color: Colors.grey),
              ),
            ),
            const SizedBox(height: 20),

            // زر التحقق من الصور (Reverse Image Search)
            OutlinedButton.icon(
              onPressed: () {
                // TODO: سيتم إضافة منطق التقاط/اختيار الصورة هنا لاحقاً
                print('البحث العكسي عن الصورة - قريباً');
              },
              icon: const Icon(Icons.photo_library, size: 24, color: Colors.teal),
              label: const Text(
                'البحث العكسي عن صورة',
                style: TextStyle(fontSize: 18, color: Colors.teal),
              ),
              style: OutlinedButton.styleFrom(
                padding: const EdgeInsets.symmetric(vertical: 15),
                side: const BorderSide(color: Colors.teal, width: 2),
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
