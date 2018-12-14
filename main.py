import shutil
import time
import os

print("What file do you want to make backups of? (enter filename with extension)")
filename = str(input())
filename, extension = filename.split(".")[0], filename.split(".")[1]

print("With what interval do you want backups to be made? (enter float minutes)")
interval = float(input())

print("How many backups do you want of the file? (enter integer amount)")
backupcount = int(input())

print(f"You have chosen to make backups of '{filename}' with the filextension '{extension}' every '{interval}' minute(s) to '{backupcount}' different files")
print("Are these settings correct? (Y/N)")

if str(input()).lower() == "y":

    if not os.path.exists("backups"):
        os.makedirs("backups")

    currentbackup = 1

    while True:
        print(f"Waiting for {interval} minute(s)... Press 'ctrl+c' to cancel")
        time.sleep(interval * 60)

        shutil.copy2(f'{filename}.{extension}', f'backups/{filename}{currentbackup}.{extension}')

        print(f"Made a copy of '{filename}.{extension}', to 'backups/{filename}{currentbackup}.{extension}'")

        currentbackup += 1
        if currentbackup > backupcount:
            currentbackup = 1

