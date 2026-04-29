from agents.pattern_agent import PatternAgent
from agents.recipe_agent import RecipeAgent
from agents.simulation_agent import SimulationAgent
from agents.optimizer_agent import OptimizerAgent
from agents.report_agent import ReportAgent

class OPCOrchestrator:
    def __init__(self):
        self.pattern_agent = PatternAgent()
        self.recipe_agent = RecipeAgent()
        self.sim_agent = SimulationAgent()
        self.optimizer = OptimizerAgent()
        self.report_agent = ReportAgent()

    def run(self, layout_data):
        patterns = self.pattern_agent.analyze(layout_data)
        recipe = self.recipe_agent.generate(patterns)

        history = []
        for _ in range(5):
            sim_result = self.sim_agent.simulate(recipe)
            recipe = self.optimizer.optimize(recipe, sim_result)
            history.append(sim_result)

        report = self.report_agent.generate(history)
        return recipe, report
