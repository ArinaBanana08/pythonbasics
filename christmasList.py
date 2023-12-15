gift_list = []
while True:
   action = input("Do you want to add or remove a gift? (Type 'add', 'remove', or 'exit'): ")
  
   if action == 'add':
       gift = input("Enter the gift you want to add: ")
       gift_list.append(gift)
   elif action == 'remove':
       if gift_list:
           removed_gift = gift_list.pop()
           print("Removed:",removed_gift)
       else:
           print("Gift list is empty.")
   elif action == 'exit':
       print("Exiting the program. Your gift list:")
       print(gift_list)
       break
   else:
       print("Invalid choice. Please enter 'add', 'remove', or 'exit'.")