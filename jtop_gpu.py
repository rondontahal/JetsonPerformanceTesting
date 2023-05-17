from jtop import jtop
import json


if __name__ == "__main__":

    print("Gpu Reader")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            # Print all gpu
            for idx in enumerate(jetson.gpu):
                print("------{idx} ------".format(idx=idx))
                for key, value in jetson.gpu.items():
                    print("{key}: {value}".format(key=key, value=value))
            # read aggregate GPU status
            total = jetson.gpu
            print("------ GPU TOTAL ------")
            for key, value in total.items():
                print("{key}: {value}".format(key=key, value=value))
                j =json.dumps(jetson.gpu)
                with open('GpuData.json','w') as f:
                    f.write(j)
                    f.close()
# EOF