import os

def cwd():
  path = os.getcwd()
  print(f"Current Working Directory: {path}")
  print("the directory contains following files:")
  for file in os.listdir(path):
      print(file)

def run():
  print("processing....")
  cwd()

run()