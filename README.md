# 🕸️ ASCII Network Topology Scanner

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> **"Know your network. Map your network."** 🌐

Ein leichtgewichtiges, aber mächtiges Kommandozeilen-Tool (CLI), das dein lokales Netzwerk dynamisch analysiert und eine visuelle, farbcodierte ASCII-Baumstruktur aller verbundenen Geräte direkt im Terminal generiert.

## 📸 Preview
<img width="706" height="421" alt="image" src="https://github.com/user-attachments/assets/0b3a6770-6129-4f7a-bf7a-fb7626832804" />


## ✨ Features

* **Dynamische Erkennung:** Liest die Kernel-Routing-Tabelle (`ip route`) aus, um das korrekte Subnetz und das Standard-Gateway automatisch zu finden.
* **OS-Parsing:** Erkennt das Betriebssystem des Host-Rechners (über `/etc/os-release`).
* **Deep Scan (Layer 2):** Nutzt ARP-Broadcasts (`scapy`), um auch Geräte zu finden, die nicht auf normale Pings (ICMP) antworten.
* **MAC Vendor Lookup:** Löst MAC-Adressen automatisch in die Namen der Hardware-Hersteller auf (z.B. Apple, AVM, Samsung).
* **Standalone:** Keine Verschmutzung globaler Python-Pakete dank automatischer `venv`-Kapselung in `/opt/`.

---

## 🚀 Installation

Dieses Tool wurde für maximale Kompatibilität entwickelt. Wähle einfach die Vorbereitungsschritte für dein Betriebssystem und führe danach das universelle Installations-Skript aus.

### 1. Voraussetzungen installieren

Je nach deiner Linux-Distribution benötigst du Git und die Standard-Python-Umgebung:

**Arch Linux / CachyOS / Manjaro:**
```bash
sudo pacman -S git python
```

**Ubuntu / Debian / Linux Mint:**
```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

**Fedora / RHEL / CentOS:**
```bash
sudo dnf install git python3
```

### 2. Tool klonen & installieren (Universell)

Egal welches Linux du nutzt, dieser Schritt ist überall gleich. Das Skript installiert das Tool sauber nach `/opt/networkscanner` und erstellt einen globalen Befehl.

```bash
# 1. Repository herunterladen
git clone [https://github.com/Sandroexe/network-scanner.git](https://github.com/Sandroexe/network-scanner.git)
cd network-scanner

# 2. Skript ausführbar machen
chmod +x install.sh

# 3. Installation starten
sudo ./install.sh
```

---

## 💻 Benutzung

Da das Tool tiefgreifende Netzwerkpakete (Layer 2) versendet, benötigt es Administratorrechte. Egal in welchem Verzeichnis du dich befindest, tippe einfach:

```bash
sudo networkscanner
```

Das Skript ermittelt selbstständig dein aktuelles Subnetz, scannt die Umgebung und baut den Strukturbaum auf.

## 🛠️ Unter der Haube

* Erstellt mit [Scapy](https://scapy.net/) für Paket-Manipulation.
* Visualisiert mit [Rich](https://rich.readthedocs.io/en/stable/) für die Cyber-Terminal-Ästhetik.
* Gekapselt in einer isolierten virtuellen Umgebung, um Paket-Konflikte im Host-System zu verhindern.

## Meine Hardware Konfiguration

* [CachyOS mit AMD Ryzen 7 9800x3d + RTX 5070 Asus TUF OC](https://github.com/Sandroexe/dotfiles)
* SSH über MacBook Terminal
