from random import randint


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5


class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    @property
    def area(self):
        return (self.point1.x - self.point2.x) * (
            self.point1.y - self.point2.y
        )

    def is_point_inside(self, point: Point):
        return (
            self.point1.x < point.x < self.point2.x
            and self.point1.y < point.y < self.point2.y
        )


def main():
    lower_left = Point(x=randint(0, 9), y=randint(0, 9))
    upper_right = Point(x=randint(10, 19), y=randint(10, 19))
    rectangle = Rectangle(point1=lower_left, point2=upper_right)
    print(
        f"Rectangle Coordinates: "
        f"({rectangle.point1.x}, {rectangle.point1.y}) "
        f"and ({rectangle.point2.x}, {rectangle.point2.y})"
    )

    user_point = Point(
        x=int(input("Guess X: ")),
        y=int(input("Guess Y: ")),
    )
    user_area = int(input("Guess rectangle area: "))

    print(
        f"Your point was inside rectangle: {rectangle.is_point_inside(point=user_point)}"
    )
    print(f"Your area was off by: {rectangle.area - user_area}")


if __name__ == "__main__":
    main()
