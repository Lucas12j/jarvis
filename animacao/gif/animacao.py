import pyglet
import time
import threading

class Animacao(object):

    def __init__(self, gif):
        t2 = threading.Thread(target=self.encerra_animacao, daemon= True)
        self.gif = gif
        t2.start()
        t2.join()
    
    def animacao(self):
        global gif
        animation = pyglet.image.load_animation(self.gif)
        animSprite = pyglet.sprite.Sprite(animation)
        w = animSprite.width
        h = animSprite.height
        window = pyglet.window.Window(width=w, height=h)
        r,g,b,alpha = 0.5,0.5,0.8,0.5
        pyglet.gl.glClearColor(r,g,b,alpha)
        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()
        pyglet.app.run()
            
    def encerra_animacao(self):
        t1 = threading.Thread(target=self.animacao)
        t1.start()
        for i in range(0,5):
            print(i)
            time.sleep(1)
        

