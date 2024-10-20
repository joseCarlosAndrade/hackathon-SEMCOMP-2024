class Notification {
  final String title;
  final String body;
  final String confirmation;

  Notification(
      {required this.title, required this.body, required this.confirmation});

  factory Notification.fromJson(Map<String, dynamic> json) {
    return Notification(
      title: json['title'],
      body: json['body'],
      confirmation: json['confirmation'],
    );
  }
}
