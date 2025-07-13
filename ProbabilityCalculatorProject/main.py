import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for _ in range(count):
                self.contents.append(color)
    
    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            drawn_balls = self.contents.copy()
            self.contents = []
            return drawn_balls
        drawn_balls = []
        for _ in range(num_balls):
            index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        ball_count = {}
        for ball in drawn_balls:
            ball_count[ball] =  ball_count.get(ball, 0)+ 1
        success = True
        for color, count in expected_balls.items():
            if ball_count.get(color, 0) < count:
                success = False
                break
        if success:
            success_count += 1
    return success_count / num_experiments