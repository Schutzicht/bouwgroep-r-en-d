import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Hand-picked Luxury Indoor Swimming Pool (Photo ID: M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)
img_url = "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?q=80&w=1080&auto=format&fit=crop"
print(f"Downloading real swimming pool from {img_url} ...")
try:
    urllib.request.urlretrieve(img_url, "public/generated-projects-real/pool.jpg")
    print("Successfully replaced pool.jpg")
except Exception as e:
    print(f"Error: {e}")
