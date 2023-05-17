from jtop import jtop



if __name__ == "__main__":

    print("Import Data to Json")

    with jtop() as jetson:
        # jetson.ok() will provide the proper update frequency
        if jetson.ok():
            jetson.json('Save.json')
