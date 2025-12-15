import 'package:flutter/material.dart';

void main() {
  runApp(const MeezanApp());
}

class MeezanApp extends StatelessWidget {
  const MeezanApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Meezan Fact Checker',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final TextEditingController _controller = TextEditingController();
  String _result = '';

  void _checkFact() {
    setState(() {
      if (_controller.text.isEmpty) {
        _result = 'الرجاء إدخال نص الخبر أولاً.';
      } else {
        // هنا لاحقًا يمكن إضافة خوارزمية التحقق الحقيقية
        _result = 'تم التحقق من الخبر: جاري المعالجة...';
      }
    });

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(content: Text(_result)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Meezan Fact Checker'),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: const [
            DrawerHeader(
              decoration: BoxDecoration(color: Colors.blue),
              child: Text(
                'Meezan Fact Checker',
                style: TextStyle(color: Colors.white, fontSize: 20),
              ),
            ),
            ListTile(
              leading: Icon(Icons.info),
              title: Text('حول المشروع'),
            ),
            ListTile(
              leading: Icon(Icons.settings),
              title: Text('الإعدادات'),
            ),
          ],
        ),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            const Text(
              'أدخل الخبر للتحقق منه:',
              style: TextStyle(fontSize: 18),
            ),
            const SizedBox(height: 10),
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'اكتب الخبر هنا...',
              ),
              maxLines: 3,
            ),
            const SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: _checkFact,
              icon: const Icon(Icons.search),
              label: const Text('تحقق من الخبر'),
            ),
            const SizedBox(height: 20),
            Text(
              _result,
              style: const TextStyle(fontSize: 16, color: Colors.black87),
            ),
          ],
        ),
      ),
    );
  }
}
