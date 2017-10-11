import requests
import sys
from jsontraverse.parser import JsonTraverseParser

if len(sys.argv) > 1:
  r = requests.get(f"https://www.reddit.com/r/{sys.argv[1]}.json", headers = {'User-agent': 'grpy 0.1'})
else:
  r = requests.get("https://www.reddit.com/r/python.json", headers = {'User-agent': 'grpy 0.1'})  

parser = JsonTraverseParser(r.text)

if parser.traverse("error") is None:
  for x in range(1,25):
    print(f"{x}. " + parser.traverse(f"data.children.{x-1}.data.title"))
else:
  print("Error")
  print(r.text)