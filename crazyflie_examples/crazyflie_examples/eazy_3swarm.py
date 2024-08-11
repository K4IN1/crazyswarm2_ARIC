
from crazyflie_py import Crazyswarm
from crazyflie_py.crazyflie import Crazyflie
import numpy as np
import signal

name1 = 'cf1'
name3 = 'cf3'
pos11=np.array([1.0,1.0,0.5])
posn11=np.array([-1.0,-1.0,0.5])
swarm = Crazyswarm()
timeHelper = swarm.timeHelper
cf1:Crazyflie = swarm.allcfs.crazyfliesByName[name1]
cf3:Crazyflie = swarm.allcfs.crazyfliesByName[name3]
allcfs = swarm.allcfs
def keyInterHandler(Signal,Frame):
    position = {'x':0,'y':0,'z':0}
    allcfs.land(0.03,3.0)
    for cf in allcfs.crazyflies:
        cf:Crazyflie
        position['x']=cf.getParam('stateEstimate.x')
        position['y']=cf.getParam('stateEstimate.y')
        position['z']=cf.getParam('stateEstimate.z')
        # cf.land(0.03,3.0)
        print(cf.prefix,"land to ",f"{position['x']},{position['y']},0.03")
def main():
    signal.signal(signal.SIGINT,keyInterHandler)
    allcfs.takeoff(0.5,2.0)
    timeHelper.sleep(2.5)

    cf1.goTo(pos11,0,3.0)
    cf3.goTo(posn11,0,3.0)
    timeHelper.sleep(4.5)
    
    cf1.goTo(np.array([-0.5,0,0.5]),0,3.0)
    cf3.goTo(np.array([0.5,0,0.5]),0,3.0)
    timeHelper.sleep(4.5)

    allcfs.land(0.03,3.0)
    timeHelper.sleep(3.5)
if __name__ == '__main__':
    main()
