
Disco_1 = [1, 2, 3 , 4, 5]
Disco_2 = [0, 0, 0, 0, 0]
Disco_3 = [0, 0, 0, 0, 0]
i = 0
n = 3

def impresion(Disco_1, Disco_2, Disco_3):
    for i in range(0, 4):
        print(str(Disco_1[i])+"    "+str(Disco_2[i])+"    "+str(Disco_3[i]))

print("Primer estado de Discos")
impresion(Disco_1, Disco_2, Disco_3)

def hanoi(Disco_1, Disco_2, Disco_3):
        i = 0
        n = 3
        if(Disco_1[i] < Disco_2[n + 1] or Disco_2[n]==0):
            Disco_2[n] = Disco_1[i]
            Disco_1[i] = 0
        elif(Disco_1[i] < Disco_3[n + 1] or Disco_3[n]==0):
            Disco_3[n] = Disco_1[i]
            Disco_1[i] = 0
        else:
            i = i + 1
        impresion(Disco_1, Disco_2, Disco_3)
        if(Disco_1!= [1, 2, 3, 4, 5]):
            hanoi(Disco_1, Disco_2, Disco_3)

hanoi(Disco_1, Disco_2, Disco_3)
