import random

a=random.randint(1,3)

print("1--Stone")
print("2--Paper")
print("3--Scissor")


print("Player1, Select your Option")
p1=int(input())
print("comp, Selected option")
print(a)
comp=(a)

if (comp==1 and p1==2) or (comp==2 and p1==3) or (comp==3 and p1==1):
	print("Player 1 Wins…")
if  (comp==2 and p1==1) or (comp==3 and p1==2) or (comp==1 and p1==3):
	print("comp Wins...")
elif comp==p1:
	print("Match Draw…")