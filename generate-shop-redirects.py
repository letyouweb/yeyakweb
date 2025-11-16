import os

shops = {
    "ordinarymung": "오니너리 멍",
    "chardor": "샤도르",
    "hallohund": "할로훈트",
    "dgroo_o": "디그루오",
    "groomingtime": "그루밍타임",
    "petsalon": "펫살롱",
    "oodangdang": "우댕댕펫살롱",
    "미용하는강아지": "미용하는강아지",
    "puppy": "퍼피",
    "puppycare": "퍼피케어",
    "pet": "펫",
    "petcare": "펫케어",
    "pethotel": "펫호텔"
}

html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - 리다이렉트 중...</title>
    <script>
        window.location.replace('/shop/?shop={shop_id}');
    </script>
</head>
<body>
    <div style="display: flex; align-items: center; justify-content: center; height: 100vh; font-family: sans-serif;">
        <p>{name} 예약 페이지로 이동 중...</p>
    </div>
</body>
</html>
"""

for shop_id, shop_name in shops.items():
    html_content = html_template.format(shop_id=shop_id, name=shop_name)
    
    folder_path = shop_id
    os.makedirs(folder_path, exist_ok=True)
    
    with open(f"{folder_path}/index.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"[OK] {shop_name}")

print("\n[DONE] Complete!")
