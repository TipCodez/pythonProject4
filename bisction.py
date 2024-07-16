from math import sin


# f(x)= x - 2sin(x), [1, 2], tolerance = 1e-6
# defining the function
def f(x):
    return x - 2 * sin(x)


# Defining the Bisection method
def bisection_method(a, b, tol):
    if (f(a) * f(b)) > 0:
        print("The Bisection method failed !")
        return None
    lower_limit = a
    higher_limit = b

    centre = (higher_limit - lower_limit) / 2.0
    while centre >= tol:
        midpoint = (lower_limit + higher_limit) / 2.0
        if f(midpoint) == 0:
            return midpoint
        elif f(lower_limit) * f(midpoint) < 0:
            higher_limit = midpoint
        else:
            lower_limit = midpoint
    return (lower_limit + higher_limit) / 2.0


print("f(x)= x - 2sin(x), [1, 2], tolerance = 1e-6 ")
print("Test the function with other limits and considerable tolerance value")
a = float(input("Enter the lower limit: "))
b = float(input("Enter the higher limit: "))
tolerance = float(input("Enter the lower limit: "))

root = bisection_method(a, b, tolerance)
root = round(root, 3)
print(f"The root of the function is {root}.")
