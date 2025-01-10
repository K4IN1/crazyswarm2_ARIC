
from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie
import numpy as np
import signal

name1 = 'cf1'
name3 = 'cf3'
pos11=np.array([0.3,0.3,0.5])
pos12=np.array([0.3,-0.3,0.5])
pos21=np.array([-0.3,0.3,0.5])
pos22=np.array([-0.3,-0.3,0.5])
swarm:Crazyswarm = Crazyswarm()
timeHelper = swarm.timeHelper
cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]
allcfs = swarm.allcfs
loopSignal = 1
def keyInterHandler(Signal,Frame):
    loopSignal = 0
    position = {'x':0,'y':0,'z':0}
    allcfs.land(0.03,3.0)
    print('emergency stop')
    for cf in allcfs.crazyflies:
        cf:Crazyflie
        cf.getParam
        position['x']=cf.getParam('stateEstimate.x')
        position['y']=cf.getParam('stateEstimate.y')
        # position['z']=cf.getParam('stateEstimate.z')
        # cf.land(0.03,3.0)
        print(cf.prefix,"land to ",f"{position['x']},{position['y']},0.03")
def main():
    signal.signal(signal.SIGINT,keyInterHandler)
    allcfs.takeoff(0.5,2.0)
    timeHelper.sleep(2.5)
    while(loopSignal):
        for _ in range(10):
            cf1.goTo(pos11,0,3.0)
            cf3.goTo(pos22,0,3.0)
        timeHelper.sleep(4.5)
        for _ in range(10):
            cf1.goTo(pos12,0,3.0)
            cf3.goTo(pos21,0,3.0)
        timeHelper.sleep(4.5)
        for _ in range(10):
            cf1.goTo(pos22,0,3.0)
            cf3.goTo(pos11,0,3.0)
        timeHelper.sleep(4.5)
        for _ in range(10):
            cf1.goTo(pos21,0,3.0)
            cf3.goTo(pos12,0,3.0)
        timeHelper.sleep(4.5)
    
    for _ in range(10):
        cf1.goTo(np.array([-0.5,0,0.5]),0,3.0)
        cf3.goTo(np.array([0.5,0,0.5]),0,3.0)
    timeHelper.sleep(4.5)

    allcfs.land(0.03,3.0)
    timeHelper.sleep(3.5)
if __name__ == '__main__':
    main()
