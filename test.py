from diagrams import Diagram
from diagrams.onprem.network import Internet, CiscoRouter, CiscoSwitchL2
from diagrams.onprem.compute import Server

with Diagram("My First Network", show=False):
    Internet("Internet") >> CiscoRouter("Core Router") >> CiscoSwitchL2("24-Port Switch") >> Server("Web Server")
