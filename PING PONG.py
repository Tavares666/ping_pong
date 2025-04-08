import pygame, sys, random, time

# Inicialização do Pygame
pygame.init()

# Música
pygame.mixer.music.set_volume(0.5)
musica_fundo = pygame.mixer.music.load(r'C:\Users\luana\Downloads\ping pong\smw_course_clear.wav')
pygame.mixer.music.play(-1)
barulho_bolo_raquete = pygame.mixer.Sound(r'C:\Users\luana\Downloads\ping pong\smw_coin.wav')


# Configurações básicas
largura, altura = 1200, 700
fonte = pygame.font.SysFont("ADlaM Display", int(largura / 8))
fontePequena = pygame.font.SysFont("ADlaM Display", int(largura / 40))
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Ping Pong!")
relogio = pygame.time.Clock()

# Configuração das raquetes
raioRaquete = 50
larguraCabo = 10
alturaCabo = 50
raqueteJogador1 = pygame.Rect(0, 0, raioRaquete * 2, raioRaquete * 2)
raqueteJogador1.center = (largura - 100, altura / 2)

raqueteJogador2 = pygame.Rect(0, 0, raioRaquete * 2, raioRaquete * 2)
raqueteJogador2.center = (100, altura / 2)

placarJogador1, placarJogador2 = 0, 0
pontos_vitoria = 20  # Pontos necessários para vencer

# Configuração da bola
raioBola = 16
bola = pygame.Rect(0, 0, raioBola * 2, raioBola * 2)
bola.center = (largura / 2, altura / 2)

velBolaX, velBolaY = 4, 4

# Cores
verde = ('#3B0069')
branco = (255, 255, 255)
vermelho = (255, 102, 102)
azul = (173, 216, 230)
marrom = (139, 69, 19)
corBola = (255, 165, 0)
roxoclaro = (186, 85, 211)
roxo = (128, 0, 128)

# Função para exibir a tela inicial
def telaInicial():
    while True:
        tela.fill(roxoclaro)
        

        # Título do jogo
        titulo = fonte.render("PING PONG", True, branco)
        tela.blit(titulo, (largura / 2 - titulo.get_width() / 2, altura / 3))

        # Instruções
        instrucoes = fontePequena.render('Clique em qualquer tecla!', True, branco)
        tela.blit(instrucoes, (largura / 2 - instrucoes.get_width() / 2, altura / 2))

        # Créditos (opcional)
        creditos = fontePequena.render('Desenvolvido por Luana e Camila', True, branco)
        tela.blit(creditos, (largura / 2 - creditos.get_width() / 2, altura - 50))

        pygame.display.update()

        # Aguarda o jogador pressionar uma tecla para começar
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                return  # Sai da função e inicia o jogo

# Função para exibir a tela de vitória
def exibirVencedor(vencedor):
    while True:
        tela.fill(roxoclaro)
        

        # Texto de vitória
        texto_vencedor = fonte.render(f"{vencedor} venceu!", True, branco)
        tela.blit(texto_vencedor, (largura / 2 - texto_vencedor.get_width() / 2, altura / 3))

        # Instruções para sair
        instrucoes = fontePequena.render("Pressione qualquer tecla para sair", True, branco)
        tela.blit(instrucoes, (largura / 2 - instrucoes.get_width() / 2, altura / 2))

        pygame.display.update()

        # Aguarda o jogador pressionar uma tecla para sair
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

# Inicializa o tempo inicial antes do loop principal
tempo_inicial = time.time()

# Loop principal do jogo
telaInicial()

while True:
    teclas = pygame.key.get_pressed()

    # Movimentação da raquete do Jogador 1
    if teclas[pygame.K_UP] and raqueteJogador1.top > 0:
        raqueteJogador1.top -= 5
    if teclas[pygame.K_DOWN] and raqueteJogador1.bottom < altura:
        raqueteJogador1.bottom += 5

    # Movimentação da raquete do Jogador 2
    if teclas[pygame.K_w] and raqueteJogador2.top > 0:
        raqueteJogador2.top -= 5
    if teclas[pygame.K_s] and raqueteJogador2.bottom < altura:
        raqueteJogador2.bottom += 5

    # Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica da bola
    if bola.top <= 0 or bola.bottom >= altura:
        velBolaY *= -1
    if bola.left <= 0:
        placarJogador1 += 1
        bola.center = (largura / 2, altura / 2)
        velBolaX, velBolaY = random.choice([-3, 3]), random.choice([-3, 3])
    if bola.right >= largura:
        placarJogador2 += 1
        bola.center = (largura / 2, altura / 2)
        velBolaX, velBolaY = random.choice([-3, 3]), random.choice([-3, 3])

    # Verificar vencedor
    if placarJogador1 >= pontos_vitoria:
        exibirVencedor("Jogador 1")

    if placarJogador2 >= pontos_vitoria:
        exibirVencedor("Jogador 2")
       
    # Ajuste de velocidade da bola
    velBolaX += 0.1 if velBolaX > 0 else -0.1
    velBolaY += 0.1 if velBolaY > 0 else -0.1

    # Colisão da bola com as raquetes
    if raqueteJogador1.colliderect(bola):
        velBolaX *= -1
        velBolaY *= -1
        barulho_bolo_raquete.play()
    if raqueteJogador2.colliderect(bola):
        velBolaX *= -1
        velBolaY *= -1
        barulho_bolo_raquete.play()

    # Movimento da bola
    bola.x += velBolaX
    bola.y += velBolaY

    # Desenho da tela
    tela.fill(roxoclaro)

    # Desenhar linha central (rede)
    pygame.draw.line(tela, roxo, (largura / 2, 0), (largura / 2, altura), 5)

    # Desenhar os cabos das raquetes
    caboJogador1 = pygame.Rect(raqueteJogador1.centerx - larguraCabo // 2, raqueteJogador1.centery + raioRaquete, larguraCabo, alturaCabo)
    caboJogador2 = pygame.Rect(raqueteJogador2.centerx - larguraCabo // 2, raqueteJogador2.centery + raioRaquete, larguraCabo, alturaCabo)
    pygame.draw.rect(tela, marrom, caboJogador1)
    pygame.draw.rect(tela, marrom, caboJogador2)

    # Desenhar as raquetes
    pygame.draw.circle(tela, azul, raqueteJogador1.center, raioRaquete)
    pygame.draw.circle(tela, vermelho, raqueteJogador2.center, raioRaquete)

    # Desenhar a bola
    pygame.draw.circle(tela, corBola, bola.center, raioBola)

    # Exibir o placar
    placarJ1 = fontePequena.render(f"Jogador 1: {placarJogador1}", True, branco)
    placarJ2 = fontePequena.render(f"Jogador 2: {placarJogador2}", True, branco)

    tela.blit(placarJ1, (largura / 2 + 50, 50))
    tela.blit(placarJ2, (largura / 2 - 200, 50))

    # Calcular e exibir o tempo de jogo
    tempo = int(time.time() - tempo_inicial)
    relogiotemp = fontePequena.render(f'Tempo: {tempo}s', True, branco)
    tela.blit(relogiotemp, (20, 20))

    pygame.display.update()
    relogio.tick(60)