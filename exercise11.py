#Slicing strings

text=("Twinkle, twinkle, little star,\n\thow I wonder what you are! \n\t\tUp above the world so high,\n\t\tlike a diamond in the sky.\nTwinkle, twinkle, little star,\n\thow I wonder what you are!")

first="Twinkle, twinkle, little star"
second="Up above the world so high"
third="how I wonder what you are!"

print(first + text[30:60] + second + text[87:119] + first + "\n\t"+third)