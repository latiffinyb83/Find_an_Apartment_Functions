def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month..."
    else:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month..."
    return result

# Function apt_search2 with default values
def apt_search2(city, max_rent, min_beds=1, pets_allowed=True):
    if pets_allowed:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of ${max_rent} per month..."
    else:
        result = f"Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments, all within a budget of ${max_rent} per month..."
    return result

# Lambda functions
plus_one_hundred = lambda x: x + 100
square_num = lambda x: x ** 2
concatenate = lambda x: "- " + x
divide_by_three = lambda x: x / 3

# Testing apt_search2 function with different scenarios
print(apt_search2("Charlotte", 1500))  # Default values for min_beds and pets_allowed
print(apt_search2("Houston", 1800, min_beds=2))  # Using min_beds and default value for pets_allowed
print(apt_search2("Miami", 2000, pets_allowed=False))  # Using named argument for pets_allowed

# Testing lambda functions
print(plus_one_hundred(30))  # Should print 130
print(square_num(4))  # Should print 16
print(concatenate('hello'))  # Should print "- hello"
print(divide_by_three(9))  # Should print 3.0

# Call apt_search2 with different scenarios
result1 = apt_search2("Charlotte", 1500)
print(result1)

# Providing min_beds, omitting pets_allowed
result2 = apt_search2("Miami", 1800, min_beds=2)
print(result2)

# Providing pets_allowed, omitting min_beds (using named arguments)
result3 = apt_search2("Houston", 2000, pets_allowed=False)
print(result3)