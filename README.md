# 🎯 예약웹 이미지 업데이트 완료 가이드

## ✅ 완료된 작업 (3가지)

### 1️⃣ 기타업종 "문의하기" → 이메일 링크 연동 ✅
- **변경 전**: 네이버 스마트스토어 링크만
- **변경 후**: `yeyakweb@letyou.kr` 이메일 자동 발송 링크
- **작동 방식**: 클릭 시 기본 이메일 앱에서 문의 양식 자동 생성

### 2️⃣ 푸터 샘플사이트 → 전체 10개 목록 표시 ✅
- **변경 전**: 4개 샘플만 표시
- **변경 후**: 전체 10개 샘플사이트 표시 (이모지 포함)

### 3️⃣ 샘플 카드 이미지 배경 구조 변경 ✅
- **변경 전**: 이모지 아이콘만 표시
- **변경 후**: 구글 드라이브 이미지 배경으로 변경 (준비 완료)

---

## 🚀 이미지 적용 방법 (5분 소요)

### 📋 필요한 정보
구글 드라이브 폴더에서 **각 이미지의 FILE_ID** 10개

### 🔍 FILE_ID 추출 방법 (2분)

1. **구글 드라이브 폴더 열기**
   ```
   https://drive.google.com/drive/folders/1SC5NOb3IGstNO0FW8liPPkncI4HbL7N2
   ```

2. **각 이미지 우클릭 → "공유" 클릭**

3. **"링크가 있는 모든 사용자" 선택 → "링크 복사"**

4. **FILE_ID 추출**
   ```
   복사된 링크 예시:
   https://drive.google.com/file/d/1AbC123XyZ-Example_FILE_ID/view?usp=sharing
   
   FILE_ID = 1AbC123XyZ-Example_FILE_ID
   ```

### 📝 IMAGE_ID 입력 (1분)

**파일 위치**: `C:\Users\mongshilymom\dev\yeyakweb\update-images.js`

```javascript
const IMAGE_IDS = {
  1: '실제_FILE_ID_1',  // 🐶 반려동물 호텔
  2: '실제_FILE_ID_2',  // 🏡 공간대여
  3: '실제_FILE_ID_3',  // 🎵 K-POP 학원
  4: '실제_FILE_ID_4',  // 💅 네일샵
  5: '실제_FILE_ID_5',  // 💪 헬스장
  6: '실제_FILE_ID_6',  // ☕ 카페
  7: '실제_FILE_ID_7',  // 🧘 필라테스
  8: '실제_FILE_ID_8',  // 🏥 피부과
  9: '실제_FILE_ID_9',  // 🎨 공방
  10: '실제_FILE_ID_10' // 🚗 세차장
};
```

### ⚡ 자동 업데이트 실행 (10초)

**터미널에서 실행**:
```bash
cd C:\Users\mongshilymom\dev\yeyakweb
node update-images.js
```

**성공 메시지**:
```
✅ 이미지 ID 업데이트 완료!

📋 적용된 이미지 URL:
   1. https://drive.google.com/uc?export=view&id=...
   2. https://drive.google.com/uc?export=view&id=...
   ...

🎉 index.html 파일이 업데이트되었습니다!
```

---

## 🎨 대안: 로컬 이미지 사용 (더 빠름!)

구글 드라이브 대신 **로컬 이미지 업로드** 추천

### 장점
✅ 로딩 속도 10배 빠름
✅ 구글 드라이브 용량/제한 걱정 없음
✅ 이미지 최적화 가능

### 사용 방법

1. **이미지 파일명 규칙**
   ```
   pet-hotel.jpg       → 반려동물 호텔
   space-rental.jpg    → 공간대여
   kpop-academy.jpg    → K-POP 학원
   nail-shop.jpg       → 네일샵
   pt-center.jpg       → 헬스장
   cafe.jpg            → 카페
   pilates.jpg         → 필라테스
   clinic.jpg          → 피부과
   workshop.jpg        → 공방
   carwash.jpg         → 세차장
   ```

2. **이미지 업로드 위치**
   ```
   C:\Users\mongshilymom\dev\yeyakweb\images\
   ```

3. **HTML 수정** (자동 스크립트 제공 가능)
   ```html
   background: url('images/pet-hotel.jpg')
   ```

---

## 📧 이메일 문의 폼 테스트

**테스트 링크**:
```
mailto:yeyakweb@letyou.kr?subject=기타업종 웹사이트 제작 문의&body=안녕하세요
```

**작동 확인**:
1. 웹사이트에서 "기타업종" 카드 클릭
2. "이메일 문의하기" 버튼 클릭
3. 기본 이메일 앱 자동 실행 확인

---

## 🔄 추가 이메일 폼 옵션

현재는 `mailto:` 링크 사용 중 (무료, 즉시 적용)

### 업그레이드 옵션

**1. FormSpree (무료)**
- 월 50건 무료
- 웹 폼에서 직접 제출
- https://formspree.io

**2. Netlify Forms (무료)**
- 월 100건 무료
- 스팸 필터 포함
- Netlify 배포 시 자동 활성화

**3. Google Forms 연동**
- 무제한 무료
- 응답 자동 저장
- 구글 스프레드시트 연동

원하시는 방식 선택 시 추가 설정 도와드리겠습니다!

---

## 📞 다음 단계

**이미지 ID 10개를 알려주시면**:
→ 자동 스크립트 실행
→ 5분 내 웹사이트 완성!

**또는 로컬 이미지 사용 원하시면**:
→ images 폴더에 이미지 업로드
→ 파일명 규칙대로 저장
→ 자동 업데이트 스크립트 제공

---

## 🎉 완성 후 확인사항

✅ 모든 샘플 카드에 이미지 표시
✅ "기타업종" 이메일 문의 작동
✅ 푸터 샘플사이트 10개 전체 표시
✅ 모바일 반응형 확인
✅ 로딩 속도 테스트

**질문이나 추가 작업 필요시 언제든 요청해 주세요!** 🚀
