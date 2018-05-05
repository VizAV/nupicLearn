#Swarm is a description of what a the day looks like . Swarm is a permutation of the various models
import os
import pprint
from nupic.swarming import permutations_runner
from swarm_description import SWARM_DESCRIPTION

def writeModelParams(modelParams):
    outDir = os.path.join(os.getcwd(),"model_params")
    if not os.path.isdir(outDir):
         os.mkdir(outDir)
    outpath = os.path.join(outDir, "model_params.py")
    pp=pprint.PrettyPrinter(indent=2)
    with open(outpath,"wb") as outFiles:
        modelParamString = pp.pformat(modelParams)
        outFiles.write("MODEL_PARAM = \\\n%s" %modelParamString)
    return outpath


#swarm description
def swarm(input_file):
    permWorkDir = os.path.abspath('swarm')
    if not os.path.exists(permWorkDir):
        os.mkdir(permWorkDir)
    model_params = permutations_runner.runWithConfig(
        SWARM_DESCRIPTION,
        {"maxWorkers":4,"overwrite": True},
        outputLabel="rec_center",
        outDir=permWorkDir,
        permWorkDir=permWorkDir
    )
    writeModelParams(model_params)


if __name__=='__main__':
    swarm("rec-center-hourly.csv")