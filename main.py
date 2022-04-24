from xml.dom import minidom

import os

root = minidom.Document()
xml = root.createElement('Root')

root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute("name", "Hello world")

xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t")

save_path = "./temp/test.xml"

with open(save_path,"w") as f:
  f.write((xml_str))