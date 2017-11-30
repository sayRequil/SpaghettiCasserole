import json
class Pickle:
  def __init__(self,build):
    self.build = open(build,"a+")
    self.packs = {}
  def pack(self,*packs):
    for i,v in *packs:
      self.packs[i] = v
  def build(self):
    for i,v in self.packs:
      self.build.append("\"%s\": \"%s\"" % i,v)
    return self.build

class Load:
  def __init__(self,build_name):
    self.file = open(build_name).read()
  def get(file):
    return json.loads(self.file)[file]
  def export(file):
    return open(file,"w+").write(json.loads(self.file)[file])
