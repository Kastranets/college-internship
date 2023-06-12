total_amount = 352.7
tip_percentage = 15

amount_per_person = total_amount / 3
tip_amount_per_person = amount_per_person * (tip_percentage / 100)

total_per_person = amount_per_person + tip_amount_per_person

print("Кожний має сплатити за їжу {}, кожний має сплатити за чайові {}, загальний чек кожного {}".format(amount_per_person, tip_amount_per_person, total_per_person))