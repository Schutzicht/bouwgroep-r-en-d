import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

queries = {
    "pool": "indoor pool luxury home interior",
    "wellness": "sauna interior home luxury",
    "marble": "marble tile floor interior luxury",
    "bathroom": "modern luxury bathroom interior bathtub",
    "toilet": "luxury guest toilet interior modern"
}

for name, query in queries.items():
    url = f"https://unsplash.com/napi/search/photos?query={urllib.parse.quote(query)}&per_page=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        data = json.loads(response)
        if data['results']:
            img_url = data['results'][0]['urls']['raw'] + "&q=80&w=1080&auto=format&fit=crop"
            print(f"Downloading {name} from {img_url} ...")
            urllib.request.urlretrieve(img_url, f"public/generated-projects-real/{name}.jpg")
            print(f"Successfully downloaded {name}")
        else:
            print(f"No results for {name}")
    except Exception as e:
        print(f"Error for {name}: {e}")
