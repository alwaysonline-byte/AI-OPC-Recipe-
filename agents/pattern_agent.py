import random

class PatternAgent:
    def analyze(self, layout_data):
        return {
            "line_end": random.randint(10, 50),
            "corner": random.randint(5, 30),
            "dense": random.randint(20, 100)
        }
