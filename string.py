name="ShReYas-SaHoo-islike-moon"
print(name)
print(name[-6]);
print(len(name))
#slicing
print(name[2:5])
print(name[-6:-2])
print(name[:4])
print(name[-4:-1])
#printing even characters
print(name[::2])
#printing odd characters
print(name[1::2])
print(name[3:18:3])
print(name[-17:-4:2])
print(name[-4:-17:-2])
print(name[-4:-17:-1])
print(name[::-1])
#replace method
name=name.replace("-", " ", 2)
print(name)
name=name.replace("islike", "is like")
print(name)
#split method
name1=name.split(" ", 2)
print(name1)
#define lower and upper cases, capitalize, title, swapcase
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.swapcase())
print("hello shreYas".islower())
print("Hello Shreyas".isupper())
print("hello".encode(encoding="ascii"))
# grinning face
print("\U0001f600")
 
# grinning squinting face
print("\U0001F606")
 
# rolling on the floor laughing
print("\U0001F923")
