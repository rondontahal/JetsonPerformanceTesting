from jtop import jtop
import numpy
import csv
import json

if __name__ == "__main__":

    print("Gpu Data to Csv")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            #LoaD gPU
            for type,value in jetson.gpu:
                print(type, value)
                #j =json.dumps(jetson.gpu)
                #with open('GpuData.json','w') as f:
                    #f.write(j)
                    #f.close()








                