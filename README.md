# 🕸️ ASCII Network Topology Scanner

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux-lightgrey?style=flat-square&logo=linux)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> **"Know your network. Map your network."** 🌐

Ein leichtgewichtiges, aber mächtiges Kommandozeilen-Tool (CLI), das dein lokales Netzwerk dynamisch analysiert und eine visuelle, farbcodierte ASCII-Baumstruktur aller verbundenen Geräte direkt im Terminal generiert.

## 📸 Preview
<img width="709" height="623" alt="image" src="https://github.com/user-attachments/assets/74d910f9-3840-4a1c-a4e4-0b8299762677" />

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

---

## 📦 Versionen & Updates

Dieses Projekt nutzt [GitHub Releases](https://github.com/Sandroexe/network-scanner/releases) zur Versionierung. 

* Wenn du immer den allerneuesten (aber vielleicht noch in Entwicklung befindlichen) Code möchtest, nutze den `git clone`-Befehl aus der Installationsanleitung oben.
* Wenn du eine **stabile, ältere Version** installieren möchtest:
  1. Gehe oben rechts auf **Releases**.
  2. Lade dir den Source Code (`.zip` oder `.tar.gz`) der gewünschten Version herunter.
  3. Entpacke den Ordner, öffne darin ein Terminal und führe das `install.sh` Skript aus.

---

## 🛠️ Unter der Haube

* Erstellt mit [Scapy](https://scapy.net/) für Paket-Manipulation.
* Visualisiert mit [Rich](https://rich.readthedocs.io/en/stable/) für die Cyber-Terminal-Ästhetik.
* Gekapselt in einer isolierten virtuellen Umgebung, um Paket-Konflikte im Host-System zu verhindern.

  ---

## 🖥️ Mein Setup & Dotfiles

Dieses Tool wurde auf meinem täglichen Driver unter **CachyOS** (Arch Linux) mit einem AMD Ryzen 7 9800X3D und einer RTX 5070 geschrieben und getestet. 

Wenn dir die Cyber-Terminal-Ästhetik, meine Fish-Shell-Konfiguration oder das generelle Linux-Setup gefallen, schau dir gerne an, wie mein System unter der Haube konfiguriert ist:

👉 **[Schau dir mein Dotfiles-Repository an!](https://github.com/Sandroexe/dotfiles)** 
