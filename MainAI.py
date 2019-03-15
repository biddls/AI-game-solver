import random as ra
import matplotlib.pyplot as plt

##############values for init##############
names = [
    #name
"Reusable Rockets" ,
"Space elevator"   ,
"Orbital rings"    ,
"Asteroid mining"  ,
"1Space clean up"  ,
"1Mars colony"     ,
"Planet mining"    ,
"1Dyson Swarm"     ,
"1Dyson sphere"    ,
"Sun mining"       ,
"Space colony"     ,
"Colony Ship"      ,
]

ProjectList = [
#PS      cost
[100, 	3000],  #0
[200,	6000],  #1
[300,	9000],  #2
[400,	12000], #3
[500,	13000], #4
[600,	15000], #5
[700,	16000], #6
[800,	17000], #7
[900,	18000], #8
[1000,	19000], #9
[1100,	20000], #10
[0,		21000]  #11
]


class gameai():
    #random weight to start
    dontbuy = 0

    #inti
    gamecomplete = False
    money = 10000
    moneyps = 200
    boughtitems = [None] * 0
    max = -1

    ############## buys said item and check if its the last one ##############
    def buymax(self, numbbuy):
        self.money -= ProjectList[numbbuy][1]
        self.moneyps += ProjectList[numbbuy][0]
        self.boughtitems.append(numbbuy)

        #game complete#
        if numbbuy == 11:
            self.gamecomplete = True


    ############## Checks to see what it needs to do befre it can be bought ##############
    def buyOrSkip(self,numbbuy):
        up = ra.random()

        if up > self.dontbuy:
            self.buymax(numbbuy)
            self.max = 0
        else:
            self.boughtitems.append(-1)

    ############## max purchase def ##############
    def buylist(self):

        #init
        self.money += self.moneyps
        self.max = -1

        #for loop to define what can and cant be used
        for n in range(len(ProjectList)):
            if ProjectList[n][1] <= self.money:
                #max buy
                if n > self.max:
                    self.max = n

        if self.max >= 0:
            self.buyOrSkip(self.max)

    ############## print all ##############
    def outall(self):
        print("moneyps",self.moneyps)
        print("money",self.money)
        print("game complete",self.gamecomplete)
        print("dont buy",self.dontbuy)
        print("boughtitems",len(self.boughtitems))
        print()


    def __init__(self,ran):
        self.dontbuy = ran


############## main AI def and running ##############
def makeAI():
    #def of ai#
    pop = 1000
    l = list()

    #make a bunch of random AI
    for x in range(pop):

        ran = ra.random()
        temp = (gameai(ran))
        temp.boughtitems = []

        #run ai#
        while temp.gamecomplete == False:
            temp.buylist()

        #add it to the list
        l.append(temp)

    return l


############## pops non classes ##############
def popity(lil):

    #kicks out the assigned ones
    out1 = False
    while out1 == False:

        changed1 = False

        for m in range(len(lil)-1):

            check = "<class '__main__.gameai'>"

            if str(type(lil[m])) != check and changed1 == False or lil[m] == 0 and changed1 == False:

                lil.pop(m)
                changed1 = True

        if changed1 == False:
            out1 = True

    return lil


############## take the arrays and eval them ##############
def evalAI(lil):

    lil = popity(lil)

    lil.sort(key = lambda x: len(x.boughtitems),reverse=False)

    #trims to 100 AI's (cut off worst)
    x = len(lil)

    while len(lil) > 1000:
        lil.pop(x-1)
        x -= 1

    perOut = 0

    #randomly asigns out 1/2
    for count in range(len(lil)):
        rar = ra.random()

        if rar < perOut:
            lil[count] = 0

        perOut += 1/1000


    out = False

    #kicks out the assigned ones
    while out == False:

        changed = False

        for index in range(len(lil)-1):

            if lil[index] == 0 and changed == False:

                lil.pop(index)
                changed = True

        if changed == False:
            out = True

    return evolve(lil)


############## Evolve ##############
def evolve(lil):

    #makes a copy for every one of the AI's doubling the lot
    for x in range(len(lil)-1):
        #new weight for new ai
        ranAI = None

        ran = 0

        ran = ra.random()/1000000

        ran = lil[x].dontbuy + ran

        if  lil[x].dontbuy + ran > 1:
            ran = ra.random()

        elif lil[x].dontbuy + ran < 0:
            ran = ra.random()

        #init newly made AI

        ranAI = gameai(ran)

        #run ai#

        ranAI.boughtitems = []

        while ranAI.gamecomplete == False:
            ranAI.buylist()

        lil.append(ranAI)

    #add it to the list
    return lil


############## main ##############
lil = makeAI()

max = 1000000

x = 0

x1 = []
y1 = []

iterations = 100

for q in range(iterations):

    lil = evalAI(lil)

    for m in range(len(lil)-1):
        lil = popity(lil)

        if len(lil[m].boughtitems) < max:
            max = len(lil[m].boughtitems)
            index = m

    x1.append(max)
    y1.append(q)

    for m in range(len(lil)):
        if len(lil[m].boughtitems) > 200:
            lil[m] = 0

    lil = popity(lil)
    lil.pop(len(lil)-1)

    #print("best",q)
    #lil[0].outall()
    print(str(round((q/iterations)*100))+"%")
    print("lowest itterations "+str(max)+"'s")

print("out")
plt.plot(y1, x1)
plt.show()