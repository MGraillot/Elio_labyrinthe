import neopixel
import board
import time, random
import elio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.05, auto_write=False, pixel_order=neopixel.GRB)

# i = 0

while True:
    
#     time.sleep(0.1)

# """
#     elio.vitesseMoteur(1, 50, 1)
#     elio.vitesseMoteur(2, 50, 0)
# """

#     #print('b')
#     time.sleep(0.3)
#     elio.motorStop()
#     elio.vitesseMoteur('Droite', 50, 'Avance')
#     #print('c')
#     #motorStop()
#     #time.sleep(0.5)
#     
# """ pour faire varier la vitesse du robot de min à max
#     for i in range (100):
#         time.sleep(0.1)
# """

    

    elio.obstacleCMD.value = True
    
#     elio.vitesseMoteur('Droite', 14, 'Avance')
#     elio.vitesseMoteur('Gauche', 15, 'Avance')
#     
    if elio.obstacle(1) < 1000:
    
#         i = random.randint(0, 255)
#         j = random.randint(0, 255)
#         k = random.randint(0, 255)
#         
        pixels[0] = (255, 0, 0)
        pixels.show()
        elio.vitesseMoteur('Droite', 29, 'Avance')#14
        elio.vitesseMoteur('Gauche', 30, 'Avance')#15
        time.sleep(1.35)
        elio.motorStop()
#         time.sleep(0.20)
        elio.vitesseMoteur('Droite', 29, 'Avance')
        elio.vitesseMoteur('Gauche', 30, 'Recule')
        time.sleep(0.51)#0.83

        if elio.obstacle(1) > 500:
            pixels[0] = (255, 255, 0)
            pixels.show()
            elio.motorStop()
            time.sleep(0.20)
            elio.vitesseMoteur('Droite', 29, 'Recule')
            elio.vitesseMoteur('Gauche', 30, 'Avance')
#             elio.vitesseMoteur('Droite', 14, 'Avance')
#             elio.vitesseMoteur('Gauche', 15, 'Recule')
            time.sleep(0.55)
            
            if elio.obstacle(1) > 500:
                 pixels[0] = (0, 0, 255)
                 pixels.show()
                 elio.motorStop()
                 time.sleep(0.20)
                 elio.vitesseMoteur('Droite', 29, 'Recule')
                 elio.vitesseMoteur('Gauche', 30, 'Avance')
                 time.sleep(0.51) #0.85
                 
                 if elio.obstacle(1) > 500:
                     pixels[0] = (255, 0, 255)
                     pixels.show()
                     elio.motorStop()
                     time.sleep(0.20)
                     elio.vitesseMoteur('Droite', 29, 'Recule')
                     elio.vitesseMoteur('Gauche', 30, 'Avance')
                     time.sleep(0.51) #0.85

