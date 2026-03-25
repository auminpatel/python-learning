class Point:
    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point()

point1.move()

point1.x = 3
point1.y = 2
print(point1.x, point1.y)
point2 = Point()

# this are different objects
#  class is a blueprint or template, while an object is a concrete instance created from that blueprint
print(point2.x)
