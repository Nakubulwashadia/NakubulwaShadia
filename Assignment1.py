print("===== Bill Split Calculator =====\n")

bill = float(input("Enter total bill amount: UGX"))

people = int(input("Enter number of people: "))

print("Tip options: 1) 10%  2) 15%  3) 20%  4) Custom")
tip_choice = input("Choose tip option (1-4): ")

if tip_choice == "1":
    tip_percent = 10
elif tip_choice == "2":
    tip_percent = 15
elif tip_choice == "3":
    tip_percent = 20
elif tip_choice == "4":
    tip_percent = float(input("Enter custom tip percentage: "))
else:
    print("Invalid choice, defaulting to 15%")
    tip_percent = 15

tip_amount = bill * (tip_percent / 100)
total_bill = bill + tip_amount
per_person = total_bill / people

print(f"""
======== RECEIPT ========
Original Bill:   UGX{bill:.2f}
Tip ({tip_percent}%):      UGX{tip_amount:.2f}
Total Bill:      UGX{total_bill:.2f}
People:          {people}
-------------------------
Each Person Pays: UGX{per_person:.2f}
=========================
""")