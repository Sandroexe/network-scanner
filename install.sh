#!/bin/bash

# Farben für coole Terminal-Ausgaben
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}[*] Starte Installation des Network Scanners...${NC}"

# Zielverzeichnis definieren
INSTALL_DIR="/opt/networkscanner"

echo -e "${CYAN}[*] Erstelle Installationsverzeichnis in ${INSTALL_DIR}...${NC}"
sudo mkdir -p $INSTALL_DIR
sudo cp scanner.py $INSTALL_DIR/
sudo cp requirements.txt $INSTALL_DIR/

echo -e "${CYAN}[*] Richte isolierte Python-Umgebung ein...${NC}"
sudo python3 -m venv $INSTALL_DIR/venv
sudo $INSTALL_DIR/venv/bin/pip install -r $INSTALL_DIR/requirements.txt > /dev/null 2>&1

echo -e "${CYAN}[*] Erstelle globalen System-Befehl...${NC}"
sudo bash -c "cat > /usr/local/bin/networkscanner <<EOF
#!/bin/bash
sudo $INSTALL_DIR/venv/bin/python $INSTALL_DIR/scanner.py
EOF"
sudo chmod +x /usr/local/bin/networkscanner

echo -e "${GREEN}[+] Installation erfolgreich!${NC}"
echo -e "Du kannst das Tool jetzt jederzeit und überall mit dem Befehl ${CYAN}sudo networkscanner${NC} starten."
