from mininet.node import Host
from mininet.log import setLogLevel, info
from mn_wifi.net import Mininet_wifi
from mn_wifi.node import Station, OVSKernelAP
from mn_wifi.cli import CLI
from mn_wifi.link import wmediumd
from mn_wifi.wmediumdConnector import interference
from subprocess import call

def myNetwork():
    
    net = Mininet_wifi(topo=None, build=False, link=wmediumd, wmediumd_mode=interference, ipBase='10.0.0.0/8')

    info('*** Adding controller\n')
    info('*** Add switches/APs\n')
    #IS DESTROYED#ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid', channel='1', mode='g', position='0,0,0', range=8.75)
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid', channel='1', mode='g', position='9.5,5,0', range=12)
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid', channel='1', mode='g', position='17,20,0', range=8.75)
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid', channel='1', mode='g', position='30,10,0', range=8.75)
    
    info('*** Add hosts/stations\n')
    sta1 = net.addStation('sta1', ip='10.0.0.1', position='1,2,0', range=5)
    sta2 = net.addStation('sta2', ip='10.0.0.2', position='11,7,0', range=5)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    sta3 = net.addStation('sta3', ip='10.0.0.3', position='18,22,0', range=5)
    sta4 = net.addStation('sta4', ip='10.0.0.4', position='31,12,0', range=5)
    
    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info('*** Add links\n')
    net.addLink(h3, ap3)

    #plot the network graph
    net.plotGraph(max_x=50, max_y=50)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches/APs\n')
    #IS DESTROYED#net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])

    info('*** Post configure nodes\n')

    CLI(net)
    net.stop()

if __name__== '__main__':
    setLogLevel('info')
    myNetwork()