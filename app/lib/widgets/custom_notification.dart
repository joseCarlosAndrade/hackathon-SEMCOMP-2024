import 'dart:ui';

import 'package:acadarena_semcomp_app/main.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

Future<void> showCustomNotification(title, body, confirmation) async {
  var androidPlatformChannelSpecifics = AndroidNotificationDetails(
    'default_channel_id', // Custom channel ID
    'Custom Notifications', // Channel name
    channelDescription: 'Custom channel for notifications',
    importance: Importance.max, // Importance level of the notification
    priority: Priority.high, // Priority level for notifications
    ticker: 'ticker',
    color: const Color(0xFF1F2633),
    styleInformation: BigTextStyleInformation(
      body,
      contentTitle: "<b>$title</b>",
      summaryText: " • Discord",
      htmlFormatBigText: true, // Enable HTML formatting for big text
      htmlFormatContentTitle: true,
      htmlFormatSummaryText: true,
    ),
  );

  var platformChannelSpecifics = NotificationDetails(
    android: androidPlatformChannelSpecifics,
  );

  await flutterLocalNotificationsPlugin.show(
    0, // Notification ID
    title, // Notification title
    body, // Notification body
    platformChannelSpecifics,
    payload: confirmation,
  );
}
