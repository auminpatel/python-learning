from pathlib import Path

# Abosolute Path
# c:\Program Files\MicroSoft
#/user/local/bin
# Relative Path

path = Path("eccomerc1e")

print(path.exists())



path2 = Path()

for file in path2.glob('*'):
    print(file)


# pyPi can we used to check for packages created by People