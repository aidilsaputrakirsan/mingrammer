from diagrams import Diagram, Cluster
from diagrams.onprem.network import Internet, CiscoRouter, CiscoSwitchL2
from diagrams.onprem.compute import Server
from diagrams.generic.device import Tablet

with Diagram("Office Network", show=False, direction="TB"):
    internet = Internet("Internet")
    
    with Cluster("Office"):
        router = CiscoRouter("Cisco Router")
        switch = CiscoSwitchL2("Cisco Switch")
        
        with Cluster("Servers"):
            web_server = Server("Web Server")
            file_server = Server("File Server")
        
        with Cluster("Workstations"):
            pc1 = Tablet("PC-001")
            pc2 = Tablet("PC-002")
    
    internet >> router >> switch
    switch >> [web_server, file_server]
    switch >> [pc1, pc2]
