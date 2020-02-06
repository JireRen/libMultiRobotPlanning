import yaml
import argparse
import numpy as np

class yamlTest:
    def __init__(self, yamlfile):
        self.cost = yamlfile["statistics"]["cost"]
        self.makespan = yamlfile["statistics"]["makespan"]
        self.runtime = yamlfile["statistics"]["runtime"]
        self.schedule = yamlFile["schedule"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("yamlFile", help="input yamlfile to parse")
    args = parser.parse_args()

    with open (args.yamlFile) as file:
        yamlFile = yaml.load(file, Loader=yaml.FullLoader)

    test = yamlTest(yamlFile)

    t = 0
    max_agent = None
    for agent_name in test.schedule:
        agent = test.schedule[agent_name]
        # if t < agent[-1]["t"]:
        #     t = max(t, agent[-1]["t"])
        #     max_agent = agent_name
        for i in range(0, len(agent)):
            print(type(agent[i]["x"]), agent[i]["y"])
    a = np.random.randint(0,10,[4,4])
    x, y = np.where(a > 4)
    print(a)
    print(x)
    print(y)
    a[a > 4] = 0
    print(a)
    # print(t, max_agent)