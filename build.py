# -*- coding: utf-8 -*-
# 사용법: 아래 COMPANY 만 바꾸고  python3 build.py  를 실행하면 모든 페이지에 반영됩니다.
import os
TITLE_NAME = "청운투자그룹"   # 브라우저 탭 제목에 쓰는 이름
COMPANY = "청운"             # <- 회사명은 여기 한 곳만 수정
LEGAL = "주식회사 청운파트너스"
ADDRESS = "서울 영등포구 영등포로 150 (당산1가) 생각공장 당산 B동 13F"
SHOW_POPUP = True            # 사칭 주의 팝업 (끄려면 False)
PHONE   = "02-786-1005"
SITE_URL = "https://hoon6653.github.io/cheongwoon-site/"   # 도메인 연결 후 https://도메인/ 로 변경
OUT = os.path.dirname(os.path.abspath(__file__))
C = COMPANY

HEAD = '''<!DOCTYPE html>
<html lang="ko" class="js-off">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>@TITLE@</title>
<meta name="description" content="@DESC@">
<link rel="canonical" href="@URL@">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="favicon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="{TN}">
<meta property="og:title" content="@TITLE@">
<meta property="og:description" content="@DESC@">
<meta property="og:url" content="@URL@">
<meta property="og:image" content="@IMG@">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;800&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header><div class="wrap">
<a class="brand" href="index.html"><img src="assets/img/logo.svg" alt="{C}"></a>
<button class="burger" aria-expanded="false" aria-label="메뉴 열기">메뉴</button>
<nav aria-label="주요 메뉴"><ul>
<li><a href="about.html">회사소개</a><ul class="sub"><li><a href="about.html#greeting">대표 인사말</a></li><li><a href="about.html#overview">회사개요</a></li><li><a href="about.html#location">오시는 길</a></li></ul></li>
<li><a href="business.html">사업분야</a></li>
<li><a href="service.html">서비스 안내</a></li>
<li><a href="experts.html">{C} 전문가</a></li>
<li><a href="reviews.html">고객후기</a></li>
<li><a href="notice.html">커뮤니티</a><ul class="sub"><li><a href="notice.html#notice">공지사항</a></li><li><a href="notice.html#press">보도자료</a></li></ul></li>
</ul></nav>
<a class="tel" href="tel:{PHONE}">전화상담</a>
</div></header>
<main>
'''
FOOT = '''</main>
<footer><div class="wrap">
상호: {LEGAL}<br>
본점 : 서울특별시 영등포구 영등포로 150, 13층 (당산동 1가 459, 당산 생각공장)<br>
사업자등록번호 652-81-03582 ㅣ 전화번호: {PHONE}<br>
Copyright &copy; All Rights Reserved.
</div></footer>
@EXTRA@
<script src="assets/main.js"></script>
</body>
</html>
'''
def fill(s): return s.replace('{LEGAL}', LEGAL).replace('{ADDR}', ADDRESS).replace('{C}', C).replace('{PHONE}', PHONE).replace('{TN}', TITLE_NAME)
def sub(en, img): return '<div class="subhero" style="background-image:linear-gradient(rgba(15,42,71,.62),rgba(15,42,71,.62)),url(assets/img/%s)"><div class="wrap"><h1>%s</h1></div></div>\n' % (img, en)
def tabs(items): return '<div class="wrap"><nav class="tabs" aria-label="하위 메뉴">'+''.join('<a href="#%s">%s</a>'%i for i in items)+'</nav></div>\n'
def board(n=0):
    rows = '<tr><td colspan="5">등록된 글이 없습니다.</td></tr>' if n == 0 else ''
    return ('<div class="board-top"><span>전체 %d</span></div><table><thead><tr><th>번호</th><th>제목</th><th>작성자</th><th>작성일</th><th>조회</th></tr></thead><tbody>%s</tbody></table>'
            '<form class="search"><select aria-label="검색 범위"><option>제목</option><option>내용</option></select><input type="search" aria-label="검색어"><button>검색</button></form>') % (n, rows)
DESCS = {
 'index.html': '청운투자그룹 - 데이터 기반 시장 분석과 합리적인 투자 관점을 제공하는 투자사. 사업분야, 서비스 안내, 청운 전문가를 소개합니다.',
 'about.html': '청운투자그룹 회사소개. 대표 인사말, 회사개요, 오시는 길을 안내합니다.',
 'business.html': '청운투자그룹의 사업분야. 투자 교육, 시장 분석, 투자 전략 컨설팅 등 주요 사업을 소개합니다.',
 'service.html': '청운투자그룹 서비스 안내. 등급별 서비스 구성과 이용 방법을 안내합니다.',
 'experts.html': '청운투자그룹 전문가. 투자 전략과 시장 분석을 이끄는 전문가진을 소개합니다.',
 'reviews.html': '청운투자그룹 고객후기. 고객이 남긴 이야기를 확인하세요.',
 'notice.html': '청운투자그룹 커뮤니티. 공지사항과 보도자료를 확인하세요.',
}
PAGES = []
def page(name, title, body, extra=''):
    PAGES.append(name)
    url = SITE_URL + ('' if name == 'index.html' else name)
    head = (HEAD.replace('@DESC@', DESCS.get(name, TITLE_NAME)).replace('@URL@', url)
                .replace('@IMG@', SITE_URL + 'assets/img/hero-sky1.jpg').replace('@TITLE@', title))
    html = head + body + FOOT.replace('@EXTRA@', extra)
    open(os.path.join(OUT, name), 'w', encoding='utf-8').write(fill(html))

POPUP = '''<div class="pop" id="pop" role="dialog" aria-modal="true" aria-labelledby="pt"><div class="box">
<button type="button" class="pop-x" id="xbtn" aria-label="닫기"></button>
<span class="pop-chip">&#9888; 사칭 주의 안내</span>
<h2 id="pt">{TN} 사칭 사기에 주의하세요</h2>
<p>전문가의 실명·사진·경력을 도용해 고수익을 미끼로 접근하는 보이스피싱이 확산되고 있습니다.</p>
<div class="pop-warn">{TN}은 해외선물·지수 거래 리딩을 일절 진행하지 않습니다.</div>
<p>회사와 무관한 연락이나 투자 제안을 받으셨다면 응답하지 마시고 즉시 차단해 주세요. 관련 사칭 행위는 증거 수집 후 수사기관·법률 자문과 함께 대응 중입니다.</p>
<div class="acts"><button type="button" class="hide" id="hide">오늘 하루 보지 않기</button><button type="button" class="ok" id="ok">확인했습니다</button></div></div></div>'''

# ---- 메인
page('index.html', '{TN}', '''<div class="hero"><div class="slides"><div class="on" style="background-image:url(assets/img/hero-sky1.jpg)"></div><div style="background-image:url(assets/img/hero-sky2.jpg)"></div><div style="background-image:url(assets/img/hero-mountain1.jpg)"></div><div style="background-image:url(assets/img/hero-mountain2.jpg)"></div></div><div class="overlay"></div><button class="arrow prev" type="button" aria-label="이전 배너">&#8249;</button><button class="arrow next" type="button" aria-label="다음 배너">&#8250;</button>
<div class="wrap"><h1>“{C} — 더 높은 푸른 하늘.”</h1><p>새로운 가능성이 피어오르는 곳,<br>높은 뜻을 품고 더 넓은 하늘로 나아가는 투자사</p></div></div>
<section class="biz"><div class="wrap"><h2 class="big-title"><span>OUR</span> BUSINESS</h2>
<p class="lead">고객분들의 뜻이 한곳에 모여 광장이라는 한공간에서<br>혁신적인 발전으로 미래를 지향하겠습니다.</p>
<div class="cards">
<a class="card" style="background-image:linear-gradient(rgba(10,15,30,.35),rgba(10,15,30,.35)),url(assets/img/banner-business.jpg)" href="business.html"><h3>사업분야</h3><span class="plus" aria-hidden="true"></span></a>
<a class="card" style="background-image:linear-gradient(rgba(10,15,30,.35),rgba(10,15,30,.35)),url(assets/img/banner-service.jpg)" href="service.html"><h3>서비스 안내</h3><span class="plus" aria-hidden="true"></span></a>
<a class="card" style="background-image:linear-gradient(rgba(10,15,30,.35),rgba(10,15,30,.35)),url(assets/img/banner-reviews.jpg)" href="reviews.html"><h3>고객후기</h3><span class="plus" aria-hidden="true"></span></a>
</div></div></section>
<section class="soft"><div class="wrap about-split"><div><div class="eyebrow" style="text-align:left">ABOUT US</div>
<p style="margin-top:14px">{C}은 다양한 투자자의 생각과 관점을 하나로 모아,<br>정보의 비대칭을 해소하고 신뢰를 바탕으로 한 투자 인사이트를 전하며<br>투자의 복잡함을 단순하게, 불안함을 확신으로 바꾸는<br>투자자 중심의 열린 광장이 되겠습니다.</p>
<a class="btn" href="about.html">Read More</a></div>
<div class="photo has-img" role="img" aria-label="회사 소개 이미지" style="background-image:url(assets/img/banner-about.jpg)">이미지</div></div></section>
<section class="dual">
<a class="dual-box" style="background-image:linear-gradient(rgba(7,25,60,.55),rgba(7,25,60,.55)),url(assets/img/banner-notice.jpg)" href="notice.html#notice"><h3>공지사항</h3><span class="pill">Read More</span></a>
<a class="dual-box" style="background-image:linear-gradient(rgba(7,25,60,.55),rgba(7,25,60,.55)),url(assets/img/extra-958.jpg)" href="notice.html#press"><h3>보도자료</h3><span class="pill">Read More</span></a>
</section>
''', POPUP if SHOW_POPUP else '')

# ---- 회사소개
page('about.html', '회사소개 - {TN}', sub('ABOUT US', 'banner-about.jpg') + tabs([('greeting','대표 인사말'),('overview','회사개요'),('location','오시는 길')]) + '''
<section><div class="wrap">
<div class="panel" id="greeting"><h2 class="title">대표 인사말</h2><div class="greet">
<div class="photo has-img" role="img" aria-label="인사말 이미지" style="background-image:url(assets/img/greeting.jpg)">이미지</div>
<div><strong>안녕하십니까.<br>{C}(靑雲) 입니다.</strong>
<p>{C}은 푸른 하늘에 펼쳐진 구름처럼,<br>더 넓은 가능성을 바라보고<br>새로운 기회를 통해 더 높은 미래로 나아가는 투자사입니다.</p>
<p>빠르게 변화하는 시장 환경 속에서<br>정보는 넘쳐나지만,<br>정확한 판단과 신뢰할 수 있는 기준은 오히려 더 희소해지고 있습니다.</p>
<p>{C}은 눈앞의 변화에 흔들리기보다<br>고객의 입장에서 먼저 고민하고,<br>복잡한 흐름 속에서도 더 넓은 시야로<br>시장의 본질과 새로운 가능성을 바라봅니다.</p>
<p>우리는 과장된 기대보다<br>지속 가능한 성장을,<br>순간의 속도보다<br>올바른 방향성을 중시합니다.</p>
<p>단기적인 성과에 머무르지 않고<br>시간이 지날수록 더욱 빛나는 가치,<br>말보다 실천으로 증명되는 신뢰를 쌓아가겠습니다.</p>
<p>앞으로도 {C}은<br>투명하고 정직한 소통을 바탕으로<br>고객의 가능성이 더 큰 미래로 이어질 수 있도록<br>함께 나아가는 든든한 파트너가 되겠습니다.</p>
<p>더 넓은 시야로, 더 높은 가치를 향해.</p><p>감사합니다.</p></div></div></div>
<div class="panel" id="overview"><h2 class="title">회사개요</h2>
<p class="ov-title">더 넓은 시야로, 더 높은 가치를 향해. {C}.</p>
<p class="ov-text">{C}은 드넓은 푸른 하늘처럼<br>새로운 가능성과 다양한 투자자의 시선이 모여<br>더 높은 미래를 향한 가치가 펼쳐지는 투자사입니다.</p>
<dl class="dl" style="margin-top:36px"><dt>상호</dt><dd>{LEGAL}</dd><dt>주소</dt><dd>{ADDR}</dd></dl></div>
<div class="panel" id="location"><h2 class="title">오시는 길</h2><img class="mapimg" src="assets/img/map.jpg" alt="{C} 오시는 길 약도">
<dl class="dl" style="margin-top:24px"><dt>주소</dt><dd>{ADDR}</dd><dt>교통편</dt><dd>2호선 문래역 4번 출구 도보 약 5분<br>2·5호선 영등포구청역 도보 약 7분</dd></dl></div>
</div></section>''')

# ---- 사업분야
items = ["시장 리서치 및 분석 콘텐츠 제공","국내외 금융시장 관련 정보 및 트렌드 콘텐츠 제공","다양한 관점의 시황 리포트 및 분석 자료 발행","일반 투자 정보 콘텐츠 제공","투자 참고용 정보 및 뉴스 큐레이션","금융시장에 대한 시각을 나누는 콘텐츠 제작","온라인 커뮤니티 운영","다양한 투자자들의 의견이 공유되는 열린 커뮤니티 제공","자유로운 토론과 정보 교류의 장 마련","데이터 기반 정보 콘텐츠 제공","시장 지표, 차트 등 정량적 데이터 콘텐츠 제공","사용자 이해를 돕는 시각화 자료 제작","금융·투자 인식 제고 프로그램","초보자를 위한 기초 정보 콘텐츠 운영","합리적 투자 판단에 도움이 되는 정보 제공"]
icons = ["person-chalkboard","clipboard-list","file-lines","user-group","sliders","bars-progress","message","comments","users","envelope-open-text","chart-line","desktop","lightbulb","pen-to-square","share-nodes"]
cells = ''.join('<div><i class="fa-solid fa-%s" aria-hidden="true"></i><small>BUSINESS %02d</small><p>%s</p></div>' % (icons[i], i+1, t) for i, t in enumerate(items))
page('business.html', '사업분야 - {TN}', sub('BUSINESS', 'banner-business.jpg') + '<section><div class="wrap"><h2 class="title">사업분야</h2><div class="grid5">' + cells + '</div></div></section>\n')

# ---- 서비스 안내 (등급 이미지에 글자가 포함되어 있음)
page('service.html', '서비스 안내 - {TN}', sub('SERVICE', 'banner-service.jpg') + '''<section><div class="wrap"><h2 class="title">서비스 안내</h2>
<h3 class="sec-label">상품소개</h3><div class="tiers">
<div class="tc"><img src="assets/img/tier-1.png" alt="실버 등급"></div><div class="tc"><img src="assets/img/tier-2.png" alt="골드 등급"></div><div class="tc"><img src="assets/img/tier-3.png" alt="플래티넘 등급"></div></div></div></section>
''')

# ---- 전문가
ex = [("이대표","경영 총괄 · 투자전략","{C}의 방향을 설계하는 리더. 원칙 있는 투자 문화와 고객 신뢰를 최우선으로 합니다."),
      ("최교수","리서치 · 투자교육","이론과 실전을 잇는 리서치 전문가. 데이터에 근거한 분석으로 시장을 해석합니다."),
      ("공박사","가치투자 · 리스크 관리","숫자로 말하는 가치투자 베테랑. 저평가를 집요하게 찾고, 위험은 먼저 차단합니다."),
      ("박프로","종목 분석 · 시장 트렌드","젊은 감각으로 시장을 빠르게 읽는 신예 전문가. 정교한 분석으로 탄탄한 신뢰를 쌓아갑니다.")]
cards = ''.join('<div class="expert"><div class="avatar has-img" role="img" aria-label="%s" style="background-image:url(assets/img/expert-%d.png)">사진</div><div><b>%s</b><em>%s</em><p>%s</p></div></div>' % (n, i+1, n, r, d) for i, (n, r, d) in enumerate(ex))
page('experts.html', '{C} 전문가', sub('SERVICE', 'banner-experts.jpg') + '<section><div class="wrap"><div class="eyebrow">EXPERTS</div><h2 class="title">{C} 전문가</h2><div class="experts">' + cards + '</div></div></section>\n')

# ---- 고객후기 / 커뮤니티
page('reviews.html', '고객후기 - {TN}', sub('REVIEWS', 'banner-reviews.jpg') + '<section><div class="wrap"><h2 class="title">고객후기</h2>' + board(0) + '<a class="write" href="#">글쓰기</a></div></section>\n')
page('notice.html', '커뮤니티 - {TN}', sub('COMMUNITY', 'banner-notice.jpg') + tabs([('notice','공지사항'),('press','보도자료')]) + '''<section><div class="wrap">
<div class="panel" id="notice"><h2 class="title">공지사항</h2>''' + board(0) + '''</div>
<div class="panel" id="press"><h2 class="title">보도자료</h2>''' + board(0) + '''</div></div></section>
''')
print("완료:", COMPANY)

# ---- sitemap.xml / robots.txt
import datetime
today = datetime.date.today().isoformat()
urls = ''.join('<url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (SITE_URL + ('' if n == 'index.html' else n), today) for n in PAGES)
open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + '</urlset>\n')
open(os.path.join(OUT, 'robots.txt'), 'w', encoding='utf-8').write('User-agent: *\nAllow: /\n\nSitemap: ' + SITE_URL + 'sitemap.xml\n')
