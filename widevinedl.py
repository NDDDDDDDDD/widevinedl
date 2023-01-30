import subprocess
from urllib.request import urlopen
import re
import os

dir = r"C:\Users\46735\Documents\downey"  # this directory should include downey.exe
mpd = input("enter MPD url: ")
mpdfile = urlopen(f"{mpd}")
with open(r'C:\Users\46735\Documents\downey\manifest.mpd','wb') as output:  # this has to be in the folder as downey.exe, mpd file shall be named manifest.mpd
  output.write(mpdfile.read())  # downloads manifest.mpd
licenseurl = input("enter license url: ")
cmdd = f"downey.exe --lic-server {licenseurl}"
rc = subprocess.check_output(cmdd, cwd=dir)  # catches decryption key
result = re.search(r"\B[a-z0-9]{16,}:[a-z0-9]{16,}", str(rc))
decryption_key = result.group()
os.system(f'N_m3u8DL-CLI_v3.0.2.exe {mpd}  --enableDelAfterDone --noMerge --enableMuxFastStart')  #downloading content in .mpd file
filename = input("enter file name: ") # VERY important step, the file name is located at the top of the new entries in your terminal.
os.system(fr'mp4decrypt.exe --key {decryption_key} C:\Users\46735\PycharmProjects\pythonProject\Downloads\{filename}.mp4 C:\Users\46735\PycharmProjects\pythonProject\Downloads\decrypted-video.mp4') # download will be located where you have your python file enter that path in all of these.
os.system(fr'mp4decrypt.exe --key {decryption_key} C:\Users\46735\PycharmProjects\pythonProject\Downloads\{filename}(Audio).aac C:\Users\46735\PycharmProjects\pythonProject\Downloads\decrypted-audio.aac')
name = input("enter final file name: ") # what the merged file will be called
os.system(fr'mkvmerge.exe -o C:\Users\46735\Documents\downey\{name}.mkv C:\Users\46735\PycharmProjects\pythonProject\Downloads\decrypted-video.mp4 C:\Users\46735\PycharmProjects\pythonProject\Downloads\decrypted-audio.aac')
