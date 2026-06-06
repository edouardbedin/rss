from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# Création du flux RSS
rss = Element("rss", version="2.0")
channel = SubElement(rss, "channel")

# Infos du flux
SubElement(channel, "title").text = "Sofascore News"
SubElement(channel, "link").text = "https://www.sofascore.com/news"
SubElement(channel, "description").text = "Flux RSS des actualités sportives Sofascore"
SubElement(channel, "language").text = "fr-fr"

# Exemple d'article (tu peux en ajouter plusieurs)
item = SubElement(channel, "item")
SubElement(item, "title").text = "Dernières actualités Sofascore"
SubElement(item, "link").text = "https://www.sofascore.com/news"
SubElement(item, "guid").text = "https://www.sofascore.com/news"
SubElement(item, "pubDate").text = datetime.utcnow().strftime(
    "%a, %d %b %Y %H:%M:%S GMT"
)
SubElement(item, "description").text = "Actualités sportives, scores et analyses."

# Mise en forme XML propre
xml_str = minidom.parseString(tostring(rss)).toprettyxml(indent="  ")

# Sauvegarde du fichier RSS
with open("rss.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

print("✅ rss.xml créé avec succès")