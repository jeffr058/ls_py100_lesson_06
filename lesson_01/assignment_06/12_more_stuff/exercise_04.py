# Write a function called increment_counter that increments a counter variable every time it is called. You can test your code with the following:

# my solution
counter = 0

def increment_counter():
    global counter
    counter += 1
    # return counter          # remove as the function shouldn't have a side
                              # effect AND a return value
# end of my solution

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101