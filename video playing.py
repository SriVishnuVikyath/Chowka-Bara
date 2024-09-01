import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip("/home/vps26/Downloads/to-the-game.mp4")
video.preview()
pygame.quit()
pygame.display.update()
