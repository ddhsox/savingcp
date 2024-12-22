import os
import xml.etree.ElementTree as ET
from parametrs import MAX_COLORS

# Функция для сохранения палитры в XML файл
def save_palette_to_xml(palette, filename='palette.xml'):
    root = ET.Element("Palette")
    for color in palette:
        color_elem = ET.SubElement(root, "Color")
        color_elem.text = color
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


# Функция для загрузки палитры из XML файла
def load_palette_from_xml(filename='palette.xml'):
    if not os.path.exists(filename):
        return []

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Проверяем, не превышает ли количество цветов лимит
        colors = [elem.text for elem in root.findall("Color")]
        if len(colors) > MAX_COLORS:
            raise ValueError(f"File contains {len(colors)} colors, which exceeds the limit of {MAX_COLORS}.")

        return colors
    except ET.ParseError:
        raise ValueError("The file is corrupted or is not a valid XML file.")