# love calculator:
#   Take both people'name and check for number of time the letters in the word TRUE occurs.
#   Then check for the number of times the letters in the LOVE occurs.
#   Then combine these numbers to make a 2 digit number.
_yourName = input("What is your name?\n")
_theirName = input("What is their name?\n")

# count for true word
_yourName = _yourName.lower()
_theirName = _theirName.lower()

_countOfTrue = _yourName.count("t") + _yourName.count('r') + _yourName.count("u") + _yourName.count("e")
_countOfTrue += _theirName.count("t") + _theirName.count('r') + _theirName.count("u") + _theirName.count("e")

_countOfLove = _yourName.count("l") + _yourName.count('o') + _yourName.count("v") + _yourName.count("e")
_countOfLove += _theirName.count("l") + _theirName.count('o') + _theirName.count("v") + _theirName.count("e")


_combine = _countOfTrue*10 + _countOfLove

if _combine < 10 or _combine > 90:
    print(f"Your score is **{_combine}**, you go together like coke and mentos.")
elif _combine > 40 and _combine < 50:
    print(f"Your score is **{_combine}**, you are alright together.")
else:
    print(f"Your score is **{_combine}**.")



# _another way
_name = _yourName.lower() + _theirName.lower()

_t = _name.count("t")
_r = _name.count("r")
_u = _name.count("u")
_e = _name.count("e")

true = _t + _r + _u + _e


_l = _name.count("l")
_o = _name.count("o")
_v = _name.count("v")
_e = _name.count("e")

love = _l + _o + _v + _e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is **{love_score}**, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is **{love_score}**, you are alright together.")
else:
    print(f"Your score is **{love_score}**.")