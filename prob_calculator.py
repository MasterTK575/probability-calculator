# import copy to make a deepcopy of the self.contents list
# import random to randomly choose elements from the list

import copy
import random

class Hat:
    # by using **, we say that the function can take variable amounts of arguments
    # ** means keyword arguments, ergo a dictionary is produced
    def __init__(self, **balls):
        # print(balls)
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
        # print(random.randint(0, len(self.contents)- 1))
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

        # self.contents remains untouched since we created a copy
        #print(self.contents)
        #print(contentscopy)
        return drawn
        

# by adding "*" we force all succeeding arguments to be named (aka. keyword arguments)
def experiment(*, hat, expected_balls, num_balls_drawn, num_experiments):
    # I don't have to create a copy for hat, since inside the draw function..
    # self.contencts remains untouched
    # therefore we start fresh each experiment

    times_result = 0
    # do the experiment x amount of times
    for experiment in range(num_experiments):
        # draw the balls
        result = hat.draw(num_balls_drawn)
        #print(result)
        
        # create a dictionary with counts for each ball
        result_dict = dict()
        for ball in result:
            result_dict[ball] = result_dict.get(ball, 0) + 1
        #print(result_dict)

        # compare the draw to what you want to see
        result_boolean = False
        for key, value in expected_balls.items():
            # if the value of the key (the ball) is equal or greater than..
            # the value of the same key in the result dictionary..
            # return True, else false
            # try and except in case the key is not present in the dict
            try:
                if value >= result_dict[key]:
                    result_boolean = True
                else:
                    result_boolean = False
            except:
                result_boolean = False
        
        # if we did get the desired result, increase the count
        if result_boolean == True:
            times_result = times_result + 1
    probability = times_result / num_experiments
    return probability

hat = Hat(black=6, red=4, green=3)
hat.draw(10)

print(experiment(hat=hat, expected_balls={"red":2,"green":1},num_balls_drawn=5,num_experiments=2000))


