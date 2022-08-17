import copy
import random


class Hat:
    # by using **, we say that the function can take variable amounts of arguments
    # ** means keyword arguments, ergo a dictionary is produced
    def __init__(self, **balls):
        #print(balls)
        contents = list()
        # make a list of tuples by using .items() and then iterate through key and value at the same time
        for key, value in balls.items():
            # add an amount of keys to the list equal to the number
            for number in range(value):
                contents.append(key)
        self.contents = contents
    
    def draw(self, times):
        # option 1: return a random integer from 0 to lenght of the list -1
        # then use indexing to get the "ball" and remove it
        #print(random.randint(0, len(self.contents)- 1))
        drawn = list()

        # contentscopy = self.contents does not work
        # it only creates a shallow copy and shallow copies refer to the original object
        # this means that changes in one affect the other
        contentscopy = copy.deepcopy(self.contents)

        # draw the amount of times given
        for draw in range(times):
            # option 2: just return a random item from the list
            try:
                balldrawn = random.choice(contentscopy)
            except:
                print("Returning all balls.")
                contentscopy = copy.deepcopy(self.contents)
                balldrawn = random.choice(contentscopy)

            contentscopy.remove(balldrawn)
            drawn.append(balldrawn)
        print(drawn)
        print(contentscopy)
        # no idea why, but self.contents gets modified (aka. balls are removed) as well
        print(self.contents)

hat1 = Hat(yellow=2, blue=2, green=2)
hat1.draw(7)
