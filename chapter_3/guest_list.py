#Initial Guest List
guest_list = ['Aditya', 'Josh', 'Dan', 'Niranjana', 'Obama']
message = "You are invited to have dinner with me, "
print(message + guest_list[0].title() + ".")
print(message + guest_list[1].title() + ".")
print(message + guest_list[2].title() + ".")
print(message + guest_list[3].title() + ".")
print(message + guest_list[4].title() + ".")

print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")

#Changing Guest List
print("Unfortunately, " + guest_list.pop() + " can't make it.")
new_guest = 'Mehak'
print("We're inviting " + new_guest + " instead.")
guest_list.append(new_guest)

for counter in range(len(guest_list)):
	print(guest_list[counter] + " You're invited!")
print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")


#More Guests
guest_list.insert(0, "Prad")
guest_list.insert(4, "Anish")
guest_list.append("Kaushal")
for counter in range(len(guest_list)):
	print(guest_list[counter] + " You're invited!!11!1!")
print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")

	
#Less Guests
print(guest_list.pop() + ", you're not invited any more!")
print(guest_list.pop() + ", you're not invited any more!")
print(guest_list.pop() + ", you're not invited any more!")
print(guest_list.pop() + ", you're not invited any more!")
print(guest_list.pop() + ", you're not invited any more!")
print(guest_list.pop() + ", you're not invited any more!")

print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")



for counter in range(len(guest_list)):
	print(guest_list[counter] + " You're still invited!!")
	
print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")


del guest_list[1]
del guest_list[0]
print(guest_list)

print("I am inviting " + str(len(guest_list)) + " people to dinner \n\n\n")

