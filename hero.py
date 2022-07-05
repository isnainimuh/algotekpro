class Hero:
    #create constructor
    def __init__(self, name, attackHitPoint, attackKickPoint):
        self.lifePoint=100
        self.name=name
        self.attackHitPoint=attackHitPoint
        self.attackKickPoint=attackKickPoint
    
    #create method
    def getName(self):
        return self.name

    def hit(self,Lawan):
        Lawan.lifePoint -= self.attackHitPoint
        print(self.name, " memukul ", Lawan.getName())
    
    def kick(self, Lawan):
        Lawan.lifePoint -= self.attackKickPoint
        print(self.name, " menendang ", Lawan.getName())
    
    def getLifePoint(self):
        print ("Lifepoint ", self.name, " ", self.lifePoint)


superman = Hero("superman",20,10)
batman = Hero("batman",15,20)

superman.hit(batman)
batman.kick(superman)
batman.hit(superman)
superman.getLifePoint()
batman.getLifePoint()