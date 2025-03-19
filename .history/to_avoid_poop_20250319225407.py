import random
import pygame

##################################################################################################
#기본 초기화(반드시 필요)
pygame.init()

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("To avoid POOP")

#FPS
clock = pygame.time.Clock()
###################################################################################################

###1. 사용자 게임 초기화(배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)###
#배경 만들기
background = pygame.image.load("background.png")

#캐릭터 만들기
character = pygame.image.load("character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

#이동 위치
to_x = 0
character_speed = 10

#똥 만들기
poop = pygame.image.load("poop.png")
poop_size = poop.get_rect().size
poop_width = poop_size[0]
poop_height = poop_size[1]
poop_x_pos = random.randint(0, screen_width - poop_width)
poop_y_pos = 0
poop_speed = 10

# 폰트 설정 (크기 50)
font = pygame.font.Font(None, 50)

running = True
game_over = False  # 충돌 상태 변수

while running:
    dt = clock.tick(30)
    
    ###2. 이벤트 처리(키보드, 마우스 등)###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP and not game_over:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    if not game_over:
        
        # 캐릭터 위치 정의
        character_x_pos += to_x

        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        poop_y_pos += poop_speed

        if poop_y_pos > screen_height:
            poop_y_pos = 0
            poop_x_pos = random.randint(0, screen_width - poop_width)

        # 충돌 처리
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        poop_rect = poop.get_rect()
        poop_rect.left = poop_x_pos
        poop_rect.top = poop_y_pos

        if character_rect.colliderect(poop_rect):
            game_over = True  # 게임 오버 상태 설정
    
    if character_rect.colliderect(poop_rect):
        text = font.render("Ouch!", True, (255, 0, 0))  # 빨간색 글씨
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)  # 2초간 메시지를 보여줌
        running = False

    ###5. 화면에 그리기###
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(poop, (poop_x_pos, poop_y_pos))

    pygame.display.update()

#pygame 종료 처리
pygame.quit()