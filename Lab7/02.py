import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((300,200))
pygame.display.set_caption("Music Player")
musics = ["C:/Users/ernad/Desktop/PP2/Lab7/musics/Breathe.mp3", "C:/Users/ernad/Desktop/PP2/Lab7/musics/Counting_Stars.mp3", "C:/Users/ernad/Desktop/PP2/Lab7/musics/Don_t_Be_So_Shy.mp3"]
stop = False
current_track = 1
pygame.mixer.music.load(musics[current_track])

while True:
    screen.fill((255, 255, 254))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                stop = not stop
                if stop:
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.stop()
            if event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(musics)
                pygame.mixer.music.load(musics[current_track])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(musics)
                pygame.mixer.music.load(musics[current_track])
                pygame.mixer.music.play()