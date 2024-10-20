import 'package:flutter/material.dart';

class DashboardState extends ChangeNotifier {}

class DashboardPage extends StatefulWidget {
  const DashboardPage({super.key});

  @override
  State<DashboardPage> createState() => _DashboardPageState();
}

class _DashboardPageState extends State<DashboardPage> {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: const Color(0xFF1A1D2C), // Background color from image
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          title: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Image.asset(
                'assets/logo.png', // Caminho da imagem no projeto
                width: 100, // Defina a largura da imagem
                height: 100, // Defina a altura da imagem
              ),
              ElevatedButton(
                  onPressed: () {},
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF6F72A9), // Discord button color
                  ),
                  child: const Text(
                    "Discord official",
                    style: TextStyle(
                      color: Colors.white,
                    ),
                  )),
            ],
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.all(20),
          child: SingleChildScrollView(
            child: SizedBox(
              width: double.infinity,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Greeting Section
                  Row(
                    children: [
                      const Text(
                        'Olá Gabriel',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 28,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(width: 10),
                      Image.asset(
                        'assets/caaso.png', // Caminho da imagem no projeto
                        width: 30, // Defina a largura da imagem
                        height: 30, // Defina a altura da imagem
                      ),
                    ],
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Suas Notificações',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 10),
                  // Notification Section
                  Container(
                    padding: const EdgeInsets.all(15),
                    decoration: BoxDecoration(
                      color: const Color(0xFF2B2E3D),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Row(
                      children: [
                        // First row with name, icon, and time
                        Expanded(
                          // Allow Row to take full width
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Row(
                                children: [
                                  const Text(
                                    'Pedro_mod',
                                    style: TextStyle(
                                      color: Colors.white,
                                      fontSize: 16,
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                  const SizedBox(width: 5),
                                  Image.asset(
                                    'assets/discord.png', // Caminho da imagem no projeto
                                    width: 20, // Defina a largura da imagem
                                    height: 20, // Defina a altura da imagem
                                  ),
                                  const SizedBox(width: 5),
                                  const Text(
                                    '20:30',
                                    style: TextStyle(
                                      color: Colors.white70,
                                      fontSize: 16,
                                    ),
                                  ),
                                ],
                              ),
                              const SizedBox(height: 5),
                              // Second line for the rest of the message
                              const Text(
                                'Galera, o campeonato irá atrasar em 15 minutos. Fiquem ligados!',
                                style: TextStyle(
                                    color: Colors.white, fontSize: 16),
                                softWrap: true, // Ensure the text wraps
                                overflow: TextOverflow
                                    .visible, // Allows the text to be fully visible
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),

                  const SizedBox(height: 20),
                  // Próximos Jogos Section
                  const Text(
                    'Seus Próximos Jogos',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 10),
                  // Game List
                  GameCard(
                    team1: 'Caaso Hogs',
                    team2: 'Ufscar E-sports',
                    time: 'Jogo Confirmado',
                    date: 'Sat, Nov 26, 2024',
                    onTap: () {
                      _showGameDetails(context, 'Caaso Hogs', 'Ufscar E-sports',
                          '26 de Novembro', '20:00');
                    },
                  ),
                  GameCard(
                    team1: 'Caaso Hogs',
                    team2: 'UFSCAR E-sports',
                    time: 'Jogo Confirmado',
                    date: 'Sat, Nov 30, 2024',
                    onTap: () {
                      _showGameDetails(context, 'Caaso Hogs', 'Ufscar E-sports',
                          '30 de Novembro', '20:00');
                    },
                  ),
                  GameCard(
                    team1: 'Caaso Hogs',
                    team2: 'UFSCAR E-sports',
                    time: 'Jogo Confirmado',
                    date: 'Sat, Dec 5, 2023',
                    onTap: () {
                      _showGameDetails(context, 'Caaso Hogs', 'Ufscar E-sports',
                          '5 de Dezembro', '20:00');
                    },
                  ),
                  const SizedBox(height: 20),
                  // Meus Torneios Section
                  const Text(
                    'Meus torneios AcadArena',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 10),
                  TournamentCard(
                    tournamentName: 'Campeonato Wild Rift',
                    date: 'Fri, August 25, 2023',
                    status: 'A confirmar',
                    onTap: () {
                      _showTournamentDetails(context); // Show the modal on tap
                    },
                  ),
                  TournamentCard(
                    tournamentName: 'Campeonato LoLcuras',
                    date: 'Fri, August 25, 2023',
                    status: 'Pronto',
                    onTap: () {
                      _showTournamentDetails(context); // Show the modal on tap
                    },
                  ),
                  TournamentCard(
                    tournamentName: 'Campeonato Clash Royale',
                    date: 'Fri, August 25, 2023',
                    status: 'A confirmar',
                    onTap: () {
                      _showTournamentDetails(context); // Show the modal on tap
                    },
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}

// Custom widget for Game Card
class GameCard extends StatelessWidget {
  final String team1;
  final String team2;
  final String date;
  final String time;
  final VoidCallback onTap; // Add onTap function

  const GameCard({super.key, 
    required this.team1,
    required this.team2,
    required this.date,
    required this.time,
    required this.onTap, // Pass the onTap function
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap, // Trigger the modal on tap
      child: Card(
        color: const Color(0xFF2B2E3D),
        margin: const EdgeInsets.symmetric(vertical: 10),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        child: Padding(
          padding: const EdgeInsets.all(15),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  // Team 1 with Icon
                  Row(
                    children: [
                      Text(
                        team1,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(width: 5), // Add space between text and icon
                      Image.asset(
                        'assets/caaso.png', // Caminho da imagem no projeto
                        width: 20, // Defina a largura da imagem
                        height: 20, // Defina a altura da imagem
                      )
                    ],
                  ),

                  // Versus symbol
                  const Text(
                    ' X ',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),

                  // Team 2 with Icon
                  Row(
                    children: [
                      Text(
                        team2,
                        style: const TextStyle(
                          color: Colors.white,
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(width: 5), // Add space between text and icon
                      Image.asset(
                        'assets/ufscar.png', // Caminho da imagem no projeto
                        width: 20, // Defina a largura da imagem
                        height: 20, // Defina a altura da imagem
                      )
                    ],
                  ),
                ],
              ),
              const SizedBox(height: 10),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Text(
                    date,
                    style: const TextStyle(color: Colors.white70, fontSize: 16),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                    decoration: BoxDecoration(
                      color:
                          time == 'Jogo Confirmado' ? Colors.green : Colors.red,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Text(
                      time,
                      style: const TextStyle(
                          color: Colors.white,
                          fontSize: 13,
                          fontWeight: FontWeight.bold),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}

// Custom widget for Tournament Card
class TournamentCard extends StatelessWidget {
  final String tournamentName;
  final String date;
  final String status;
  final VoidCallback onTap; // Accept onTap function

  const TournamentCard({super.key, 
    required this.tournamentName,
    required this.date,
    required this.status,
    required this.onTap, // Pass the onTap function
  });

  @override
  Widget build(BuildContext context) {
    return InkWell(
      onTap: onTap, // Trigger modal on tap
      child: Card(
        color: const Color(0xFF2B2E3D),
        margin: const EdgeInsets.symmetric(vertical: 10),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(12),
        ),
        child: Padding(
          padding: const EdgeInsets.all(15),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    tournamentName,
                    style: const TextStyle(color: Colors.white, fontSize: 18),
                  ),
                  const SizedBox(height: 5),
                  Text(
                    date,
                    style: const TextStyle(color: Colors.white70, fontSize: 16),
                  ),
                ],
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                decoration: BoxDecoration(
                  color: status == 'Pronto' ? Colors.green : Colors.red,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(
                    color: status == 'Pronto' ? Colors.green : Colors.red,
                    width: 1,
                  ),
                ),
                child: Text(
                  status,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

void _showTournamentDetails(BuildContext context) {
  showModalBottomSheet(
    context: context,
    backgroundColor:
        const Color(0xFF1A1D2C), // Background color similar to the design
    shape: const RoundedRectangleBorder(
      borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
    ),
    isScrollControlled: true, // Allow the modal to be scrollable if needed
    builder: (BuildContext context) {
      return FractionallySizedBox(
        heightFactor:
            0.80, // Set this to a higher value if you want a taller modal
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Image and Title
                SizedBox(
                  height: 150,
                  width: double.infinity,
                  child: Image.asset(
                    'assets/sample_image.png', // Path to your image asset
                    fit: BoxFit.cover,
                  ),
                ),
                const SizedBox(height: 20),
                const Row(
                  children: [
                    CircleAvatar(
                      radius: 20,
                      backgroundColor: Colors.white,
                      child: Icon(Icons.sports_esports, color: Colors.blue),
                    ),
                    SizedBox(width: 10),
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          'October Aces: MLBB',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 20,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                        SizedBox(height: 5),
                        Text(
                          'Em cerca de 1 hora    Outubro 20, 03:00',
                          style: TextStyle(
                            color: Colors.white70,
                            fontSize: 16,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
                const SizedBox(height: 10),
                const Text(
                  'Ver mais no challenger mode',
                  style: TextStyle(
                    color: Colors.blue,
                    fontSize: 16,
                    decoration: TextDecoration.underline,
                  ),
                ),
                const SizedBox(height: 20),
                const Text(
                  'Formato',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 10),
                GridView.count(
                  crossAxisCount: 2,
                  shrinkWrap: true, // Ensures GridView takes only needed space
                  physics:
                      const NeverScrollableScrollPhysics(), // Disable scrolling inside GridView
                  childAspectRatio: 1.7,
                  children: [
                    _buildInfoCard('Jogo', 'league of legends wild rift',
                        Icons.videogame_asset),
                    _buildInfoCard('Período de check-in', '20 Outubro, 14:00',
                        Icons.event),
                    _buildInfoCard('Tamanho da equipe', '5v5', Icons.people),
                    _buildInfoCard('Requisitos de participação',
                        'Apenas assinantes', Icons.check),
                    _buildInfoCard(
                        'Formato', 'Eliminação simples', Icons.sports),
                    _buildInfoCard('Inscritos', '61', Icons.person),
                  ],
                ),
              ],
            ),
          ),
        ),
      );
    },
  );
}

Widget _buildInfoCard(String title, String content, IconData icon) {
  return Card(
    color: const Color(0xFF2B2E3D),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
    child: Padding(
      padding: const EdgeInsets.all(10.0),
      child: Row(
        crossAxisAlignment:
            CrossAxisAlignment.start, // Ensure content aligns at the top
        children: [
          Icon(icon, color: Colors.white),
          const SizedBox(width: 10),
          Expanded(
            // This will ensure the content expands horizontally
            child: Column(
              crossAxisAlignment:
                  CrossAxisAlignment.start, // Align text to the left
              children: [
                Text(
                  title,
                  style: const TextStyle(color: Colors.white, fontSize: 16),
                ),
                const SizedBox(height: 5),
                Text(
                  content,
                  style: const TextStyle(color: Colors.white70, fontSize: 14),
                ),
              ],
            ),
          ),
        ],
      ),
    ),
  );
}

void _showGameDetails(BuildContext context, String team1, String team2,
    String date, String time) {
  showModalBottomSheet(
    context: context,
    backgroundColor: const Color(0xFF1A1D2C),
    shape: const RoundedRectangleBorder(
      borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
    ),
    isScrollControlled: true,
    builder: (BuildContext context) {
      return FractionallySizedBox(
        heightFactor: 0.80, // Set modal height
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Game image at the top
                SizedBox(
                  height: 150,
                  width: double.infinity,
                  child: Image.asset(
                    'assets/sample_image.png', // Replace with actual image asset path
                    fit: BoxFit.cover,
                  ),
                ),
                const SizedBox(height: 20),

                // Teams section
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      '$team1 🆚 $team2',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 20,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 20),

                // Date and Time section
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    _buildInfoBox('Data', date, Icons.calendar_today),
                    _buildInfoBox('Horário', time, Icons.access_time),
                  ],
                ),
                const SizedBox(height: 20),

                // Team Members section
                const Text(
                  'Sua equipe',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 10),

                // List of team members
                _buildTeamMember('CarvalK#2006', 'UfscarE#30064777'),
                _buildTeamMember('CarvalK#2006', 'UfscarE#30064777'),
                _buildTeamMember('CarvalK#2006', 'UfscarE#30064777'),
                _buildTeamMember('CarvalK#2006', 'UfscarE#30064777'),
              ],
            ),
          ),
        ),
      );
    },
  );
}

// Helper widget to build the Info Box for Date and Time
Widget _buildInfoBox(String label, String value, IconData icon) {
  return Card(
    color: const Color(0xFF2B2E3D),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
    child: Padding(
      padding: const EdgeInsets.all(15.0),
      child: Row(
        children: [
          Icon(icon, color: Colors.white),
          const SizedBox(width: 10),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                label,
                style: const TextStyle(color: Colors.white70, fontSize: 14),
              ),
              Text(
                value,
                style: const TextStyle(color: Colors.white, fontSize: 16),
              ),
            ],
          ),
        ],
      ),
    ),
  );
}

// Helper widget to build each team member row
Widget _buildTeamMember(String memberName, String accountInfo) {
  return Card(
    color: const Color(0xFF2B2E3D),
    shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(12),
    ),
    child: ListTile(
      leading: const CircleAvatar(
        backgroundImage:
            AssetImage('assets/avatar.jpg'), // Replace with actual avatar path
      ),
      title: Text(memberName, style: const TextStyle(color: Colors.white)),
      subtitle: Text('Jogando como $accountInfo',
          style: const TextStyle(color: Colors.white70)),
    ),
  );
}
