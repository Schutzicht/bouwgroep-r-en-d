import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://unsplash.com/napi/search/photos?query=luxury+indoor+swimming+pool+water&per_page=3"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    data = json.loads(response)
    if data['results']:
        # Let's take the first one explicitly 
        img_url = data['results'][0]['urls']['raw'] + "&q=80&w=1080&auto=format&fit=crop"
        print(f"Downloading real swimming pool from {img_url} ...")
        urllib.request.urlretrieve(img_url, "public/generated-projects-real/pool.jpg")
        print("Successfully replaced pool.jpg")
except Exception as e:
    print(f"Error: {e}")
