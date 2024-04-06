# Trójkąt
def triangle_area(base, height):
    """
    Calculates the area of a triangle given its base and height.
    
    Args:
    - base (float): The base of the triangle.
    - height (float): The height of the triangle.
    
    Returns:
    - float: The area of the triangle.
    """
    area = 0.5 * base * height
    return area

# Example usage:
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = triangle_area(base, height)
print("The area of the triangle is:", area)

# Kwadrat
def square_area(side_length):
    """
    Calculates the area of a square given the length of its side.
    
    Args:
    - side_length (float): The length of a side of the square.
    
    Returns:
    - float: The area of the square.
    """
    area_sq = side_length * side_length
    return area_sq

# Example usage:
side_length = float(input("Enter the length of a side of the square: "))

area_sq = square_area(side_length)
print("The area of the square is:", area_sq)
# Trapez
def trapezoid_area(base1, base2, height):
    """
    Calculates the area of a trapezoid given the lengths of its bases and height.
    
    Args:
    - base1 (float): Length of the first base of the trapezoid.
    - base2 (float): Length of the second base of the trapezoid.
    - height (float): The height of the trapezoid.
    
    Returns:
    - float: The area of the trapezoid.
    """
    area = 0.5 * (base1 + base2) * height
    return area

# Example usage:
base1 = float(input("Enter the length of the first base of the trapezoid: "))
base2 = float(input("Enter the length of the second base of the trapezoid: "))
height = float(input("Enter the height of the trapezoid: "))

area = trapezoid_area(base1, base2, height)
print("The area of the trapezoid is:", area)