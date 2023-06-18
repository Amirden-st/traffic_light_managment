def initialize(grids=5,lanes=2,length=100):
    os.system("netgenerate --grid --grid.number="+str(grids)+" -L="+str(lanes)+" --grid.length="+str(length)+" --output-file=grid.net.xml")

def single(path,vehicles):
    os.system("netconvert -s grid.net.xml --o grid.net.xml --tls.rebuild --tls.default-type actuated")
    os.system(path + "randomTrips.py -n grid.net.xml -o flows.xml --begin 0 --end 1 --period 1 --flows "+str(vehicles))
    os.system("jtrrouter --flow-files=flows.xml --net-file=grid.net.xml --output-file=grid.rou.xml --begin 0 --end 10000 --accept-all-destinations")
    os.system(path + "generateContinuousRerouters.py -n grid.net.xml --end 10000 -o rerouter.add.xml")
    tree = ET.parse("grid.sumocfg")
    # root = tree.getroot()
    # for child in root:
    #     if (child.tag == 'output'):
    #         for child2 in child:
    #             child2.attrib['value'] = 'grid.output.xml'
    with open('grid.sumocfg', 'wb') as f:
        tree.write(f)
    os.system("sumo-gui -c grid.sumocfg --device.fcd.period 1000 ")

if __name__ == '__main__':
    import os
    import numpy as np
    # import analysis
    from matplotlib import pyplot as plt

    import xml.etree.ElementTree as ET
    path = "./tools/"
    # initialize()
    single(path,800)
    # analysis.plots(vehicles_arr)





