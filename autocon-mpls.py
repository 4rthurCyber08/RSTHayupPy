
rst_ip = crt.Dialog.Prompt("What is your RST IPv4 Address? ")

connections = [
	"/TELNET " + rst_ip + " 2017",
	"/TELNET " + rst_ip + " 2018",
	"/TELNET " + rst_ip + " 2019",
	"/TELNET " + rst_ip + " 2020",
	"/TELNET " + rst_ip + " 2021",
	"/TELNET " + rst_ip + " 2022",
	"/TELNET " + rst_ip + " 2023",
	"/TELNET " + rst_ip + " 2024",
	"/TELNET " + rst_ip + " 2025",
	"/TELNET " + rst_ip + " 2026",
	"/TELNET " + rst_ip + " 2027",
	"/TELNET " + rst_ip + " 2028",
]

crt.Screen.Synchronous = True

for connection in connections:
	crt.Session.ConnectInTab(connection)

crt.Screen.Synchronous = False
