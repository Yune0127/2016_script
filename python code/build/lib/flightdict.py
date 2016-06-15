# -*- coding: utf-8 -*-


#항공사
airlinedic = {"3SX" : "에어로로직" , "CSC" : "사천항공" , "UPS":"유피에스항공","GTI":"아틀라스항공",
"JJA":"제주항공","BCC":"비즈니스에어","CYZ":"중국우정항공","SOO":"미국남부화물항공","AAL":"아메리칸항공",
"ACA":"에어캐나다","MDA":"만다린항공","AFR":"에어 프랑스","AIC":"에어인디아","FIN":"핀에어","UIA":"유니항공",
"BAW":"영국항공","EVA":"에바항공","CCA":"중국국제항공","CAL":"중화항공","CKK":"중국화물항공","CLX":"카고룩스항공",
"CPA":"캐세이패시픽항공","CSN":"중국남방항공","DYA":"다이나믹 에어","XAX":"에어아시아엑스","DAL":"델타항공",
"UAE":"에미레이트항공","ETH":"에티오피아항공","ETD":"에티하드 항공","EIA":"에버그린인터내셔날","CSH":"상하이항공",
"FDX":"페덱스","GIA":"가루다인도네시아항공","GCR":"텐진 에어라인","PCA":"피시 에어라인","HAL":"하와이안항공",
"CRK":"홍콩항공","UZB":"우즈베키스탄항공","SHU":"오로라항공","JAL":"일본항공","VNL":"바닐라 에어","KZR":"에어아스타나",
"KAL":"대한항공","AIH":"에어인천","KLM":"케이엘엠네덜란드항공","EAA":"에어 비쉬켁","NCA":"일본화물항공","AHK":"에어홍콩",
"DLH":"루프트한자항공","JNA":"진에어","MEG":"메가몰디브항공","CXA":"중국하문항공","MAS":"말레이시아항공","APJ":"피치항공",
"CES":"중국동방항공","ANA":"전일본공수","AJX":"에어재팬","AMU":"에어 마카오","CSS":"순풍항공","CSA":"체코항공",
"MGL":"몽골항공","AAR":"아시아나항공","PAC":"폴라에어카고","PAL":"필리핀항공","QTR":"카타르항공","LAO":"라오항공",
"SYL":"야쿠티아 항공","ABW":"에어브리지 카고 에어라인","CDG":"산동항공","SIA":"싱가포르항공","AFL":"에어로플로트항공",
"THA":"타이항공","THY":"터키항공","TWB":"티웨이항공","SCO":"스쿳 항공","UAL":"유나이티드항공","HKE":"홍콩엑스프레스항공",
"VJC":"비엣제트항공","HVN":"베트남항공","WOA":"월드항공","TAX":"타이에어아시아엑스","YZR":"양쯔강익스프레스항공",
"EZD":"에어아시아 제스트항공","SWM":"스카이윙스 아시아 항공","ESR":"이스타항공","CSZ":"심천항공"}


airlineCodedic = {"3S":"3SX","3U":"CSC","5J":"CEB","5X":"UPS","5Y":"GTI","7C":"JJA","8B":"BCC","8Y":"CYZ",
"9S":"SOO","AA":"AAL","AC":"ACA","AE":"MDA","AF":"AFR","AI":"AIC","AY":"FIN","B7":"UIA","BA":"BAW","BR":"EVA",
"CA":"CCA","CI":"CAL","CK":"CKK","CV":"CLX","CX":"CPA","CZ":"CSN","D2":"DYA","D7":"XAX","DL":"DAL","EK":"UAE",
"ET":"ETH","EY":"ETD","EZ":"EIA","FM":"CSH","FX":"FDX","GA":"GIA","GS":"GCR","GT":"PCA","HA":"HAL","HX":"CRK",
"HY":"UZB","HZ":"SHU","JL":"JAL","JW":"VNL","KC":"KZR","KE":"KAL","KJ":"AIH","KL":"KLM","KR":"EAA","KZ":"NCA",
"LD":"AHK","LH":"DLH","LJ":"JNA","LV":"MEG","MF":"CXA","MH":"MAS","MM":"APJ","MU":"CES","NH":"ANA","NQ":"AJX",
"NX":"AMU","O3":"CSS","OK":"CSA","OM":"MGL","OZ":"AAR","PO":"PAC","PR":"PAL","QR":"QTR","QV":"LAO","R3":"SYL",
"RU":"ABW","SC":"CDG","SQ":"SIA","SU":"AFL","TG":"THA","TK":"THY","TW":"TWB","TZ":"SCO","UA":"UAL","UO":"HKE",
"VJ":"VJC","VN":"HVN","WO":"WOA","XJ":"TAX","Y8":"YZR","Z2":"EZD","ZA":"SWM","ZE":"ESR","ZH":"CSZ"}




# 공항
airportdic = {"AKJ":"아사히카와","AKL":"오클랜드","ALA":"알마티","AMS":"암스테르담","ANC":"앵커리지",
"AOJ":"아오모리","ASB":"아쉬가바트","ATL":"애틀랜타","AUH":"아부다비","BAH":"바레인","BEY":"베이루트",
"BKI":"코타키나발루","BKK":"방콕","BNE":"브리즈번","BOM":"뭄바이","BRU":"브뤼셀","BSL":"바젤","BUE":"부에노스 아이레스",
"BWN":"반다르스리브가완","CAI":"카이로","CAN":"광저우","CCS":"마이케티아","CDG":"파리","CEB	":"세부","CGK":"자카르타",
"CGN":"쾰른","CGO":"정저우","CGQ":"창춘","CJU	":"제주","CKG":"충칭","CMB":"콜롬보","CNX":"치앙마이",
"CPH":"코펜하겐","CRK":"클라크필드","CSX":"장사","CTS":"삿포로","CTU	":"청두","DAC":"다카","DEL":"델리",
"DFW":"댈러스","DLC":"다롄","DOH":"도하","DPS":"덴파사르","DTW":"디트로이트","DXB":"두바이","FCO":"로마",
"FKS":"후쿠시마","FRA":"프랑크푸르트","FRU":"	비슈케크","FSZ":"시즈오카","FUK":"후쿠오카","GMP":"서울/ 김포",
"GOT":"고테버그","GRU":"상파울루","GUM":"괌","GYD":"바쿠","HAN":"하노이","HEL":"헬싱키","HGH":"항저우",
"HIJ":"히로시마","HKD":"하코다테","HKG":"홍콩","HKT":"푸케트","HND":"도쿄/ 하네다","HNL":"호놀룰루",
"HOU":"휴스턴","HRB":"하얼빈","IAD":"워싱턴","IKT":"이르쿠츠크","ILN	":"에어본 에어파크","IND":"인디애나폴리스",
"IST":"이스탄불","JFK":"뉴욕","KHH":"가오슝","KHN":"난창","KHV":"하바로프스크","KIJ":"니가타"
"KIX":"오사카/ 간사이","KKJ":"기타큐슈","KLO":"칼리보","KMG	":"쿤밍","KMI":"미야자키","KMJ":"구마모토",
"KMQ":"고마쓰","KOJ":"가고시마","KTM":"카트만두","KUL":"쿠알라룸푸르","KWI":"쿠웨이트","KWL":"계림",
"LAS":"라스베이거스","LAX":"로스앤젤레스","LED":"상트페테르부르크","LHR":"런던/히드로","LJG":"리장",
"LUX":"룩셈부르크","MAA":"첸나이","MAD":"마드리드","MDG":"무단장","MEL":"멜버른","MEM":"멤피스",
"MFM	":"마카오","MIA":"마이애미","MNL":"마닐라","MUC":"뮌헨","MXP":"밀라노","MYJ":"마쓰야마","NAN":"난디",
"NGB":"닝보","NGO":"나고야","NGS":"나가사키","NKG":"난징","NNG":"난닝","NOU":"누메아","NRT":"도쿄/ 나리타",
"OIT":"오이타","OKA":"오키나와","OKJ":"오카야마","ORD":"시카고","OSA	":"오사카","OSL":"오슬로","OVB":"노보시비르스크",
"PEK":"베이징","PEN":"페낭","PHL":"필라델피아","PNH":"프놈펜","PRG":"프라하","PUS":"부산","PVG":"상하이/ 푸동",
"REP":"시엠립","RGN":"양곤","ROR":"코로르","SDJ":"센다이","SEA":"시애틀","SFO":"샌프란시스코","SFS":"수비크",
"SGN":"호찌민","SHE":"선양","SIA":"서안","SIN":"싱가포르","SJW":"스자좡","SOF":"소피아","SPN":"사이판",
"STI":"산티아고","STO":"스톡홀름","SVO":"모스크바","SYD":"시드니","SYX":"싼야","SZX":"선전","TAE":"대구",
"TAK":"다카마쓰","TAO":"칭다오","TAS":"타슈켄트","THR":"테헤란","TLV":"텔아비브","TNA":"지난","TOY":"도야마"
"TPE":"타이페이","TSE":"아스타나","TSN":"톈진","ULN":"울란바토르","URC":"우루무치","UUS":"사할린",
"VIE":"비엔나","VVO":"블라디보스토크","WAW":"바르샤바","WEH":"웨이하이","XMN":"샤먼","YGJ":"요나고",
"YKS":"야쿠츠크","YNJ":"옌지","YNT":"옌타이","YNZ":"옌청","YVR":"밴쿠버","YYC":"캘거리","YYZ":"토론토","ZRH":"취리히"}


