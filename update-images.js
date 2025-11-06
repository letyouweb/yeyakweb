const fs = require('fs');
const path = require('path');

// ========================================
// 🎯 구글 드라이브 이미지 ID 설정
// ========================================
// 아래 YOUR_IMAGE_ID_X 부분을 실제 구글 드라이브 파일 ID로 교체하세요
const IMAGE_IDS = {
  1: 'YOUR_IMAGE_ID_1',  // 🐶 반려동물 호텔 (예약봇.kr)
  2: 'YOUR_IMAGE_ID_2',  // 🏡 공간대여/파티룸 (yeyakbot.com)
  3: 'YOUR_IMAGE_ID_3',  // 🎵 K-POP 학원 (simulatordrone.com)
  4: 'YOUR_IMAGE_ID_4',  // 💅 네일샵/미용실 (idpix.app)
  5: 'YOUR_IMAGE_ID_5',  // 💪 헬스장/PT센터 (24bot.kr)
  6: 'YOUR_IMAGE_ID_6',  // ☕ 카페/디저트 (idpix.photo)
  7: 'YOUR_IMAGE_ID_7',  // 🧘 필라테스/요가 (yeyakbot.kr)
  8: 'YOUR_IMAGE_ID_8',  // 🏥 피부과/의원 (kloopi.app)
  9: 'YOUR_IMAGE_ID_9',  // 🎨 공방/원데이클래스 (yeyakbot.co.kr)
  10: 'YOUR_IMAGE_ID_10' // 🚗 세차/손세차 (예약봇.com)
};

// ========================================
// 🚀 자동 업데이트 실행
// ========================================
const htmlFilePath = path.join(__dirname, 'index.html');

try {
  // HTML 파일 읽기
  let htmlContent = fs.readFileSync(htmlFilePath, 'utf8');
  
  // 각 이미지 ID 교체
  Object.entries(IMAGE_IDS).forEach(([num, id]) => {
    const placeholder = `YOUR_IMAGE_ID_${num}`;
    const newUrl = `https://drive.google.com/uc?export=view&id=${id}`;
    htmlContent = htmlContent.replace(new RegExp(placeholder, 'g'), id);
  });
  
  // HTML 파일 저장
  fs.writeFileSync(htmlFilePath, htmlContent, 'utf8');
  
  console.log('✅ 이미지 ID 업데이트 완료!');
  console.log('\n📋 적용된 이미지 URL:');
  Object.entries(IMAGE_IDS).forEach(([num, id]) => {
    console.log(`   ${num}. https://drive.google.com/uc?export=view&id=${id}`);
  });
  console.log('\n🎉 index.html 파일이 업데이트되었습니다!');
  console.log('브라우저에서 새로고침하여 확인하세요.\n');
  
} catch (error) {
  console.error('❌ 오류 발생:', error.message);
  process.exit(1);
}
