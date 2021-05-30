import pygame
import time
import pygame.camera
from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image


pygame.init()
pygame.camera.init()

cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()

screen = pygame.display.set_mode([1300, 600])
area = pygame.Rect(700, 280, 150, 40)

smallfont = pygame.font.SysFont('Corbel',35)
buttonText = smallfont.render('Scan' , True , (255, 255, 255))
screen.fill((60,60,60))
pygame.draw.rect(screen, (255, 255, 255), [900, 50, 380, 482])

while True:
    img = cam.get_image()
    pygame.draw.rect(screen,(0,0,0),[700,280,150,40])
    screen.blit(buttonText, (744,288))
    screen.blit(img, (20, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if area.collidepoint(event.pos):
                #decode qrs here
                pygame.image.save(img, "scan.png")
                decoded = decode(Image.open("scan.png"), symbols=[ZBarSymbol.QRCODE])
                qr_dic = {}
                pygame.draw.rect(screen, (255, 255, 255), [900, 50, 380, 482])
                counter = 0
                text = ""
                for qr in decoded:
                    x = qr[2][0] # The Left position of the QR code
                    qr_dic[x] = qr[0] # The Data stored in the QR code

                for qr in sorted(qr_dic.keys()):
                    text = qr_dic[qr].decode("utf-8")
                    print(text)
                    qrText = smallfont.render(text, True, (0, 0, 0))
                    screen.blit(qrText, (910, 60+counter*40))
                    counter += 1

    pygame.display.update()
