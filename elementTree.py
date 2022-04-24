import xml.etree.ElementTree as eltree


def generate_xml(filename):
  root = eltree.Element('Catalog')
  m1 = eltree.Element("mobile")
  root.append(m1)

  b1 = eltree.SubElement(m1,"brand")
  b1.text = "Redmi"

  b2 = eltree.SubElement(m1, "price")
  b2.text = "6000"

  m2 = eltree.Element("mobile")
  root.append(m2)

  c1 = eltree.SubElement(m2, "brand")
  c1.text = "Samsung"

  c2 = eltree.SubElement(m2, "price")
  c2.text =" 7000"

  m3 = eltree.Element("mobile")
  root.append(m3)

  d1 = eltree.SubElement(m3, "brand")
  d1.text = "RealMe"

  d2 = eltree.SubElement(m3, "price")
  d2.text = "333222"

  tree = eltree.ElementTree(root)

  with open('./temp/'+filename, "wb") as files:
    tree.write(files)

if __name__ == "__main__":
  generate_xml('eltree.xml')