import sys
class legends:
    def __init__(self,name,pas,tact,ult,is_lp,is_ftf):
        self.name=name
        self.pas=pas
        self.tact=tact
        self.ult=ult
        self.is_lp=is_lp
        self.is_ftf=is_ftf

l1=legends("Banglore", "Double time","Smoke launcher","Rolling thunder",False,False)
l2=legends("Wraith","Voices from the void" , "Into the void","Dimensional rift",True,False)
l3=legends("Loba","Eye for quality","Burglar's best friend","Black market boutique",False,False)
l4=legends("Bloodhound","Tracker","Eye of allfather","Bast of hunt",False,False)
l5=legends("Caustic","Nox vision","Nox gas trap","Nox gas grenade ",False,True)
l6=legends("Wattson","Spark of genius","Perimeter security","Interception pylon ",True,False)
l7=legends("Crypto","Nuero link","Surveillance drone","Drone EMP",False,False)
l8=legends("Pathfinder","Insider knowledge","Grappling hook","Zipline gun",True,False)
l9=legends("Mirage","Now you see me","Psyche out","Life of the party",False,False)
l10=legends("Gibraltar","Gun shield","Dome of protection","Defensive bombardment",False,True)
l11=legends("Lifeline","Combat revive","D.O.C. heal drone","Care package",True,False)
l12=legends("Octane","Swift mend","Stim","Launch pad",False,False)
l13=legends("Revenant","Stalker","Silence","Death totem",False,False)

list=("Legend Name:- ","Passive:- ","Tactical:- ","Ultimate:- ","Low profile legend","Fortified legend")

choice = sys.argv[1]
print("\n")
if choice == "banglore" or choice == "bang":
    print(list[0] + l1.name + "\n" + list[1] + l1.pas + "\n" + list[2] + l1.tact + "\n" + list[3] + l1.ult)
    if l1.is_lp:
        print(list[4])
    elif l1.is_ftf:
        print(list[5])
    print("\n")


elif choice == "wraith":
    print(list[0] + l2.name + "\n" + list[1] + l2.pas + "\n" + list[2] + l2.tact + "\n" + list[3] + l2.ult)
    if l2.is_lp:
        print(list[4])
    elif l2.is_ftf:
        print(list[5])
    print("\n")


elif choice == "loba":
    print(list[0] + l3.name + "\n" + list[1] + l3.pas + "\n" + list[2] + l3.tact + "\n" + list[3] + l3.ult)
    if l3.is_lp:
        print(list[4])
    elif l3.is_ftf:
        print(list[5])
    print("\n")


elif choice == "bloodhound":
    print(list[0] + l4.name + "\n" + list[1] + l4.pas + "\n" + list[2] + l4.tact + "\n" + list[3] + l4.ult)
    if l4.is_lp:
        print(list[4])
    elif l4.is_ftf:
        print(list[5])
    print("\n")


elif choice == "caustic":
    print(list[0] + l5.name + "\n" + list[1] + l5.pas + "\n" + list[2] + l5.tact + "\n" + list[3] + l5.ult)
    if l5.is_lp:
        print(list[4])
    elif l5.is_ftf:
        print(list[5])
    print("\n")


elif choice == "wattson":
    print(list[0] + l6.name + "\n" + list[1] + l6.pas + "\n" + list[2] + l6.tact + "\n" + list[3] + l6.ult)
    if l6.is_lp:
        print(list[4])
    elif l6.is_ftf:
        print(list[5])
    print("\n")


elif choice == "crypto":
    print(list[0] + l7.name + "\n" + list[1] + l7.pas + "\n" + list[2] + l7.tact + "\n" + list[3] + l7.ult)
    if l7.is_lp:
        print(list[4])
    elif l7.is_ftf:
        print(list[5])
    print("\n")


elif choice == "pathfinder" or choice == "path":
    print(list[0] + l8.name + "\n" + list[1] + l8.pas + "\n" + list[2] + l8.tact + "\n" + list[3] + l8.ult)
    if l8.is_lp:
        print(list[4])
    elif l8.is_ftf:
        print(list[5])
    print("\n")


elif choice == "mirage":
    print(list[0] + l9.name + "\n" + list[1] + l9.pas + "\n" + list[2] + l9.tact + "\n" + list[3] + l9.ult)
    if l9.is_lp:
        print(list[4])
    elif l9.is_ftf:
        print(list[5])
    print("\n")


elif choice == "gibraltar" or choice == "gibby" or choice == "gib":
    print(list[0] + l10.name + "\n" + list[1] + l10.pas + "\n" + list[2] + l10.tact + "\n" + list[3] + l10.ult)
    if l10.is_lp:
        print(list[4])
    elif l10.is_ftf:
        print(list[5])
    print("\n")


elif choice == "lifeline":
    print(list[0] + l11.name + "\n" + list[1] + l11.pas + "\n" + list[2] + l11.tact + "\n" + list[3] + l11.ult)
    if l11.is_lp:
        print(list[4])
    elif l11.is_ftf:
        print(list[5])
    print("\n")


elif choice == "octane":
    print(list[0] + l12.name + "\n" + list[1] + l12.pas + "\n" + list[2] + l12.tact + "\n" + list[3] + l12.ult)
    if l12.is_lp:
        print(list[4])
    elif l12.is_ftf:
        print(list[5])
    print("\n")


elif choice == "revenant" or choice == "rev":
    print(list[0] + l13.name + "\n" + list[1] + l13.pas + "\n" + list[2] + l13.tact + "\n" + list[3] + l13.ult)
    if l13.is_lp:
        print(list[4])
    elif l13.is_ftf:
        print(list[5])
    print("\n")
else:
    print("that's not a legend !!")
    print("Usage:- python apexf.py <name of legend>\n")





