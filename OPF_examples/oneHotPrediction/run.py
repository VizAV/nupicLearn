import csv
import datetime
from model_params import model_params
from nupic.frameworks.opf.model_factory import ModelFactory
import nupic_output
from nupic.data.inference_shifter import InferenceShifter
DATE_FORMAT = "%m/%d/%y %H:%M"
def createModel():
    model = ModelFactory.create(model_params.MODEL_PARAM)
    model.enableInference(
        {
            "predictedField":"kw_energy_consumption"
        }
    )
    return model

def runModel(model):
    inputFile = open("rec-center-hourly.csv","rb")
    csvReader = csv.reader(inputFile)
    csvReader.next()
    csvReader.next()
    csvReader.next()
    shifter = InferenceShifter()
    output= nupic_output.NuPICPlotOutput(['REC center'])

    counter = 0
    for row in csvReader:
        counter+=1
        if(counter %100 == 0):
            print("Read %i lines", counter)
        timestamp = datetime.datetime.strptime(row[0],DATE_FORMAT)
        consumption = float(row[1])


        result = model.run({
            "timestamp":timestamp,
            "kw_energy_consumption":consumption
        })

        result = shifter.shift(result)
        prediction = result.inferences["multiStepBestPredictions"][1]
        output.write([timestamp],[consumption],[prediction])

    inputFile.close()
    output.close()
def runHotGym():
    model = createModel()
    runModel(model)
if __name__=="__main__":
    runHotGym()