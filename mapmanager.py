class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.colors = [(0.85,0.85,0.23,1),
                        (0.44,0.92,0.05,1),
                        (1,0.83,0,1),
                        (0.44,0.04,0.67,1),
                        (0.91,0,0.24,1)]
        self.startNew()
    def startNew(self):
        self.land = render.attachNewNode('Land')
    def getColor(self,z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]
    def addBlock(self,position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land) 
        self.color = self.getColor(position[2])
        self.block.setColor(self.color)
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def loadLand(self,filename):
        self.clear()
        with open (filename,'r') as file:
            y = 0
            for string in file:
                x = 0
                line = string.split(' ')
                for z in line:
                    for z1 in range(int(z) + 1):
                        self.addBlock((x,y,z1))
                    x += 1 
                y += 1 
        return x,y