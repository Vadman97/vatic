import json
import math
import os
import subprocess

def get_turkic_videos():
  with open("tmp", "wb") as out:
    subprocess.Popen(["turkic", "list"],
                     stdout = out, stderr = subprocess.STDOUT).wait()
    out.close()
    res = []
  with open("tmp", "rb") as vids:
    for line in vids:
      res.append(line.strip())
  return res

def dump_data(id):
  if not os.path.exists('data'):
    os.makedirs('data')
  subprocess.Popen([
    'turkic', 'dump', str(id), '-o', 'data/' + str(id) + '.json',
    '--json', '--merge', '--merge-threshold', str(0.5)
  ])

  #turkic dump identifier -o output.txt --json --merge --merge-threshold 0.5
  #turkic dump identifier -o output.txt --original-video /path/to/video.mp4

def compensate():
  #warn accepts the HIT but notifies the worker that their quality is low
  subprocess.Popen(['turkic', 'compensate', '--default', 'warn'])

if __name__ == "__main__":
  ids = get_turkic_videos()
  print ids
  for id in ids:
    dump_data(id)
  print("Saved all data to folder")
  compensate()
  print("Workers compensated!")

