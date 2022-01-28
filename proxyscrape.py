import urllib.request

req = urllib.request.Request("http://free-proxy-list.net/")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1")
sourcecode = urllib.request.urlopen(req)
part = str(sourcecode.read())
part = part.split("<tbody>")
part = part[1].split("</tbody>")
part = part[0].split("<tr><td>")
proxylist = ""
for proxy in part:
    proxy = proxy.split("</td><td>")
    try:
        proxylist=proxylist + proxy[0] + ":" + proxy[1] + "\n"
    except:
        pass
out_file = open("proxies.txt","w")
out_file.write(proxylist)
out_file.close()
