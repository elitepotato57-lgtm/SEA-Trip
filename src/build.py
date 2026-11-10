"""Builds the app. Run from the src folder:  python build.py
1. runs data.py (which pulls in thai.py) to write data.json
2. drops the data, country outlines and Leaflet CSS into template.html
3. writes ../index.html, the single file GitHub Pages serves
"""
import os, re, subprocess, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.run([sys.executable, "data.py"], check=True)
rd = lambda p: open(p, encoding="utf-8").read()
t = rd("template.html")
css = rd("vendor/leaflet.css")
css = re.sub(r'[a-zA-Z-]+:\s*url\([^)]*\);?', '', css); css = re.sub(r'/\*.*?\*/', '', css, flags=re.S); css = re.sub(r'\s+', ' ', css)
out = t.replace('/*__LEAFLET_CSS__*/', css).replace('__GEO__', rd("countries.json")).replace('__DATA__', rd("data.json"))
assert '__DATA__' not in out and '__GEO__' not in out
HEAD = '''<title>SE Asia Trip</title>
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="SEA Trip">
<script src="config.js"></script>

'''
SW = '''<script>
if ("serviceWorker" in navigator && location.protocol === "https:" && !/claude\\.ai|claudeusercontent/.test(location.hostname)) {
  window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
}
</script>
</body>'''
assert out.count('<title>SE Asia trip app</title>') == 1 and out.count('</body>') == 1
out = out.replace('<title>SE Asia trip app</title>\n', HEAD).replace('</body>', SW)
open("../index.html", "w", encoding="utf-8", newline="\n").write(out)
print("Built ../index.html,", len(out) // 1024, "KB, version", re.search(r'const VERSION = "([^"]+)"', out).group(1))
