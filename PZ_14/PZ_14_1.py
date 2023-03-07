# В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным)
import re
f = open('radio_stations.txt', encoding="utf8")
for i in f:
    p = re.findall(r'(?<=://)[^/:]+', i)
    if len(p) > 0:
        p = re.search(r'(?<=://)[^/:]+', i)
        print(p.group(0))

