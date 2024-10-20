import 'package:acadarena_semcomp_app/firebase_options.dart';
import 'package:acadarena_semcomp_app/pages/notification_page.dart';
import 'package:acadarena_semcomp_app/widgets/custom_notification.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';
import 'package:acadarena_semcomp_app/pages/home_page.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:acadarena_semcomp_app/pages/dashboard_page.dart';

final navigatorKey = GlobalKey<NavigatorState>();
FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin =
    FlutterLocalNotificationsPlugin();

Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // Handle background messages here
  print('Handling a background messageeeeee: ${message.messageId}');

  showCustomNotification(message.notification?.title,
      message.notification?.body, message.data['confirmation']);
}

Future<void> createNotificationChannel() async {
  const AndroidNotificationChannel channel = AndroidNotificationChannel(
    'default_channel_id', // The same ID used in the AndroidManifest.xml
    'Default Notifications', // Name of the channel
    description:
        'This is the default notification channel for the app.', // Description for the channel
    importance: Importance.max, // Importance level (max ensures visibility)
  );

  // Ensure the channel is created
  await flutterLocalNotificationsPlugin
      .resolvePlatformSpecificImplementation<
          AndroidFlutterLocalNotificationsPlugin>()
      ?.createNotificationChannel(channel);
}

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  var initializationSettingsAndroid =
      const AndroidInitializationSettings('@mipmap/ic_launcher');
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

  var initializationSettings = InitializationSettings(
    android: initializationSettingsAndroid,
  );

  // Now create the notification channel
  await createNotificationChannel();

  await flutterLocalNotificationsPlugin.initialize(
    initializationSettings,
    onDidReceiveNotificationResponse: (NotificationResponse response) {
      print("Notification received: ${response.id}");
    },
  );

  // // Handle foreground notifications manually
  // FirebaseMessaging.onMessage.listen((RemoteMessage message) {
  //   print('Handling foreground message: ${message.messageId}');

  //   showCustomNotification(
  //     message.notification?.title,
  //     message.notification?.body,
  //     message.data['confirmation'],
  //   );
  // });

  // Set up background message handler
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);

  // Get the FCM token
  // FirebaseMessaging messaging = FirebaseMessaging.instance;
  // String? token = await messaging.getToken();
  // print("FCM Token: $token"); // Print the token in the console

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        debugShowCheckedModeBanner: false,
        home: HomePage(),
        navigatorKey: navigatorKey,
        routes: {
          '/notification_screen': (context) => const NotificationPage(),
          '/dashboard_screen': (context) => DashboardPage(),
        });
  }
}
