
#before_scenario
def after_scenario(context,scenario):
    print(f"Scenario {scenario.name} has {scenario.status}")
    if scenario.status!='Status.passed':
        print('capture screenshot here.')