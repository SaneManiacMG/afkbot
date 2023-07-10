import psutil
import subprocess

# get list of running processes
processes = psutil.process_iter()

teams_running = False
# iterate over list of active processes
for process in psutil.process_iter(['name']):
    # if process already running, stop script
    if process.info['name'] == "Teams.exe":
        print("Teams is already running!\n")
        teams_running = True
        break

# if process not running, start it
if not teams_running:
    try:
        subprocess.Popen(
            r"C:\Users\Mapap\AppData\Local\Microsoft\Teams\Update.exe --processStart Teams.exe")
        print("Starting Teams...\n")
    except FileNotFoundError:
        print("Could not find Teams.exe!\n")
else:
    print("Exiting teams startup function.\n")
