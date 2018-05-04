#Swarm is a description of what a the day looks like . Swarm is a permutation of the various models
import os
from nupic.swarming import permutations_runner
from swarm_description import SWARM_DESCRIPTION

#swarm description
def swarm(input_file):
    permWorkDir = os.path.abspath('swarm')
    if not os.path.exists(permWorkDir):
        os.mkdir(permWorkDir)
    permutations_runner.runWithConfig(
        SWARM_DESCRIPTION,
        {"maxWorkers":4,"overwrite": True},
        outputLabel="rec_center",
        outDir=permWorkDir,
        permWorkDir=permWorkDir
    )


if __name__=='__main__':
    swarm("rec-center-hourly.csv")