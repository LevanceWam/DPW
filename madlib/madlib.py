ice_cream = raw_input("What's your flavor: ")

print "Tom was walking down the street and wanted a "+ice_cream+" Ice cream cone"

friends = ["Monster", "T-Rex", "Jello"]
print "Tom's friends wanted Ice cream too and they all had the same amount of money, Tom already has $5.00"

for f in friends:
    print f + ", Has $2.00 on with them."

quest = raw_input("Please put in a random word: ")
print "The group decided to go to "+quest+ ", for Ice cream"

print "At "+quest+" their ultimate Ice cream  Sundae cost $25"
print "Tom know's that he has money in his piggy bank but can't remember how much was in there but he know's it's no greater than 5"
print "Tom's friends also have some extra money but they have $2 less than he has"
print "Tom goes and checks the piggy bank"

piggy = raw_input("How much money was in the bank: ")
piggy = int(piggy)
if 5 < piggy:
    raw_input("Please check again")
else:
    print "Tom has $" + str(piggy)
#function to find how much money toms friends have
    def all (a):
        b = a - 2
        return b
#toms friends money
returnb = all(piggy)
print "Tom's friends individually have $" + str(returnb)

#All of toms friends money all together
extra_friend_money_all = int(returnb) * 3 + 6
print extra_friend_money_all

tom_money_all = int(piggy) + 5

print "after going counting all of the money Tom had $"+str(tom_money_all)+", and his friends had $"+str(extra_friend_money_all)

final_amount = extra_friend_money_all + tom_money_all
print "When they added it together it totaled out to $"+str(final_amount)
final_amount = int(final_amount)

if final_amount < 25 or None:
    print"Sorry No Ice cream for you"
else:
    print"Yay For Ice Cream"



