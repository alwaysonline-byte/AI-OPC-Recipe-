import random

class SimulationAgent:
    def simulate(self, recipe):
        return {
            "EPE": random.uniform(1.0, 5.0),
            "DOF": random.uniform(50, 150),
            "CD_error": random.uniform(0.5, 2.0)
        }
