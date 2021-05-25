CC = python3

run:
	$(CC) main.py

install_linux:
	sudo ./scripts/setupLinux.sh

install_mac:
	sudo ./scripts/setupMac.sh