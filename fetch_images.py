import urllib.request
import urllib.parse
import re
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = {
    "pool": "site:unsplash.com indoor private home swimming pool interior",
    "wellness": "site:unsplash.com luxury home sauna interior wood",
    "marble": "site:unsplash.com luxury marble floor tiles interior",
    "bathroom": "site:unsplash.com luxury modern bathroom interior bathtub",
    "toilet": "site:unsplash.com luxury modern toilet guest bathroom"
}

for name, query in queries.items():
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})
    try:
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        # find github/unsplash urls
        matches = re.findall(r'https://unsplash\.com/photos/[a-zA-Z0-9\-]+', html)
        if matches:
            photo_id = matches[0].split('/')[-1].split('-')[-1]
            if len(photo_id) > 5:
                img_url = f"https://images.unsplash.com/photo-{photo_id}?q=80&w=1080&auto=format&fit=crop"
                print(f"Match for {name}: {img_url}")
                urllib.request.urlretrieve(img_url, f"public/generated-projects-real/{name}.jpg")
            else:
                print(f"Skipping {matches[0]}")
        else:
            print(f"No matches for {name}")
    except Exception as e:
        print(f"Error for {name}: {e}")
