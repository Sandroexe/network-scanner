import platform
import ipaddress
import os
from scapy.all import ARP, Ether, srp, conf, get_if_addr, get_if_hwaddr
from rich.console import Console
from rich.tree import Tree
from mac_vendor_lookup import MacLookup

def get_system_info():
    """Sammelt alle dynamischen System- und Netzwerkdaten."""
    
    # 1. Gateway (Router) ermitteln
    try:
        gateway_ip = conf.route.route("0.0.0.0")[2]
    except:
        gateway_ip = None
        
    # 2. Lokale IP und MAC ermitteln
    try:
        local_ip = get_if_addr(conf.iface)
        local_mac = get_if_hwaddr(conf.iface)
    except:
        local_ip, local_mac = None, None

    # 3. Subnetz dynamisch aus der Routing-Tabelle berechnen (MIT FIX)
    target_subnet = None
    if local_ip:
        for dest, netmask, gw, iface, out_ip, metric in conf.route.routes:
            if out_ip == local_ip and gw == '0.0.0.0' and dest != 0:
                mask_bits = bin(netmask).count('1')
                # FIX: Ignoriere /32 Host-Routen und suche das echte Subnetz
                if mask_bits < 32:
                    network_ip = ipaddress.IPv4Address(dest)
                    target_subnet = f"{network_ip}/{mask_bits}"
                    break
                
    # Fallback, falls die Tabelle nicht gelesen werden konnte
    if not target_subnet and local_ip:
        ip_parts = local_ip.split('.')
        target_subnet = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"

    # 4. Betriebssystem exakt erkennen
    os_name = "Dein PC"
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release') as f:
                for line in f:
                    if line.startswith('PRETTY_NAME='):
                        os_name = line.split('=')[1].strip().strip('"')
                        break
        else:
            os_name = platform.system() + " System"
    except:
        pass

    return target_subnet, gateway_ip, local_ip, local_mac, os_name

def scan_network():
    console = Console()
    mac_finder = MacLookup()
    
    # Dynamische Daten abrufen
    target_subnet, gateway_ip, local_ip, local_mac, os_name = get_system_info()
    
    if not target_subnet:
        console.print("[bold red]Fehler: Konnte lokales Subnetz nicht ermitteln.[/bold red]")
        return

    console.print(f"\n[bold cyan][*] Analysiere Netzwerk-Topologie für:[/bold cyan] [bold yellow]{target_subnet}[/bold yellow]...\n")
    
    # ARP-Scan durchführen
    arp_request = ARP(pdst=target_subnet)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=0)[0]
    
    clients = []
    for element in answered_list:
        clients.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
        
    clients = sorted(clients, key=lambda x: ipaddress.IPv4Address(x["ip"]))
    
    def get_vendor(mac_address):
        try:
            vendor = mac_finder.lookup(mac_address)
            return vendor[:20] + "..." if len(vendor) > 20 else vendor
        except:
            return "Unbekannt"

    # --- LOGISCHE TOPOLOGIE ZEICHNEN ---
    tree = Tree(f"[bold red]🌐 Lokales Netzwerk ({target_subnet})[/bold red]")
    
    # Ebene 1: Router
    gateway_client = next((c for c in clients if c["ip"] == gateway_ip), None)
    if gateway_client:
        router_mac = gateway_client["mac"]
        router_vendor = get_vendor(router_mac)
        router_node = tree.add(f"[bold yellow]🏠 Router (Gateway):[/bold yellow] {gateway_ip:15} [dim]>[/dim] MAC: {router_mac} [dim]>[/dim] [bold magenta]{router_vendor}[/bold magenta]")
    else:
        router_node = tree.add(f"[bold yellow]🏠 Router (Gateway):[/bold yellow] {gateway_ip} [dim](Nicht erreichbar)[/dim]")
    
    # Ebene 2: Dieser PC (Scanner)
    if local_ip:
        router_node.add(f"[bold green]💻 Scanner-Host:[/bold green] {local_ip:15} [dim]>[/dim] MAC: {local_mac} [dim]>[/dim] [bold magenta]{os_name}[/bold magenta]")
    
    # Ebene 2: Weitere Geräte
    devices_node = router_node.add("[bold cyan]🖧 Weitere verbundene Geräte:[/bold cyan]")
    
    found_others = False
    for client in clients:
        if client["ip"] == gateway_ip or client["ip"] == local_ip:
            continue 
            
        found_others = True
        ip = client["ip"]
        mac = client["mac"]
        vendor = get_vendor(mac)
        
        devices_node.add(f"[bold white]IP:[/bold white] {ip:15} [dim]>>>[/dim] [bold blue]MAC:[/bold blue] {mac} [dim]>>>[/dim] [bold magenta]Gerät:[/bold magenta] {vendor}")
        
    if not found_others:
         devices_node.add("[dim]Keine weiteren Geräte gefunden.[/dim]")
         
    console.print(tree)
    console.print("\n[dim]Topologie-Mapping abgeschlossen.[/dim]\n")

if __name__ == "__main__":
    try:
        MacLookup().update_vendors()
    except:
        pass
        
    scan_network()
