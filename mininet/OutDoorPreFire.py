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
    ap1 = net.addAccessPoint('ap1', cls=OVSKernelAP, ssid='ap1-ssid', channel='1', mode='g', position='-130,60,0', range=30)
    ap2 = net.addAccessPoint('ap2', cls=OVSKernelAP, ssid='ap2-ssid', channel='1', mode='g', position='-35,-35,0', range=30)
    ap3 = net.addAccessPoint('ap3', cls=OVSKernelAP, ssid='ap3-ssid', channel='1', mode='g', position='35,50,0', range=30)
    ap4 = net.addAccessPoint('ap4', cls=OVSKernelAP, ssid='ap4-ssid', channel='1', mode='g', position='140,20,0', range=30)
    ap5 = net.addAccessPoint('ap5', cls=OVSKernelAP, ssid='ap5-ssid', channel='1', mode='g', position='60,-48,0', range=30)
    ap6 = net.addAccessPoint('ap6', cls=OVSKernelAP, ssid='ap6-ssid', channel='1', mode='g', position='-70,-85,0', range=30)
    ap7 = net.addAccessPoint('ap7', cls=OVSKernelAP, ssid='ap7-ssid', channel='1', mode='g', position='-131,-55,0', range=30)

    info('*** Add hosts/stations\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    sta1 = net.addStation('sta1', ip='10.0.0.1', position='-130,70,0', range=15)
    #
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    sta2 = net.addStation('sta2', ip='10.0.0.2', position='-45,-25,0', range=15)
    #
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    sta3 = net.addStation('sta3', ip='10.0.0.3', position='35,60,0', range=15)
    #
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    sta4 = net.addStation('sta4', ip='10.0.0.4', position='140,30,0', range=15)
    #
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    sta5 = net.addStation('sta5', ip='10.0.0.5', position='55,-58,0', range=15)
    #
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    sta6 = net.addStation('sta6', ip='10.0.0.6', position='-75,-75,0', range=15)
    #
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    sta7 = net.addStation('sta7', ip='10.0.0.7', position='-141,-55,0', range=15)

    info("*** Configuring Propagation Model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info('*** Add links\n')
    net.addLink(sta1, ap1)
    net.addLink(h1, sta1)
    #
    net.addLink(sta2, ap2)
    net.addLink(h2, sta2)
    #
    net.addLink(sta3, ap3)
    net.addLink(h3, sta3)
    #
    net.addLink(sta4, ap4)
    net.addLink(h4, sta4)
    #
    net.addLink(sta5, ap5)
    net.addLink(h5, sta5)
    #
    net.addLink(sta6, ap6)
    net.addLink(h6, sta6)
    net.addLink(h8, sta6)
    net.addLink(h9, sta6)
    net.addLink(h10, sta6)
    net.addLink(h11, sta6)
    net.addLink(h12, sta6)
    net.addLink(h13, sta6)
    net.addLink(h14, sta6)
    net.addLink(h15, sta6)
    net.addLink(h16, sta6)
    #
    net.addLink(sta7, ap7)
    net.addLink(h7, sta7)

    #plot the network graph
    net.plotGraph(max_x=250, max_y=250)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info('*** Starting switches/APs\n')
    net.get('ap1').start([])
    net.get('ap2').start([])
    net.get('ap3').start([])
    net.get('ap4').start([])
    net.get('ap5').start([])
    net.get('ap6').start([])
    net.get('ap7').start([])

    info('*** Post configure nodes\n')

    CLI(net)
    net.stop()

if __name__== '__main__':
    setLogLevel('info')
    myNetwork()