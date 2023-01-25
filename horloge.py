import time

### Mes paramètres
# l'heure à afficher sous forme de liste
clock =  [12, 30, 55]
# nouvelle heure à afficher sous forme de tuple
n_clock = (10,50,0)
# alarme sous forme de tuple
alarm = (12,31,0)
# heure à laquelle je souhaite mettre mon horloge en pause 
stop = (12,31,5)
# heure à laquelle je souhaite reprendre le décompte de mon horloge
reprise = (12,31,10)
# fonction regler heure une nouvelle heure
def set_time(n_clock):
    clock[0] = n_clock[0]
    clock[1] = n_clock[1]
    clock[2] = n_clock[2]
# décommenter la ligne suivante pour afficher la nouvelle heure souhaitée n_clock
#set_time(n_clock)


#fonction pour regler alarme
def alarme(clock):
    if alarm[0] == clock[0] and alarm[1] == clock[1] and alarm[2] == clock[2]:
        print("ALARM !!!")


#fonction pour choisir le mode d'affichage
def mode_affichage(clock, mode):
    if mode == 12:
        if clock[0] <= 12:
            print(str(clock[0]).zfill(2) + ":" + str(clock[1]).zfill(2) + ":" + str(clock[2]).zfill(2), "AM")
        elif clock[0] > 12:
            H_am_pm = clock[0] - 12
            print(str(H_am_pm).zfill(2) + ":" + str(clock[1]).zfill(2) + ":" + str(clock[2]).zfill(2), "PM")
    if mode == 24:
        print(str(clock[0]).zfill(2) + ":" + str(clock[1]).zfill(2) + ":" + str(clock[2]).zfill(2))
      
#fonction pour mettre l'affichage de l'heure en pause
def pause(pause, reprise):
    temps_de_pause = (reprise[0]-pause[0], reprise[1]-pause[1], reprise[2]-pause[2])
    temps_de_pause = temps_de_pause[0]+temps_de_pause[1]+temps_de_pause[2]
    if pause[0] == clock[0] and pause[1] == clock[1] and pause[2] == clock[2]:
            # time.sleep(temps_de_pause)
        time.sleep(temps_de_pause)

#fonction afficher l'heure
def afficher_heure(clock):
    while True:
        if clock[2] == 60:
            clock[2] = 0
            if clock[2] == 0:
                clock[1] +=1
        if clock[1] == 60:
            clock[1] = 0
            if clock[1] == 0:
                clock[0] += 1
        if clock[0] == 24:
            clock[0] = 0
        ## print initial qui me servait à afficher l'heure avant d'inclure la fonction mode_affichage permettant de choisir entre mode 12(AM/PM) ou 24
        #print(str(clock[0]).zfill(2) + ":" + str(clock[1]).zfill(2) + ":" + str(clock[2]).zfill(2))
        alarme(clock)
        ## mode: 12 ou 24
        mode_affichage(clock, 12) 
        clock[2] += 1
        time.sleep(1)
        pause(stop,reprise)
afficher_heure(clock)