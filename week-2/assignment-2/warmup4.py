# 1. Error message:
# TypeError: can only concatenate str (not "int") to str

# 2. What caused it:
# I used a string ("38") instead of an integer.
# Python cannot add a string and an integer together.

# 3. How I fixed it:
# I converted the string to an integer using int().
# Now Python can add 1 to my age.
age = int("38")
next_year_age = age + 1
print (f"Next year I will be {next_year_age} years old.")
