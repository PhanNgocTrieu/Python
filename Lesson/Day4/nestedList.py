# store all of names of US
unit_State = ["Delawre", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
"Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York",
"North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee"
]

unit_State.append("Hawaii")

unit_State.extend(["Angelaland", "Jack Baquarland"])

print(len(unit_State)) # 19

# nested lists:
asia = ["Vietnam", "Laos", "Combodia"]


_twoList = [unit_State,asia]

print(_twoList)