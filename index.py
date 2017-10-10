import requests
from jsontraverse.parser import JsonTraverseParser

r = requests.get("https://www.reddit.com/r/python.json")

parser = JsonTraverseParser(r.text)

if parser.traverse("error") is None:
  for x in range(1,25):
    print(f"{x}. " + parser.traverse(f"data.children.{x-1}.data.title"))
else:
  print("Error")