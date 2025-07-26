# Case Study: PT. TechnoEdu - Campus Network Redesign (FINAL VERSION)

from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Internet, CiscoRouter, CiscoSwitchL2, CiscoSwitchL3, HAProxy
from diagrams.onprem.compute import Server
from diagrams.onprem.database import MySQL, PostgreSQL
from diagrams.onprem.storage import Ceph  # Using available storage icon
from diagrams.onprem.security import Vault  # Using available security icon
from diagrams.generic.network import Firewall
from diagrams.onprem.monitoring import Grafana
from diagrams.generic.device import Tablet, Mobile
from diagrams.onprem.client import Users

# Main Enterprise Network Architecture
with Diagram("PT TechnoEdu - Enterprise Network Architecture", 
             show=False, 
             direction="TB"):
    
    # External Network
    with Cluster("External Network"):
        internet = Internet("Internet")
        users_external = Users("Remote Users\n(VPN)")
    
    # Edge/Perimeter Security
    with Cluster("Perimeter Security"):
        edge_firewall = Firewall("Edge Firewall\nFortiGate 200F")
        edge_router = CiscoRouter("Edge Router\nCisco ISR 4321")
    
    # DMZ Zone
    with Cluster("DMZ Zone"):
        dmz_firewall = Firewall("DMZ Firewall")
        load_balancer = HAProxy("Load Balancer\nHA-Proxy")
        
        with Cluster("Public Services"):
            web_server1 = Server("Web Server 1\n10.10.10.11")
            web_server2 = Server("Web Server 2\n10.10.10.12")
            mail_server = Server("Mail Server\n10.10.10.15")
            vpn_server = Server("VPN Server\n10.10.10.20")
    
    # Core Network Layer
    with Cluster("Core Network Layer"):
        core_switch1 = CiscoSwitchL3("Core Switch 1\nCisco 9300\n10.0.0.1")
        core_switch2 = CiscoSwitchL3("Core Switch 2\nCisco 9300\n10.0.0.2")
        
        # Redundant connection between core switches
        core_switch1 - Edge(label="HSRP/VRRP\nRedundancy", style="dashed", color="red") - core_switch2
    
    # Distribution Layer - Building A (Administration)
    with Cluster("Building A - Administration"):
        dist_switch_a = CiscoSwitchL3("Distribution SW-A\n10.1.0.1")
        
        with Cluster("VLAN 10 - Management"):
            access_sw_mgmt = CiscoSwitchL2("Access SW-MGMT\n10.10.0.1")
            mgmt_server = Server("Management\n10.10.0.10")
            monitoring = Grafana("Monitoring\n10.10.0.11")
            
        with Cluster("VLAN 20 - HR Department"):
            access_sw_hr = CiscoSwitchL2("Access SW-HR\n10.20.0.1")
            hr_workstations = [
                Tablet("HR-PC-01\n10.20.0.10"),
                Tablet("HR-PC-02\n10.20.0.11"),
                Tablet("HR-PC-03\n10.20.0.12")
            ]
            hr_printer = Server("HR Printer\n10.20.0.20")
        
        with Cluster("VLAN 30 - Finance"):
            access_sw_finance = CiscoSwitchL2("Access SW-FIN\n10.30.0.1")
            finance_workstations = [
                Tablet("FIN-PC-01\n10.30.0.10"),
                Tablet("FIN-PC-02\n10.30.0.11")
            ]
            finance_server = Server("Finance Server\n10.30.0.15")
    
    # Distribution Layer - Building B (Teaching Labs)
    with Cluster("Building B - Teaching Labs"):
        dist_switch_b = CiscoSwitchL3("Distribution SW-B\n10.2.0.1")
        
        with Cluster("VLAN 40 - Lab Network"):
            access_sw_lab1 = CiscoSwitchL2("Lab-1 Switch\n10.40.0.1")
            access_sw_lab2 = CiscoSwitchL2("Lab-2 Switch\n10.40.0.2")
            
            lab1_computers = [
                Tablet("LAB1-PC-01\n10.40.1.10"),
                Tablet("LAB1-PC-02\n10.40.1.11"),
                Tablet("LAB1-PC-03\n10.40.1.12"),
                Tablet("LAB1-PC-04\n10.40.1.13")
            ]
            
            lab2_computers = [
                Tablet("LAB2-PC-01\n10.40.2.10"),
                Tablet("LAB2-PC-02\n10.40.2.11"),
                Tablet("LAB2-PC-03\n10.40.2.12")
            ]
        
        with Cluster("VLAN 50 - Guest Network"):
            access_sw_guest = CiscoSwitchL2("Guest Switch\n10.50.0.1")
            guest_devices = [
                Mobile("Guest Phone 1"),
                Mobile("Guest Phone 2"),
                Tablet("Guest Laptop")
            ]
    
    # Distribution Layer - Building C (Data Center)
    with Cluster("Building C - Data Center"):
        dist_switch_c = CiscoSwitchL3("Distribution SW-C\n10.3.0.1")
        
        with Cluster("VLAN 60 - Production Servers"):
            server_switch1 = CiscoSwitchL2("Server SW-1\n10.60.0.1")
            server_switch2 = CiscoSwitchL2("Server SW-2\n10.60.0.2")
            
            production_servers = [
                Server("App Server 1\n10.60.0.10"),
                Server("App Server 2\n10.60.0.11"),
                Server("File Server\n10.60.0.15")
            ]
        
        with Cluster("VLAN 70 - Database Tier"):
            db_switch = CiscoSwitchL2("DB Switch\n10.70.0.1")
            primary_db = MySQL("Primary DB\n10.70.0.10")
            replica_db = MySQL("Replica DB\n10.70.0.11")
            backup_db = PostgreSQL("Backup DB\n10.70.0.12")
        
        with Cluster("VLAN 80 - Storage & Backup"):
            storage_switch = CiscoSwitchL2("Storage SW\n10.80.0.1")
            nas_storage = Ceph("Ceph Storage\n10.80.0.10")  # Using available Ceph icon
            backup_server = Server("Backup Server\n10.80.0.15")
            security_vault = Vault("Security Vault\n10.80.0.20")  # Using available Vault icon
    
    # Network Connections - External to Internal
    internet >> edge_firewall >> edge_router
    users_external >> vpn_server
    
    # DMZ Connections
    edge_router >> dmz_firewall >> load_balancer
    load_balancer >> [web_server1, web_server2]
    dmz_firewall >> mail_server
    dmz_firewall >> vpn_server
    
    # Core Layer Connections
    edge_router >> [core_switch1, core_switch2]
    
    # Distribution Layer Connections (Redundant)
    core_switch1 >> Edge(label="Primary", color="blue") >> dist_switch_a
    core_switch2 >> Edge(label="Backup", color="red", style="dashed") >> dist_switch_a
    
    core_switch1 >> Edge(label="Primary", color="blue") >> dist_switch_b  
    core_switch2 >> Edge(label="Backup", color="red", style="dashed") >> dist_switch_b
    
    core_switch1 >> Edge(label="Primary", color="blue") >> dist_switch_c
    core_switch2 >> Edge(label="Backup", color="red", style="dashed") >> dist_switch_c
    
    # Building A Connections
    dist_switch_a >> access_sw_mgmt >> [mgmt_server, monitoring]
    dist_switch_a >> access_sw_hr 
    access_sw_hr >> hr_workstations
    access_sw_hr >> hr_printer
    dist_switch_a >> access_sw_finance
    access_sw_finance >> finance_workstations
    access_sw_finance >> finance_server
    
    # Building B Connections  
    dist_switch_b >> [access_sw_lab1, access_sw_lab2, access_sw_guest]
    access_sw_lab1 >> lab1_computers
    access_sw_lab2 >> lab2_computers
    access_sw_guest >> guest_devices
    
    # Building C Connections
    dist_switch_c >> [server_switch1, server_switch2, db_switch, storage_switch]
    server_switch1 >> production_servers[0:2]  # App servers
    server_switch2 >> production_servers[2]    # File server
    db_switch >> [primary_db, replica_db, backup_db]
    storage_switch >> [nas_storage, backup_server, security_vault]
    
    # Inter-database replication
    primary_db >> Edge(label="Replication", style="dashed", color="green") >> replica_db
    primary_db >> Edge(label="Backup", style="dotted", color="orange") >> backup_db

print("✅ Enterprise Network Diagram Generated Successfully!")
print("📁 File: pt_techno_edu_enterprise_network_architecture.png")
print("\n📋 Network Summary:")
print("- 3 Buildings dengan hierarchical design")
print("- 8 VLANs untuk network segmentation")  
print("- Redundant core switches untuk high availability")
print("- DMZ zone untuk public services")
print("- Guest network isolation")
print("- Centralized data center dengan database replication")
print("- Ceph storage dan Vault security systems")
print("- 500+ device capacity dengan room for expansion")