#Создай собственный Шутер!

from pygame import *
from random import *
from random import random





mixer.init()
window = display.set_mode((700,500))
display.set_caption('Space shooter+')
background = transform.scale(image.load('galaxy.png'), (700,500))
Clock = time.Clock()
FPS = 60
game = True
finish = False
mixer.music.load('Knock.ogg')
mixer.music.play()
mixer.music.set_volume(2)
time_tick = Clock.tick()





font.init()
font1 = font.SysFont('Haettenschweiler', 36)

kick = mixer.Sound('fire.ogg')
hit = mixer.Sound('hit.ogg')
winner = mixer.Sound('winner.ogg')
loserok = mixer.Sound('Loserok.ogg')
skip = mixer.Sound('Skipped.ogg')
Heal_sound = mixer.Sound('Heal.ogg')
round2 = mixer.Sound('2.ogg')


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 615:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        if keys[K_LSHIFT] and self.speed <= 4:
            self.speed += 3
        if keys[K_TAB] and self.speed >= 7:
            self.speed -= 3





    def fire(self):
        kick.set_volume(0.5)
        kick.play()
        bullet  = Bullet('bullet.png', self.rect.x + 27 , self.rect.y, 15 ,25 ,25 )
        bullets.add(bullet)
lost = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < -50:
            self.kill()











class Boom(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__(player_image, player_x, player_y, player_speed, width, height)
        self.tick = 0
    def update(self):
        self.tick += 1
        if self.tick == 60:
            self.kill()



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 505:
            skip.set_volume(0.5)
            skip.play()
            self.rect.y = -10
            self.rect.x = randint(0, 620)
            lost = lost + 1 
    def Kaboom(self):
        Kaboom = Boom('Boom.png', self.rect.x, self.rect.y  , 0, 100, 100)
        kabooms.add(Kaboom)

class asteroid(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 505:
            self.rect.y = -10
            self.rect.x = randint(0, 620)

class Medkit(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 505:
            self.rect.y = -10
            self.rect.x = randint(0, 620)




rand_ufos = ['ufo.png', 'ufo1.png']
shuffle(rand_ufos)
rand_comet = ['comet.png','Comet1.png']
shuffle(rand_comet)

            


player = Player('rocket.png', 65, 425, 4, 80, 80)
choise_ufo = choice(rand_ufos)
choise_comet = choice(rand_comet)

kabooms = sprite.Group()            
ufos = sprite.Group()
for i in range (5):
    ufos.add(Enemy(choise_ufo, randint(0,620), randint(-100, -50), random() + 2, 75, 50))

Comet = sprite.Group()    
Comet.add(asteroid(choise_comet, randint(0,620), randint(-100, -50), random() + 1, 150, 100))

Souls = sprite.Group()
Souls.add(Medkit('soul.png', randint(0,620), randint(-100, -50), random() + 1, 50, 50))





s = 0

bullets = sprite.Group()
booms = sprite.Group()

killed = 0

health = randint(5,10)

kills_need = randint(60, 75)

time_since_start = 0





while game:

    timer = time_since_start / 60
    round_timer = round(timer)
    window.blit(background,(0,0))




    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()


 



    if finish != True:
        
        window.blit(background,(0,0))
        text_lose = font1.render('Пропущено:' + str(lost), 1, (31, 109, 107))
        window.blit(text_lose, (0,25))       
        text_win = font1.render('Сбито:' + str(killed), 1, (74, 208, 204))
        window.blit(text_win,(0,0))
        text_hp = font1.render('Здоровье:' + str(health), 1, (171, 57, 57))
        window.blit(text_hp, (0,50))
        text_win = font1.render('Требуется Сбить:' + str(kills_need), 1, (74, 208, 204))
        window.blit(text_win,(450,0))
        text_time = font1.render('Время:' + str(round_timer) + ' с', 1, (255, 255, 0))
        window.blit(text_time,(550,25))
        


        kabooms.update()
        kabooms.draw(window)
        player.reset()
        player.update()
        ufos.update()
        ufos.draw(window)
        Comet.update()
        Comet.draw(window)
        bullets.draw(window)
        bullets.update()
        Souls.draw(window)
        Souls.update()
        time_since_start += 1





    if finish == True:
        mixer.music.stop()
        text_time = font1.render('Время:' + str(round_timer) + ' с', 1, (255, 255, 255))
        window.blit(text_time,(300,275))











    

    



    sprites_list1 = sprite.spritecollide(player, ufos, True)
    sprites_list2 = sprite.spritecollide(player, Comet, True)
    sprites_Heal = sprite.spritecollide(player, Souls, True)

    sprites_list = sprite.groupcollide(ufos, bullets, False, True)
    sprites_comet = sprite.groupcollide(Comet, bullets, False, True)
    sprites_heal0 = sprite.groupcollide(Souls, bullets, True, True)
    sprites_heal_res = sprite.groupcollide(Souls, Comet, True, False)



    for i in sprites_list:
        i.Kaboom()
        i.rect.y = -100
        i.rect.x = randint(0, 620)
        killed += 1 
        hit.play()


    if killed >= kills_need:
        winner.set_volume(0.5)
        winner.play()
        finish = True
        text_viigrish = font1.render('YOU WIN!', 1, (0, 255, 0))
        background = transform.scale(image.load('Win.png'), (700,500))
        window.blit(text_viigrish, (300,225)) 

    if sprites_heal_res:
        Souls.add(Medkit('soul.png', randint(0,620), randint(-100, -50), random() + 1, 50, 50))



    if lost == 25:
        loserok.set_volume(0.1)
        loserok.play()
        finish = True
        text_losted = font1.render('YOU LOSE!', 1, (255, 0, 0))
        background = transform.scale(image.load('Lose.png'), (700,500))
        window.blit(text_losted, (300,225))     

    if sprites_list1:
        hit.play()
        health -= 1
        ufos.add(Enemy(choise_ufo, randint(0,620), randint(-100, -50), random() + 2, 75, 50))
        killed += 1

    if sprites_list2:
        hit.play()
        health -= 3
        Comet.add(asteroid('comet.png', randint(0,620), randint(-100, -50), random() + 1, 150, 100))
    



    if health <= 0:
        loserok.set_volume(0.1)
        loserok.play()
        finish = True
        text_losted = font1.render('YOU LOSE!', 1, (255, 0, 0))
        background = transform.scale(image.load('Lose.png'), (700,500))
        window.blit(text_losted, (300,225))  

    if sprites_Heal:
        health += 1
        Heal_sound.play()
        Souls.add(Medkit('soul.png', randint(0,620), randint(-100, -50), random() + 1, 50, 50))


    if sprites_heal0:
        Souls.add(Medkit('soul.png', randint(0,620), randint(-100, -50), random() + 1, 50, 50))
        hit.play()

    if killed == 50:
        killed += 1
        for i in range (3):
            ufos.add(Enemy(choise_ufo, randint(0,620), randint(-100, -50), random() + 2, 75, 50))
        Souls.add(Medkit('soul.png', randint(0,620), randint(-100, -50), random() + 1, 50, 50))
        round2.set_volume(5)
        round2.play()
        health += 5
        lost -= 5
        
    if killed >= 50:
        Text_round2 = font1.render('ROUND 2!', 1, (255, 0, 0))
        window.blit(Text_round2, (300,450))  

    if finish == True:
        Text_round2 = font1.render('ROUND 2!', 1, (0, 0, 0))
        window.blit(Text_round2, (300,450))  






    






   



    display.update()
    Clock.tick(FPS)



    