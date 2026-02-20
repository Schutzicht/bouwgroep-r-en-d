import urllib.request
import re

searches = {
    "pool": "https://unsplash.com/s/photos/indoor-private-pool",
    "wellness": "https://unsplash.com/s/photos/home-sauna",
    "marble": "https://unsplash.com/s/photos/marble-floor-tile-interior",
    "bathroom": "https://unsplash.com/s/photos/luxury-modern-bathroom",
    "toilet": "https://unsplash.com/s/photos/modern-toilet-interior"
}

for name, url in searches.items():
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        matches = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9\-]+', html)
        if matches:
            img_url = matches[0] + "?q=80&w=1080&auto=format&fit=crop"
            print(f"Downloading {name} from {img_url} ...")
            urllib.request.urlretrieve(img_url, f"public/generated-projects-real/{name}.jpg")
    except Exception as e:
        print(f"Failed {name}: {e}")

