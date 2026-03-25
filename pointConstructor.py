class Point:
    # used to create and construct the object
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def move(self):
        print("Moving Point")

    def draw(self):
        print("Drawing Point")



point1 = Point(10 , 20)
print(point1.x)
print(point1.y)

point1.x = 11
print(point1.x)
print(point1.y)