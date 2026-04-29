from core.orchestrator import OPCOrchestrator

if __name__ == "__main__":
    layout_data = "mock_gds_data"

    orchestrator = OPCOrchestrator()
    recipe, report = orchestrator.run(layout_data)

    print("Final Recipe:", recipe)
    print("Report:", report)
