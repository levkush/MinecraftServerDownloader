# Minecraft server downloader
# By levkush

import os
import requests

# Print copyrite
print()
print("Minecraft server downloader")
print("By levkush")
print()

# Get version, core, folder
print("Input server folder (example: C:/Server):")
selectedfolder = input()

print("Input minecraft server version (example: 1.12, get latest 1.12 version):")
selectedversion = input()

print("Input minecraft server core (example: paper)")
selectedcore = input()

# Core and version list
versionlist = ("1.7", "1.8", "1.9", "1.10", "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18")
corelist = ("paper", "spigot", "bukkit", "vanilla")

# Check version and core
if selectedversion in versionlist:
	if selectedcore in corelist:
		pass
	else:
		print("Core unavaible.")
		input("Press any key to exit")
		exit()
	pass
else:
	print("Version unavaible.")
	input("Press any key to exit")
	exit()

# Function that detects and downloads core of the required version
def getcore(ver, selectedfolder, core):
	def downloadcore(url, fold, version):
		filename = fold + "/core.jar"
		try:
			r = requests.get(url, allow_redirects=True)
			open(filename, 'wb').write(r.content)
			Downloaded = "Core downloaded. Version " + version
		except Exception:
			Downloaded = "Core download failed."
			print(Downloaded)
			print("Press any key to exit")
			input()
			exit()
		return Downloaded

	if ver == "1.7":
		if core == "paper":
			print("Version is unavaible")
			input("Press any key to exit")
			exit()
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.7.10-SNAPSHOT-b1657.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.7.10-R0.1-20140808.005431-8.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.7.10/server/952438ac4e01b4d115c5fc38f891710c4941df29/server.jar", selectedfolder, ver)
	if ver == "1.8":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.8.8-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.8.8-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.8.9/server/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd/server.jar", selectedfolder, ver)
	if ver == "1.9":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.9.4-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.9.4-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.9.4/server/edbb7b1758af33d365bf835eb9d13de005b1e274/server.jar", selectedfolder, ver)
	if ver == "1.10":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.10.2-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.10.2-R0.1-SNAPSHOT-latest.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.10.2/server/3d501b23df53c548254f5e3f66492d178a48db63/server.jar", selectedfolder, ver)
	if ver == "1.11":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.11.2.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.11.2.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.11.2/server/f00c294a1576e03fddcac777c3cf4c7d404c4ba4/server.jar", selectedfolder, ver)
	if ver == "1.12":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.12.2.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.12.2.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/mc/game/1.12.2/server/886945bfb2b978778c3a0288fd7fab09d315b25f/server.jar", selectedfolder, ver)
	if ver == "1.13":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.13.2.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.13.2.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar", selectedfolder, ver)
	if ver == "1.14":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.14.4.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.14.4.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar", selectedfolder, ver)
	if ver == "1.15":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.15.2.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.15.2.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/4d1826eebac84847c71a77f9349cc22afd0cf0a1/server.jar", selectedfolder, ver)
	if ver == "1.16":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.16.5.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.16.5.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar", selectedfolder, ver)
	if ver == "1.17":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.17.1/builds/408/downloads/paper-1.17.1-408.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.17.1.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.17.1.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar", selectedfolder, ver)
	if ver == "1.18":
		if core == "paper":
			downloadcore("https://papermc.io/api/v2/projects/paper/versions/1.18.1/builds/141/downloads/paper-1.18.1-141.jar", selectedfolder, ver)
		if core == "spigot":
			downloadcore("https://cdn.getbukkit.org/spigot/spigot-1.18.1.jar", selectedfolder, ver)
		if core == "bukkit":
			downloadcore("https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.18.1.jar", selectedfolder, ver)
		if core == "vanilla":
			downloadcore("https://launcher.mojang.com/v1/objects/125e5adf40c659fd3bce3e66e67a16bb49ecc1b9/server.jar", selectedfolder, ver)
	return print("Core downloaded.")

isdr = os.path.isdir(selectedfolder)
if isdr == True:
	pass
else:
	os.system("mkdir " + selectedfolder)

print()
getcore(selectedversion, selectedfolder, selectedcore)
if os.name == 'nt':
	with open(selectedfolder + "/start.bat", "wt") as f:
		f.write("java -Xmx2048M -Xms1024M -jar core.jar nogui")
else:
	with open(selectedfolder + "/start.sh", "wt") as f:
		f.write("java -Xmx2048M -Xms1024M -jar core.jar nogui")
print("Startup files created.")
print("Server downloaded.")
print("")
print("Start server? (y/n)")
i = input("")
if i == "y" or "Y":
	print("Server is starting...")
	print()
	os.chdir(selectedfolder)
	os.system("java -Xmx2048M -Xms1024M -jar core.jar nogui")
else:
	print("Press any key to exit")
	input()
