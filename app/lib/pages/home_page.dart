import 'package:acadarena_semcomp_app/main.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor:
          const Color(0xFF1A1A1A), // Cor de fundo azul escuro em hexadecimal
      body: Padding(
        padding: const EdgeInsets.all(16.0), // Adiciona espaçamento nas bordas
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Logotipo e texto à esquerda
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Substitua o ícone pelo Image.asset para usar a imagem do seu projeto
                    Image.asset(
                      'assets/logo.png', // Caminho da imagem no projeto
                      width: 200, // Defina a largura da imagem
                      height: 200, // Defina a altura da imagem
                    ),
                    const Text(
                      'A comunidade\ndas comunidades\ndos Gamers',
                      textAlign: TextAlign.end,
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 24,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ],
                ),
                const Spacer(),
                // Imagem à direita
                Container(
                  height: 300,
                  width: 150,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(8),
                    image: const DecorationImage(
                      image: AssetImage('assets/sample_image.png'),
                      fit: BoxFit.cover,
                    ),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 40),
            // Botão de login
            ElevatedButton(
              onPressed: () {
                // Ação do botão
                navigatorKey.currentState?.pushNamed(
                  '/dashboard_screen',
                );
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors
                    .tealAccent[700], // Nova maneira de definir a cor do botão
                padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(8),
                ),
              ),
              child: const Text(
                'Login no challengerMode',
                style: TextStyle(
                  fontSize: 16,
                  color: Colors.white,
                ),
              ),
            ),
            const SizedBox(height: 20),
            const Text(
              'Saiba mais da acad arena',
              style: TextStyle(
                color: Colors.white70,
              ),
            ),
            const SizedBox(height: 40),
            // Ícones de redes sociais
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                IconButton(
                  icon: const Icon(Icons.camera_alt),
                  color: Colors.pink,
                  onPressed: () {},
                ),
                IconButton(
                  icon: const Icon(Icons.flash_on),
                  color: Colors.orange,
                  onPressed: () {},
                ),
                IconButton(
                  icon: const Icon(Icons.message),
                  color: Colors.blue,
                  onPressed: () {},
                ),
                IconButton(
                  icon: const Icon(Icons.thumb_up),
                  color: Colors.blueAccent,
                  onPressed: () {},
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
