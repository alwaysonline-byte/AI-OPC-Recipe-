class OptimizerAgent:
    def optimize(self, recipe, sim_result):
        if sim_result["EPE"] > 2.5:
            recipe["bias"] -= 1
        else:
            recipe["bias"] += 0.5

        if sim_result["DOF"] < 80:
            recipe["serif_size"] += 1

        return recipe
