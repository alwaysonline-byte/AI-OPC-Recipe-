class ReportAgent:
    def generate(self, history):
        avg_epe = sum([h["EPE"] for h in history]) / len(history)
        avg_dof = sum([h["DOF"] for h in history]) / len(history)

        return {
            "avg_EPE": avg_epe,
            "avg_DOF": avg_dof,
            "iterations": len(history)
        }
