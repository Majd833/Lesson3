amount=int(input("please enter the Amount for withdrawal"))
note1=amount//100
note2=(amount%100)//50
note3=(amount%50)//10

print("Note1 = ",note1)
print("Note2 = ",note2)
print("Note3 = ",note3)