class ShapeCalculatorRefactored:
    def calculate_area(self, shape_type):
        if shape_type == "circle":
            self.calculate_circle_area()
        elif shape_type == "rectangle":
            self.calculate_rectangle_area()
        elif shape_type == "triangle":
            self.calculate_triangle_area()

    def calculate_circle_area(self):
        self.calculate_circle_area()

    def calculate_rectangle_area(self):
        self.calculate_rectangle_area()

    def calculate_triangle_area(self):
        self.calculate_triangle_area()

    def calculate_circle_area(self):
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14 * radius * radius
        print("Area:", area)

    def calculate_rectangle_area(self):
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print("Area:", area)

    def calculate_triangle_area(self):
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print("Area:", area)


calculator = ShapeCalculatorRefactored()
calculator.calculate_area("circle")