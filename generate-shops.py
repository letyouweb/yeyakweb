import json
import os

# 샵 데이터 로드
with open('shop-data.json', 'r', encoding='utf-8') as f:
    shops = json.load(f)

# HTML 템플릿
html_template = """<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content="{description}" />
    <title>{title}</title>
    
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:url" content="https://yeyak.app/{shop_id}" />
    <meta property="og:image" content="https://yeyak.app/images/1_main_반려동물호텔.jpg" />
    
    <link as="style" crossorigin="" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" rel="stylesheet"/>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"/>
    
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Pretendard", -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
        }}
        
        body {{
            line-height: 1.6;
            color: #333;
            overflow-x: hidden;
        }}
        
        .hero {{
            background: linear-gradient(135deg, {color} 0%, {color}dd 100%);
            color: white;
            padding: 80px 20px;
            text-align: center;
        }}
        
        .hero h1 {{
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 20px;
        }}
        
        .hero p {{
            font-size: 20px;
            margin-bottom: 15px;
            opacity: 0.95;
        }}
        
        .btn-reserve {{
            display: inline-block;
            margin-top: 30px;
            padding: 18px 50px;
            background: white;
            color: {color};
            text-decoration: none;
            border-radius: 30px;
            font-weight: 700;
            font-size: 18px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }}
        
        .btn-reserve:hover {{
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 60px 20px;
        }}
        
        .section-title {{
            text-align: center;
            font-size: 36px;
            font-weight: 800;
            margin-bottom: 50px;
            color: #333;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }}
        
        .info-card {{
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            text-align: center;
        }}
        
        .info-card i {{
            font-size: 48px;
            color: {color};
            margin-bottom: 15px;
        }}
        
        .info-card h3 {{
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        
        .info-card p {{
            color: #666;
            line-height: 1.6;
        }}
        
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }}
        
        .service-item {{
            background: linear-gradient(135deg, {color}22 0%, {color}11 100%);
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s;
        }}
        
        .service-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        }}
        
        .service-item i {{
            font-size: 40px;
            color: {color};
            margin-bottom: 15px;
        }}
        
        .service-item h4 {{
            font-size: 18px;
            font-weight: 700;
            color: #333;
        }}
        
        .map-section {{
            background: #f8f9fa;
        }}
        
        .contact-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }}
        
        .contact-item {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        
        .contact-item i {{
            color: {color};
            margin-right: 10px;
        }}
        
        .contact-item h4 {{
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        
        .contact-item p {{
            color: #666;
        }}
        
        footer {{
            background: #2c3e50;
            color: white;
            text-align: center;
            padding: 30px 20px;
        }}
        
        footer p {{
            opacity: 0.8;
        }}
        
        footer a {{
            color: {color};
            text-decoration: none;
        }}
        
        @media (max-width: 768px) {{
            .hero h1 {{
                font-size: 32px;
            }}
            
            .hero p {{
                font-size: 16px;
            }}
            
            .section-title {{
                font-size: 28px;
            }}
        }}
    </style>
</head>
<body>

    <!-- Hero Section -->
    <section class="hero">
        <h1>🐾 {name}</h1>
        <p>{description}</p>
        <p>📍 {address}</p>
        <a href="https://예약봇.kr" class="btn-reserve">
            <i class="fas fa-calendar-check"></i> 지금 바로 예약하기
        </a>
    </section>

    <!-- 영업시간 & 연락처 -->
    <div class="container">
        <div class="info-grid">
            <div class="info-card">
                <i class="fas fa-clock"></i>
                <h3>영업시간</h3>
                <p>{hours}</p>
            </div>
            <div class="info-card">
                <i class="fas fa-phone"></i>
                <h3>전화문의</h3>
                <p>{phone}</p>
            </div>
            <div class="info-card">
                <i class="fab fa-instagram"></i>
                <h3>인스타그램</h3>
                <p>{instagram}</p>
            </div>
            <div class="info-card">
                <i class="fas fa-calendar-alt"></i>
                <h3>24시간 예약</h3>
                <p>온라인으로 편리하게</p>
            </div>
        </div>
    </div>

    <!-- 서비스 -->
    <div class="container">
        <h2 class="section-title">우리의 서비스</h2>
        <div class="services-grid">
            {services_html}
        </div>
    </div>

    <!-- 예약 안내 -->
    <div class="container" style="background: linear-gradient(135deg, {color}22 0%, {color}11 100%); border-radius: 30px; padding: 50px 40px; text-align: center;">
        <h2 class="section-title">온라인 예약 시스템</h2>
        <p style="font-size: 18px; margin-bottom: 30px; color: #666;">24시간 언제든지 편리하게 예약하세요!</p>
        <a href="https://예약봇.kr" class="btn-reserve">
            <i class="fas fa-calendar-check"></i> 예약하러 가기
        </a>
    </div>

    <!-- 오시는 길 -->
    <div class="container map-section">
        <h2 class="section-title">오시는 길</h2>
        <div class="contact-grid">
            <div class="contact-item">
                <h4><i class="fas fa-map-marker-alt"></i> 주소</h4>
                <p>{address}</p>
            </div>
            <div class="contact-item">
                <h4><i class="fas fa-subway"></i> 찾아오시는 길</h4>
                <p>전화로 문의해주세요</p>
            </div>
            <div class="contact-item">
                <h4><i class="fas fa-parking"></i> 주차</h4>
                <p>주차 가능 여부 문의</p>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <footer>
        <p>© 2024 {name}. All rights reserved.</p>
        <p style="margin-top: 10px; font-size: 14px;">Powered by <a href="https://yeyak.app">예약웹</a></p>
    </footer>

</body>
</html>
"""

service_icons = {
    "프리미엄 가위컷": "cut",
    "스타일컷": "star",
    "SPA 목욕": "spa",
    "애견호텔": "hotel",
    "픽업 서비스": "car",
    "가위컷 전문": "cut",
    "노견 케어": "heart",
    "피부 트러블 케어": "heartbeat",
    "발톱 관리": "paw",
    "독일식 그루밍": "scissors",
    "대형견 전문": "dog",
    "쇼컷": "award",
    "위생미용": "shower",
    "트렌디 스타일컷": "magic",
    "컬러링": "palette",
    "네일아트": "gem",
    "스파 패키지": "bath",
    "1:1 맞춤 미용": "user-tie",
    "아로마 테라피": "leaf",
    "치석 제거": "tooth",
    "피부 진정 케어": "medkit",
    "프리미엄 컷": "cut",
    "매직 SPA": "magic",
    "유치원": "school",
    "가위컷": "cut",
    "목욕&드라이": "shower",
    "발톱&귀 관리": "paw",
    "10년 경력": "award",
    "소형견 전문": "dog",
    "스트레스 최소화": "smile",
    "종합 미용": "scissors",
    "건강검진": "stethoscope",
    "호텔": "hotel",
    "놀이방": "gamepad",
    "미용": "cut",
    "훈련": "dumbbell",
    "스타일링": "brush",
    "아로마": "spa",
    "건강관리": "heartbeat",
    "상담": "comments",
    "용품": "shopping-bag",
    "24시간 호텔": "clock",
    "실시간 CCTV": "video",
    "픽업/배송": "truck"
}

# 각 샵별 HTML 생성
for shop_id, shop_data in shops.items():
    # 서비스 HTML 생성
    services_html = ""
    for service in shop_data['services']:
        icon = service_icons.get(service, "check")
        services_html += f"""
            <div class="service-item">
                <i class="fas fa-{icon}"></i>
                <h4>{service}</h4>
            </div>"""
    
    # HTML 생성
    html = html_template.format(
        shop_id=shop_id,
        name=shop_data['name'],
        title=shop_data['title'],
        description=shop_data['description'],
        address=shop_data['address'],
        phone=shop_data['phone'],
        hours=shop_data['hours'],
        instagram=shop_data['instagram'],
        color=shop_data['color'],
        services_html=services_html
    )
    
    # 파일 저장
    folder_path = f"{shop_id}"
    os.makedirs(folder_path, exist_ok=True)
    
    with open(f"{folder_path}/index.html", 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"[OK] {shop_data['name']} 페이지 생성 완료!")

print("\n[DONE] 모든 샵 페이지 생성 완료!")
