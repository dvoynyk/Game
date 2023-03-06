class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(0.5,0.5,0.5,1)
        self.hero.setScale(1)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.acceptEvents()
        self.mode = True
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0],-pos[1],-pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False   
    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        else:
            self.cameraBind()
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    def try_move(self,angle):
        pass
    def move_to(self,angle):
        if self.mode:
            self.just_move(angle)
        # else:
        #     self.try_move()
    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
            return (0,-1)
        elif angle <= 65:
            return (1,-1) 
        elif angle <= 110:
            return (1,0)
        elif angle <= 155:
            return (1,1)
        elif angle <= 200:
            return (0,1)
        elif angle <= 245:
            return (-1,1)
        elif angle <= 290:
            return (-1,0)
        elif angle <= 355:
            return (-1,-1)
        else:
            return (0,-1)
    def look_at(self,angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())
        dx,dy = self.check_dir(angle)
        return from_x + dx,from_y + dy, from_z
    def just_move(self,angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)
    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
    def left(self): 
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)
    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)
    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)
    def acceptEvents(self):
        base.accept('q',self.changeView)
        base.accept('1'+'-repeat',self.turn_left)
        base.accept('1',self.turn_left)
        base.accept('2'+'-repeat',self.turn_right)
        base.accept('2',self.turn_right)
        base.accept('w',self.forward)
        base.accept('a',self.left)
        base.accept('d',self.right)
        base.accept('s',self.back)
        base.accept('w'+'-repeat',self.forward)
        base.accept('a'+'-repeat',self.left)
        base.accept('d'+'-repeat',self.right)
        base.accept('s'+'-repeat',self.back)