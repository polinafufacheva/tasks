def greet_guests(guest_list):
    for guest in guest_list:
        print(f"Привет, {guest}!")
guests = ["Полина", "Артём", "Максим"]
greet_guests(guests)