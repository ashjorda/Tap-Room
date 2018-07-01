guest_list = ['Mike', 'Travis', 'Jessica']

def current_tap_guest():
	print("Current Patrons are: \n")
	for x in guest_list:
		print(x)

def add_tap_guest():
	new_guest = input("Enter Patrons Name: ")
	guest_list.append(new_guest)
	print("Guest list updated!")

def remove_tap_guest(x):
	try:
		guest_list.remove(x)
		print("Patron has been removed!")
	except:
		print("Patron is not in the list.")

print(r"""
+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+
 |A|s|h|t|o|n|'|s| |T|A|P| |R|O|O|M|
+-+-+-+-+-+-+-+-+ +-+-+-+ +-+-+-+-+
 """)

beer_cold = True
while beer_cold != False:
		menu_selection = input("\n[1] Show Current Guest List \n[2] Add Guest to list \n[3] Remove Guest from list \n[4] Exit Program" + "\n\nEnter your selection: ")
		if menu_selection == '1':
			current_tap_guest()
		elif menu_selection == '2':
			add_tap_guest()
		elif menu_selection == '3':
			guest = input("Enter Patron to be removed: ")
			remove_tap_guest(guest)
		elif menu_selection == '4':
			break
		else:
			print("Invalid entry, please try again\n")
