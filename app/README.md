# Semcomp 2024 Hackathon - AcadArena Communication App

This project is a Flutter-based mobile application developed for the **Semcomp 2024 Hackathon**, where **B1ld** was the sponsor. The app addresses a key problem faced by **AcadArena** (a branch of B1ld) moderators and **Wild Rift E-sports** players, particularly focusing on the integration and efficiency of communication for tournament notifications and participation management.

## Problem Statement

The main issue this application aims to solve is the **lack of streamlined communication** between AcadArena moderators and Wild Rift mobile players. Prior to this solution, moderators had to use multiple platforms such as WhatsApp, email, Discord, and ChallengerMode, leading to inefficiencies and confusion for both the moderators and the players.

## Solution

The app is designed to centralize communication between moderators and players by integrating information from **ChallengerMode** (an e-sports management platform) and the **AcadArena database**. Key features include:

- **Notifications and Alerts**: Automatically sends important notifications about tournaments, games, and other events to players and moderators.
  - These notifications are interactive and can include action buttons, such as confirming participation.
- **Discord Bot Integration**: A Discord bot listens to commands from moderators and sends messages to the respective teams. Players can view these notifications and messages directly in the app.
- **Tournament Information**: The app displays up-to-date information about ongoing and upcoming tournaments, team standings, and game results.
- **Recent Notifications**: Users can see all the notifications sent in the last 24 hours, ensuring they never miss an important update.

With this app, moderators will no longer need to manage multiple communication channels. Players will also benefit from a single interface where they can get all the necessary updates without needing to learn how to use ChallengerMode or deal with invasive messages in apps like WhatsApp.

## Features

- **ChallengerMode Integration**: Automatically pulls game data and notifications from ChallengerMode.
- **AcadArena Database Integration**: Syncs with AcadArena's player and tournament database to provide real-time information.
- **Interactive Notifications**: Send and receive notifications with actionable buttons, such as confirming participation in tournaments.
- **Discord Bot**: Moderators can send messages via Discord that are relayed to the app for players to see.
- **24-Hour Notification History**: Users can view notifications from the last 24 hours directly within the app.
- **Streamlined Communication**: One platform to manage all notifications and updates, reducing reliance on multiple communication apps.

## Technology Stack

- **Flutter**: The mobile app is built using the Flutter framework, ensuring a smooth cross-platform experience on both iOS and Android.
- **Firebase/Backend**: (Optional: Add details if Firebase or any other backend solution is being used)
- **Discord API**: For integration with Discord to relay messages between moderators and teams.
- **ChallengerMode API**: To fetch and manage tournament-related data.

## Getting Started

### Prerequisites

- [Flutter](https://flutter.dev/docs/get-started/install) should be installed on your machine.
- A working setup for Firebase (if applicable).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shogoshima/acadarena_semcomp_app.git
   cd acadarena_semcomp_app
   ```

2. Install the dependencies:
   ```bash
   flutter pub get
   ```

3. Run the app on your preferred device:
   ```bash
   flutter run
   ```

### Configuration

- Set up your API keys for **ChallengerMode** and **Discord API** in the respective environment files or within the Firebase console (if applicable).
- Configure Firebase (if used) for notifications and backend services.

## How to Use

1. **Sign In**: Users can log in using their AcadArena credentials.
2. **View Notifications**: The main screen displays notifications sent in the last 24 hours.
3. **Tournament Information**: Users can access details about ongoing and upcoming tournaments.
4. **Confirm Participation**: Players receive interactive notifications with buttons to confirm their participation in upcoming matches or tournaments.
5. **Moderator Commands**: Moderators can use the Discord bot to communicate with the teams, and these messages will appear in the app.

## Contributors

- **Your Name**
- **Other Team Members**.

---

This app provides a seamless experience for both **moderators** and **players**, enhancing communication and reducing the clutter of managing multiple platforms for e-sports tournaments.
