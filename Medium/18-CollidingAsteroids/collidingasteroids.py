# You're given an array of integeres "asteroids", where each integer represents the size of an asteroid. 
# The sign of the integer represents whether it's moving to the right (+) or to the left (-). All of the asteroids are moving at the same speed.
# Meaning that two asteroids moving in the same direction can never collide
# For example, the integer 4 represents an asteroid with size 4 moving to the right.
# Similarly, -7 represents an asteroid of size 7 moving to the left.
# If two asteroids collide the smaller one (based on absolute value) will explode. If they are the same size, both will explode.
# Write a function that takes in this array of asteroids and returns an array of integers representing an array
# of integers representing the asteroids after all collisions occur.

# Sample Input:
# asteroids = [-3, 5, -8, 6, 7, -4, -7]
# Sample Output:
# [-3, -8, 6] // -3 moves left, having no collisions
#              // 5 moves right, colliding with the -8 and being destroyed by it
#              // 6 never collides with another asteroid
#              // 7 moves right, colliding with the -4, destroying it
#              // 7 and the -7 then collide, both being destroyed

def collidingAsteroids(asteroids):
    # resultStack[-1] is the value at the top of the stack (the last one pushed in)
    resultStack = []
    
    for asteroid in asteroids:
        if asteroid > 0:
            resultStack.append(asteroid)
            continue

        while True:
            if len(resultStack) == 0 or resultStack[-1] < 0:
                resultStack.append(asteroid)
                break

            asteroidSize = abs(asteroid)

            # if the incoming asteroid's size is smaller that the one coming from the oppostie direction (top of the stack)
            # do nothing
            if resultStack[-1] > asteroidSize:
                break
            
            # incoming asteroid is bigger than the asteroid at the top of the stack
            if resultStack[-1] == asteroidSize:
                # pop the asteroid from the stack (it got destroyed)
                resultStack.pop()
                break
                
            # incoming asteroid is bigger in size than the asteroid coming from the other direction (top of the stack)
            # destroy the asteroid in the stack
            if resultStack[-1] < asteroidSize:
                resultStack.pop()

    return resultStack
            
                

asteroids = [-3, 5, -8, 6, 7, -4, -7]
print(collidingAsteroids(asteroids))
# [-3, -8, 6] // -3 moves left, having no collisions