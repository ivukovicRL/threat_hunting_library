# -*- coding: utf-8 -*-
COMMON_EMAIL_SUBJECTS = frozenset([
    ' civil engineer looking for job in the middle east',
    '“本当に儲かる投資情報”とは何かをお教えします。',
    '”採用通知”',
    '”激安問屋”お得感ナンバー1商品',
    '(σ´∀`)σゲットォ♪',
    '(みずほ銀行)振込予約を承りました。',
    '（抽選発表!!）《♪新春初夢プレゼント大抽選会♪》',
    '(通知)080-7817-55069',
    '（重要）【フリーライフ閉鎖終了】のお知らせ',
    '[ 緊急速報 ]',
    '[ange管理人]出逢いsupervisor中西里奈様より新着メール',
    '[ext] c&n ethanol rfs2 ptd',
    '[ext] daily rin statement',
    '[ext] reg invoices (tx)',
    '[https://www.ostomais.com] wp super cache gc report',
    '[suisui] please moderate: "ls1780"',
    '[suisui] product low in stock',
    '[九条グループ代表・九条麗子]',
    '[副業]お給料を二つに！、日給制１５０００～',
    '[重要]在庫処分の大幅値下げ！',
    '[金融庁支援上層本部：最高責任者]松尾　大輔さんからメールです♪',
    '《朗報！》 ～会員の皆様にサイト閉鎖に伴う大事なお知らせ～ 《朗報！》',
    '《運営事務局》様より新着メール',
    '「1億円」の受け取り方法記載メール',
    '「1億円」の支援金を貴方に差し上げます。受け渡し方法は',
    '「ありがとう」',
    '「さようなら」と',
    '「ルパン三世より」',
    '「余命宣告」',
    '「当たる」のではなく、「当てる」のです！',
    '「攻略法は存在します」',
    '「期間限定」新装開店バーゲンセール',
    '「競馬」ってどんなイメージ？',
    '「返済不要の支援金」の「1億円」の今、貴方の',
    '『Ｇ8主要国支援首脳本部：事務総長』東十条　光一さんからメールです♪',
    '『アナタにとって出会いが不要なら、このメールは開封しないで下さい。』',
    '『中出しokだよぅ～♪』',
    '『個人支援活動家』帝塚恵子様より新着メッセージが届いています　◆vip room◆',
    '『条件』は1つだけです。',
    '【※必見※】簡単な副業♪',
    '【※銀行からの大切なお知らせです※】',
    '【◇-ご案内-◇】当サイトを無料でご利用可能となりました。',
    '【☆柳由美子様より[＼／]を受信しております☆】',
    '【1,000円一度で7500万円のお振込】(追加費用はございません)',
    '【20万ポイント無償追加】＆【完全無料指名】お相手の会員様はコチラになります▼',
    '【20名限定】ノーリスクで稼げるモニター募集',
    '【２等】１０００万円 ご当選のお知らせ',
    '【ange】[ange管理人]出逢いsupervisor中西里奈様より新着メール',
    '【ange】☆ﾛｸﾞｲﾝﾎﾞｰﾅｽ獲得☆▽get▽',
    '【ange】セフレ希望☆五十鈴ちゃん様より新着メール',
    '【ange】周防美麗：年収3000万様より新着メール',
    '【free】無☆料ポイントのお知らせ【free】◇happy事務局◇',
    '【vip】様へお知らせ',
    '【wiwiline】当番組会員様からのご連絡',
    '【world net lottery】当せんのお知らせ☆',
    '【インフォトップ：受注】期間限定で無料で公開しています。',
    '【うさぴっぴ】当番組会員様からのご連絡',
    '【オトク機能のご紹介！】',
    '【オトク機能のご紹介！】あなたの履歴がいつでもご確認頂けます。',
    '【スカウト】',
    '【ナイチンゲール:プロフ更新確認】',
    '【モニター】無料登録しただけで毎月30万円もらえるとしたらやりますか？',
    '【入金予約】を受け付けました。至急内容のご確認をお願いします。',
    '【入金通知】10,000,000円の入金がありました。',
    '【全国支援協会総本部：最高顧問】生田　雄介さんからメールです♪',
    '【全国総合支援ネットワーク管理センター】さんからメールです♪',
    '【公表】しないで下さい。',
    '【最終通知】残し時間僅か',
    '【最高名誉会員】各種手続費用不要',
    '【初心者限定】無料モニター募集',
    '【制限解除】最高名誉会員制限解除設定',
    '【動画あり】家に居ながら月100万円以上稼ぐ方法',
    '【報酬率100％】就任地域報酬／月々25日',
    '【契約完了】過去に契約されていた補償の満期となりましたので確認をお願いいたします。',
    '【好条件】在宅副業',
    '【完全無料】おめでとうございます＼(^o^)／ゲスト様宛に完全無料権譲渡依頼が届きました★',
    '【完全無料中】ポイント消費は御座いません',
    '【完全無料指名】＆【20万ポイント無償追加】お相手の会員様確認はコチラから▼',
    '【審査】',
    '【就任意思確認】就任放棄と承って宜しいでしょうか?',
    '【就任決定】瀬戸様より無条件譲渡申請',
    '【就任特典】一切、利用料金は発生致しません',
    '【就任特典】完全無料でご利用頂けます',
    '【就任特典】称号・権限・特典の剥奪は御座いません',
    '【延長通知】',
    '【必読】安全なサイトをこちらで検出しました。',
    '【手数料無料】とご連絡ください！',
    '【振り込み完了】【無料手続き】',
    '【支援案内】こちらの内容をご確認ください。',
    '【料金不要】最高名誉会員永久無料設定',
    '【朗報】新しい金融　※ご融資審査ナビ',
    '【未支援者専用：国家安全保障支援経団連】河西さんからメールです♪',
    '【極秘】稼げる副業!!',
    '【炎のチャ○ンジャー】これができたら120万円',
    '【無料】『個人支援活動家』帝塚恵子様より新着メッセージが届いています　◆vip room◆',
    '【無料】川村沙織様より新着メッセージが届いています　◆vip room◆',
    '【無料】誰でも年に数回、100万円のチャンス！',
    '【無料会員昇格中！】現在無料でご利用可能です！',
    '【無料宝くじ】',
    '【特別なお知らせ】',
    '【特別支給】現金１００万円を差し上げます。',
    '【現金：250万円】最高名誉会員就任報酬／月々25日',
    '【現金：3000万円】最高名誉会員就任記念／即日一括',
    '【発送】ご注文の商品について',
    '【登録完了メール】直アドセレブリティ',
    '【白田悠仁様】のご申請により完全無料でのご利用が可能となっております。',
    '【着信あり】',
    '【祝】相性診断結果が98％を超えました♪おめでとうございます♪',
    '【絶対に“的中”する情報】',
    '【至急】未払い料金について',
    '【至急ご確認ください】支払いの件',
    '【芸能人の】ウラ副業',
    '【芸能人の間で話題沸騰中!!】半永久的に毎月30万円受け取り続ける方法',
    '【苦情】ご利用中の支援に関して大切なお知らせ',
    '【裏情報を無料でgetする方法】',
    '【補償満期】満期になった補償のお支払のご連絡です。',
    '【診断結果：相性98％】なんと!!驚きの結果が出ました!!',
    '【譲渡証明書在中】病院長の石川です。',
    '【貴方の個人情報】',
    '【足跡】女性会員様がゲスト様のプロフィールを閲覧しています。',
    '【軍資金制度有】お近くのホールで活動してください♪',
    '【送信無米斗中】　只今時間限定で送信ポイントが不要となっております',
    '【速報】さらに値下げを継続中',
    '【重要】ロト６の検証モニター募集中　※高額収入です',
    '【重要】入金予約がありました。至急内容をご確認ください。',
    '【重要】只今受けています支援に関して大切なご連絡',
    '【重要】契約が確認されている証書の確認をお願いいたします。',
    '【重要】違法サイトの排除にご協力ください。',
    '【重要事項】決して他の方には公表しないで下さい',
    '【重要連絡】こちらの内容は必ずご確認ください。',
    '【重要連絡】葉山詩織様より、文字化け解除要請がありましたのでご対応させて頂きます。',
    '【金持ち確定】',
    '【限定特典】人数限定でプレミアムメンバーへご招待中!',
    '** r�ponse automatique **',
    '※【日本国内支援統括セキュリティ審査会】※さんからメールです♪',
    '※ご入金がありましたので至急ご確認下さい※',
    '※どう見ても遊びです',
    '※やりすぎ注意※',
    '※写真あり【必読】重要なお知らせになりますので必ずご確認を！',
    '※口座ロック解除して下さい。',
    '※口座送信解放中※1000万の支援依頼が御座います　◆vip room◆',
    '※在宅',
    '※完全無料※にて利用可能■20万■の入金代行決済：１件',
    '※必ずご確認ください※昨年度大還元日!!寄付金・不明金【14,100,000円】即受取!!■',
    '※急募時給3万円～※',
    '※本状を受信された方は情報流出の可能性が御座います',
    '※相性98%※超えの診断結果が出来ました♪',
    '※要確認※高倉様から特別依頼が届いております♪',
    '※重要※高倉様より【20万ポイント無償追加】＆【完全無料指名】のご依頼が届いております。',
    '↓タテ',
    '+α+α+α+α+α+α+α+α+α+α+α',
    '＜10分で入金＞複雑な手続きは無し。4億8000万は簡単に受け取れますのでご安心下さい。',
    '＜出会い保障対象者＞九条ゆき子様とのやりとりが無料となっております。',
    '～クイック入金案内～',
    '～申込完了のお知らせ～',
    '∞参加無料∞マイスターお年玉企画♪【マイスターお年玉企画担当】',
    '≪ s u p p o r t 窓 口 ≫ 振 込 通 知',
    '≪ウイルス診断結果≫こちらのサイトは安全です。詳細は↓',
    '≪最終受付本日15時≫新・プロジェクト実行！',
    '≪危険≫違法サイトの利用は停止してください。詳細は内容をご確認ください。',
    '──【サポートセンター問い合わせ履歴】の見落としは大丈夫ですか？──',
    '━ヽ(ﾟ∀ﾟ)ﾉ ━新感覚！クリックだけでできる頭脳活性化パズルゲーム ！━ヽ(ﾟ∀ﾟ)ﾉ ━',
    '■■■「2017年新年運試し」開催予告■■■',
    '■1等当選のご案内■',
    '■50万円譲渡入金を確認して下さい■現金で入金されております！',
    '■ロト６当選の最終兵器！高額当選連発中！',
    '■入金完了通知■ 20万円のご入金があります',
    '■受信ボックスの容量が規定値を超えました■',
    '■完全無料のご案内■',
    '■未読メール■(削除寸前のメールがございます)',
    '■無料案内■高倉様からの特典は全て無料でお受取り可能となっております♪',
    '■現在無料中!!■ファンタジスタ昇格!!■受付期間は本日24時迄となっております!!■',
    '□■現金譲渡『50万円』ゲスト様宛です。■□',
    '▼≪8年間完全無料≫＋≪900の受け取り≫▼ロイヤルエンペラー詳細▼',
    '▼≪8年間完全無料≫▼ロイヤルエンペラー詳細▼',
    '▼100%受け取り保証付き▼お手続き後、即時お渡し2200▼',
    '▼1億5',
    '▼1億5千万▼',
    '▼1億5千万受取詳細▼',
    '▼新着メッセージ一覧▼',
    '▼配・信・停・止ご希望の方はご確認ください',
    '▼重要連絡 - ご利用サイトの事業統合・吸収合併が完了致しました。',
    '▼重要連絡 - 動画・音楽・ゲームなども永久無料でご利用頂けます。',
    '▽オススメはこちら▽',
    '◆【new!!=?shift_jis?b?gxqdgyolg3cc1orxgrmc54lqgumxbifygsicqjbigqknh4ltgrmcyyrwgrwc3ik1gssbnw==?=',
    '◆≪1200≫当選!!◆ロイヤル会員様、1等おめでとう御座います!!',
    '◆☆★エッチな素人画像館★☆',
    '◆jpネットマイルより大切なお知らせ◆',
    '◆libra◆［libraﾗﾝｷﾝｸﾞ］第2位!!100万円♪ご当選おめでとうございます♪',
    '◆libra◆1000円で正規会員登録◆連絡先交換も自由・費用もﾎﾟｲﾝﾄも最小限!!',
    '◆libra◆ポイント購入案内♪決済方法をご確認下さい♪',
    '◆libra◆メインメニューへご案内致します♪☆',
    '◆libra◆絶対お得!!1000円で正会員登録♪全ｱｸｼｮﾝ無料!!メインメニューへご案内致します♪',
    '◆無料案内中◆【無料ペア指名中】【開業医】榊様とのやり取りは完全無料◎',
    '◆要確認◆高倉様より特別依頼が御座いました！内容確認はコチラ↓↓',
    '◆重要案内◆【30万pt追加】無料でpt受取可能◎詳細確認はコチラ↓',
    '◇桃色白書◇《08088346534》電話番号のお預かりが2件ございます♪',
    '◇桃色白書◇ゲスト様は現在当サイトのメール送信を無料でご利用頂けます♪',
    '★-ＭＩＸ-★相性…97％超!!運命のお相手様をご紹介させて頂きます♪',
    '★【388500pt追加】緊急ルーレット発動★',
    '★【エステ経営：さをり】様より30万円分のＰＴのお預かりが御座います★',
    '★【緊急】毎週末が給料日！毎週数十万円が勝手に口座に、喜びの声続々★',
    '★★★フリーライフの安全への取り組み★★★',
    '★★写メ付メール受信★★',
    '★☆★☆★　wowwow　★☆★☆★',
    '★ご当選者様発表★（お客様大還元祭）',
    '★気になるお相手とアドレス交換しませんか？★',
    '★特別案内★高倉様より【20万ポイント無償追加】＆【完全無料指名】の依頼が御座いました！',
    '★相性占いspecial★お客様に相性の良い会員様をご紹介♪',
    '★高倉様より「完全無料」申請ならびに【20万ポイント無償譲渡】依頼がございます★',
    '☆期間限定：毎週５０～１５０万円副収入を稼ぐ方法教えます',
    '☆無料プラン⇒値下げになりました☆この機会に是非♪今が大ﾁｬﾝｽ☆',
    '〓エロナース軍団が貴方様を祝福してます〓',
    '〓半裸美女が貴方様の事をうらやましがってます【重要】',
    '〓夏のカゲキな思い出(閲・覧・無・料)',
    '100％当たる驚愕のロト予想システム！100％当選するトップシークレットの内容とは…',
    '1000円のみで解除出来ますので、お気軽にご利用下さい。',
    '100万円もらえるモニター',
    '15日で100円を100万円にします',
    '18歳以上の方だけ',
    '1件振り込まれる予定です',
    '1度だけ言います。',
    '1日200円で年2千万超え！！',
    '1等では目立ちすぎるのです',
    '1等当選！驚異の黄金法則',
    '2018年2月6日対策対応済',
    '２０歳以上なら誰でも出来る副業【初心者ok】',
    '2等～5等を意図的にガンガン当選させるありえないロト攻略法',
    '30万円の残高がございます。▼ご利用はこちらから▼',
    '３０歳越えたら、おばさんです',
    '32億振込完了',
    '3か月で3億円を手にした個人投資家もいます！！',
    '3歳上の兄の子供を妊娠してしまいました。',
    '３等（５０万円前後）の当選番号をプレゼントします！',
    '3等以上!?',
    '400万もらった。　悪魔に魂を売った。',
    '40歳以上で心も身体も癒やされたい方は[癒やし家]へお越し下さい。',
    '4億円の作り方',
    '4億円入手方法を10名様限定無料公開',
    '4年2組★里奈先生様より新着メッセージが届いています　◆vip room◆',
    '5 рассылок за 10 000 + спецхостинг или 6-я рассылка в подарок',
    '5000万の件です。',
    '50万なら当たるから！',
    '50万円の残高がございます。▼ご利用はこちらから▼',
    '55%offキャンペーン中のb-casカードで、すべてのチャンネル見放題！',
    '6信管家@百度”',
    '6期货@百度”',
    '6期货300@百度”',
    '8 рассылок за 10 000',
    '8 рассылок за 10 000 + хостинг на месяц в ПОДАРОК',
    '8000万円＆特典すべて',
    '8000万円＋豪華サービス',
    '8期货@百度”',
    'a final notice about your 2019 tds 88000 rs payment successful',
    'accepting your application',
    'account security notice - immediate action required',
    'aggressive investors alert',
    'alarm: critical - b2 gas limit alm ev',
    'alarm: critical - b2 water lvl alm ev',
    'angelina jolie naked',
    'apple amno 945 booking message from foxconn',
    'apple emea 945 booking message from foxconn',
    'apple emea 945 booking message from hhcd (applecare)',
    'approval process',
    'aromor invoice',
    'attached image',
    'atualização cadastral',
    'authentication milter test',
    'avaliação de imóveis por inferência estatística - curitiba - pr - dias: 16 e 17 fev 2019 - rs',
    'av男優公認',
    'bad credit ok',
    'be sure to read this message! your personal data is threatened!',
    'beautiful quartz, water-resistant replica watches',
    'beautiful russian women waiting to meet you!',
    'belebt geist und korper',
    'best medical portal !!!',
    'best pharma online discount sale!!',
    'best quality drugs . shipping 1-4 day usa',
    'best quality drugs .active pack = 174$',
    'best quality xanax from fully licensed pharmacies without rx needed',
    'best seller watches : rolex gold = 119$ , rolex sport = 119$!!',
    'bewerbung',
    'black friday',
    'black week',
    'brand name luxury timepieces',
    'brand name quality rolex',
    'breaking news',
    'breitling',
    'breitling watches',
    'brokerage poa for business',
    'bruce@bruce-guenter.dyndns.orgにメールが届いています。',
    'bs・cs全チャンネルがタダで見放題のカードが今ならナント半額以下の45%で買えちゃう！',
    'business loan- $10k-$100k',
    'business proposal',
    'bvlgari watches',
    'ca・モデル・イベントコンパニオン',
    'career opportunity inside',
    'cartier',
    'cartier watches',
    'casino welcome bonus',
    'certificate of completion',
    'chanel watches',
    'cheap oem soft shipping //orldwide',
    'check out hot deals',
    'chopard watches',
    'christmas replica watches',
    'cnn alerts: my custom alert',
    'community から新着メールのお知らせです。',
    'cone mail client',
    'confirm it\'s you to access your ebay account - march 12, 2020',
    'confirmación de suscripción al boletín de noticias',
    'confirmation link',
    'confirmation of approved mitigation plan',
    'congratulations',
    'congratulations!!!',
    'conheça a mais nova loja',
    'controlled application request',
    'corel draw',
    'covid-19 pulse survey - your voice matters',
    'created by oracle bi publisher',
    'cruise ship  - yatch  jobseeker for  f&b server , lifeguard positions',
    'curso excel intermediário com acyr jansen | só restam 6 vagas | Única edição do semestre | fortaleza-ce',
    'customer alert notification',
    'customer order approval',
    'customer profile update',
    'customer shipment status',
    'customer shipping confirmation',
    'daily activities list - cly',
    'dear',
    'debt consolidation',
    'delivery status notification',
    'delivery status notification (delay)',
    'delivery status notification (failure)',
    'demand ken lay donate proceeds from enron stock sales',
    'dhl on demand delivery',
    'diamond replicas',
    'diamond replicas, affordable prices rolex',
    'digital photo editing services - photo cutout',
    'discount!',
    'divulgue sem depender de ninguém',
    'do you like to find a girlfriend like me ?',
    'download all popular softwares just now',
    'draw no reply',
    'e-way bill system',
    'ed正規医薬品・ジェネリック医薬品個人輸入代行がおすすめ！',
    'electronic permit',
    'email handling opinion needed',
    'employment',
    'employment opportunity',
    'employment you\'ve been searching!',
    'enlarge',
    'enron mentions',
    'eqtd monday, august 27, 2006',
    'erase your credit card debt',
    'exclusive replica rolex',
    'exclusive watches',
    'exclusive watches rolex',
    'exclusive watches, affordable prices rolex',
    'exclusive watches, brand name quality rolex',
    'exclusive watches, lowest prices possible rolex',
    'exquisite replica',
    'facedook新規登録',
    'failure notice',
    'fashionable replica watches',
    'fda approved on-line pharmacies',
    'fidelity advisor market update conference call',
    'for bruce',
    'franck muller watches',
    'from puremessage quarantine',
    'from　白田 悠仁',
    'front desk agent , sales agent , concierge  looking for a job in the middle east',
    'get all the medications you want online!',
    'get nominated for mba',
    'get your favorite rxmed here!',
    'get your xanax for as low as $2.15 per pill and even cheaper right now!',
    'girls if you love your boy you need to try it;)',
    'gmail',
    'good day',
    'good day!',
    'great finds',
    'green - sc batch monitoring update',
    'green - warehouse replenishment batch monitoring process',
    'greetings',
    'guaranteed erection fast',
    'haben sie wieder spass am leben!',
    'hallo',
    'handbags',
    'have a stiffy in a jiffy !!!',
    'hello',
    'hello !',
    'hello!',
    'help form: submission received',
    'help stop premature ejaculation!',
    'hermes',
    'hermes watches',
    'hi there',
    'high quality rolex replica watches',
    'high quality watches',
    'highly secure 256bit order processing',
    'hola',
    'home loan',
    'i am thinking about f%cking you',
    'i can do for you is - what can not no girl!',
    'i love ﾏﾈｰ！！',
    'i want to be in your bed',
    'i want you now, tell me reciprocate and get me!',
    'i-spaces（アイスペース）',
    'if you are disappointed in its second half, bold, come in!',
    'immediat software downloads',
    'important notice',
    'important notice: google',
    'important notice: google apps browser support',
    'indusind safeguard verification update',
    'inquiry',
    'instrumentos para sst - manutencao e calibracao',
    'interesting offer',
    'interesting work',
    'inventory fg\\wip report-silicom�',
    'invoice',
    'it\'s too late to consider changes to the south fork clearwater river special supplement for suction dredge mining',
    'it\'s very-beautiful!',
    'j\'ai raté le message fuckbuddy',
    'job ad - see details! sent through  search engine',
    'job offer match, respond to apply',
    'job opportunity  - hurry to apply!',
    'join my network on linkedin',
    'last longer in bed',
    'legal software sales',
    'linkedin alert',
    'linkedin new messages',
    'lists-djb-ezmlm@bruce-guenter.dyndns.orgにメールが届いています。',
    'loan for a low month payment',
    'loan request approved',
    'loose your fat in 9 days',
    'ＬＯＴＯ６＆７で多数の当選者！億万長者多数輩出！！',
    'lowest prices possible rolex',
    'luxurious costume replica watches at ...',
    'luxury',
    'luxury pens',
    'luxury replicas : pearfect luxury watches for blowout sale prices!',
    'luxury replicas : perfect luxury watches for blowout sale prices!',
    'luxury replicas : watches, jewelry & accessories, bags & wallets !',
    'mail delivery failed: returning message to sender',
    'male enhancement',
    'male enhancement reviews',
    'man lebt nur einmal - probiers aus !',
    'many thanks!',
    'max-gentleman  enlargement*pills',
    'max-gentleman*enlargement*pills',
    'maxgentleman enlargement pills',
    'merger update - link your gesa email with inspirus',
    'message copied from system quarantine',
    'message from demisto security operations server',
    'message notification',
    'message report',
    'message subject',
    'metatrader4',
    'minib-casカードも大量入荷',
    'mittel gegen impotenz',
    'monthly transaction statement of your nps account for the period 01-apr-2019 to 30-apr-2019',
    'moody\'s - ironport spam quarantine notification',
    'mria - online',
    'my dear',
    'need pain killers..get them here!',
    'netapp environment report - london',
    'netapp environment report - sydney',
    'new incoming fax messages has arrived',
    'new job vacancy - see details',
    'new message',
    'new offer',
    'new project',
    'new vacancies in our company',
    'news on myspace',
    'next big market winner',
    'no description',
    'notificação de conta',
    'notification',
    'notification bri',
    'nouse',
    'nse - registration for email facility',
    'nyaan',
    'officine panerai watches',
    'omega watches',
    'one year written replica watches warranty',
    'order',
    'order confirmation',
    'outlook',
    'payment notification',
    'pcメールをご利用中のお客様へ',
    'perfect logo & identity is a key to your success',
    'perfectly crafted exclusive watches rolex',
    'perfectly crafted luxury timepieces',
    'perfectly crafted rolex',
    'perícia para seguro agrícola - 22 e 23 março - cascavel - pr - sc g',
    'photoshop, windows, office',
    'please do not send email to this address',
    'please read',
    'please resend spam email',
    'position opening in your area',
    'potenzprobleme - ab heute nicht mehr',
    'premier',
    'print purchase order - utiims�',
    'probieren sie es - mann lebt nur einmal',
    'project confirmation',
    'proven effective for 72 hours free trial sample available today',
    'purses',
    'qmis v4 : login',
    'qmis: rfi entry',
    'qmis: rfi view',
    'qmis: surveillance entry',
    'qualitative replica watches for most exacting people',
    'quality replicas',
    'qualysguard report',
    'quer lucrar mais com seu imóvel?',
    'quote',
    'real doctors, real science, real results!',
    'real enlargement',
    'refill reminder',
    'refill reminder, urgent',
    'refinance approved',
    'remittance advice',
    'replica handbags',
    'replica pens',
    'replica purses',
    'replica watches',
    'replica watches, bags, pens',
    'replica watches! rolex, patek philippe, vacheron ...',
    'replica-shop : luxury watches, bags, shoes',
    'report',
    'request',
    'request for a school visit results',
    'return instructions form',
    'return mail',
    'returned mail: see transcript for details',
    'rgサマーフェア◆ロイヤル会員様が2000！受け取り者に選ばれました！◆ 【24時終了】',
    'rolex',
    'rolex watches',
    'rpmllc hci report setup hourly',
    'russian dating site',
    'rxsub',
    'sales receipt amazon',
    'sales receipt from amazon',
    'sample',
    'sample submitted for analysis',
    'samples',
    'sas output',
    'schedule crawler: hourahead failure',
    'short 30 second form',
    'si compras fuera de argentina nosotros te lo traemos',
    'sidewalkway',
    'software',
    'software at low pr1ce',
    'solicitud de contacto',
    'sonarr - episode downloaded',
    'sra - improvement to the purchase order process',
    'ssf・世界支援難民救治会【最高統括】獅子山文殊',
    'staff wanted',
    'start earning the salary you deserve by obtaining the proper credentials!',
    'sua saúde não pode esperar!',
    'superstar stock report',
    'swiss branded watches',
    'tag heuer watches',
    'test',
    'thank you',
    'thank you very much',
    'thank you!',
    'thanks',
    'thanks!',
    'the most popular localized software in 1 hour',
    'the next generation in online meetings!',
    'the south fork clearwater river special supplement for suction dredge mining changes need more time and public input',
    'the ultimate online pharmaceutical',
    'the united states national medical association',
    'three steps to the software you need at the prices you want',
    'top dog training secrets revealed',
    'top of the top',
    'top quality size',
    'top secret',
    'treinamento: como negociar por telefone, e-mail e whatsapp em porto alegre',
    'usual thing',
    'vacancy - apply online',
    'very discrete shipping and billing',
    'very much',
    'view our wholesale rolex replica watches today',
    'visa line of credit',
    'votre colis a été retourné à l\'expéditeur',
    'waiting for an answer',
    'waiting for reply',
    'watches',
    'we accepted your loan request',
    'we are ready to give you a loan',
    'we have everything that you are looking for!',
    'web support query',
    'welcome to our company',
    'welcome to windows mail',
    'what they don\'t want you to know what it does to your body !',
    'what to look for when purchasing a replica watch',
    'winning notification',
    'wniosek o udostępnienie informacji publicznej',
    'work offer inside',
    'wowwow・スカパー全部見れます',
    'wowwow無料試聴無制限',
    'yahooﾗﾝｷﾝｸﾞ[r18部門]で1位を取った話題のｻｲﾄがﾘﾆｭｰｱﾙ☆',
    'you can buy phentermin on-line today!',
    'you have a meeting invitation',
    'you have a new message!',
    'you have a new personal message',
    'you have got new messages(dating)',
    'you have new message!',
    'you have notifications pending',
    'you have received an ecard',
    'you have received an greeting ecard',
    'you received online greeting card',
    'you reset your password',
    'you\'ve received a greeting ecard',
    'you\'ve received an answer to your question',
    'your family',
    'your health',
    'your life',
    'your loan request approved',
    'your order',
    'your order approved',
    'your origin electricity bill',
    'your personal discount',
    'your refill is now available',
    'zamówienie',
    'Автозалог, машина остается у Вас! За 1 час!',
    'Аренда офиса на тихой территории вдали от шума!',
    'Аренда. Офисный центр - Марьина Роща!',
    'Бросить курить за 2 дня теперь реально! Благодаря  золотым магниты!',
    'Говорящий хомяк - игрушка которая буквально взорвала сеть!',
    'ГОДОВЫЕ ШЕНГЕНСКИЕ МУЛЬТИ-ВИЗЫ',
    'Дома из бруса по типовым и индивидуальным проектам',
    'Женские роскошные сумки - Прада Гучи Шанель!!!',
    'Избавится от храпа раз и навсегда помогает мини клипса для носа!!!',
    'Изделия из Сибирского Кедра: Вагонка, Имитация бруса и др.',
    'Исключим вашу старую компаниюю из реестров,  навсегда!',
    'Исключим фирму  из реестра налоговой без проверок!',
    'ищите склад?',
    'Летающая Фея! Необыкновенная игрушка для детей!',
    'Лучшее онлайн казино всю неделю раздает деньги и мега бонусы!',
    'Лучшие игровые автоматы и реальные девушки крупье в  онлайн  в казино!',
    'Лучшие игровые автоматы рунета дарят 100 евро каждому новому игроку.',
    'Люди уже зарабатывают по 200-500$ в день в интернете, не тормози!',
    'Не надо платить комиссиию, офисы от Собственника!',
    'Недорого сдаюю офисы! 5 минут пешком от м. Марьина Роща.',
    'Низкие цены на ЦИФРОВУЮ ПЕЧАТЬ! АКЦИЯ!',
    'Новейшее игры в казино и покер рум! Дают 100 евро  за регистрацию!',
    'Новинка. Крем для увлечения члена!',
    'Новые 3d игровые автоматы! 100 ЕВРО КАЖДОМУ!',
    'Оригинальный говорящий хомяк! Лучший подарок  для всех',
    'Отличные скидки на часы с Швейцарскими механизмами!',
    'Офисы площадью от 20 кв.м в Москве! Переезд за наш счет',
    'Официальная ликвидация фирмы. Навсегда!',
    'Перечень объявлений о проведении процедур закупок',
    'Помещения под офис от собственника! У нас недорого',
    'Поможем с налоговой. Легально исключим фирму из реестров',
    'Приглашаем в театр',
    'Продам 2х этажное здание метро Марьина Роща!',
    'Продам Торговый Центр в Москве!',
    'Пряма аренда офисов -центр, дешево!',
    'Прямая аренда офисов! Метро - Марьина Роща',
    'Распродажа лучших реплик самых известных швейцарских часов',
    'Распродажа складских запасов разъемов sez (Словакия)',
    'Регистрация ООО',
    'Регистрация ООО и ИП',
    'Роскошные часы! Стильные дизайны и Швейцарскими механизмы!',
    'Сборники кино  в высоком разрешении с доставкой на дом!',
    'Сдадим офисы в Москве. Недорого.  Без посредников',
    'Сложные и сложнейшие случаи регистрации в 46 налоговой',
    'Сода для ванны с имбирем!  Лучшее средство для похудения',
    'Сумки Прада Гучи Шанель со скидкой до 80 %',
    'Таблетки и гели для лучшего секса! Мужские и женские!',
    'Таблетки и гели для страстного секса!!! Мужские и женские!',
    'Уникальная ОВОЩЕРЕЗКА из теле-магазина, но в 2 раза дешевле!!!',
    'Хватит брать деньги у родителей!',
    'Ягода Годжи! Помогут  похудеть до 23 кг за месяц и омолодить организм!',
    'בדוק את סודיות הנתונים שלך (חשבונך נפרץ על ידי האקרים).',
    'דוח שגיאות ממשק cm�',
    'הדפסת טופס קריאת שרות�',
    'あ、あぶない！！',
    'あなたが出演している動画が投稿されました。',
    'あなたが落としたのはどの財布？？',
    'あなたにどうしてもこれを見て頂きたい！',
    'あなたの「スマホいじり」がお金に変わる',
    'あなたの口座残高が日に日に倍増する・・・',
    'あなたも毎週数万～数十万円を稼いでみませんか？',
    'あなた様ですね？やっと見つけました！ずっと探してましたよ！実は',
    'あの日の事、覚えてますか？',
    'あぶない！！',
    'アホちゃうか',
    'アホでも100万円以上稼げる',
    'あらゆる幸福をget',
    'ある日気が付いたのです',
    'いかなる制限もなくあなたの自由です。',
    'いつもと違う場所からfacedookにログインしましたか？',
    'いつやるんですか？',
    'ウチのばあちゃんが100万稼いでたｗｗｗ',
    'え り',
    'えり',
    'お・か・ね・な・し',
    'オープニングバーゲン開催中',
    'おしらせ',
    'おまとめローン',
    'お仕事のご案内',
    'お仕事依頼のお申し出が御座いましたので報告申し上げます。',
    'お問い合わせいの件　-ロト６番号',
    'お客様宛てに通信費用として100万円を無償譲渡された',
    'お早う御座います。',
    'お早う御座います。届いてますか？',
    'お茶の間にいる時間が増えそうです',
    'お金、いくら必要なん？',
    'お金が理由で夢･･･諦めてませんか？',
    'お金に困っている人だけ',
    'お金に困ってるなら私に相談してよ！',
    'お金のことならどんな悩みでも相談してください！',
    'お金余ってるってことを隠したりしません',
    'お金持ちになる方法',
    'お金欲しくないですか？',
    'お願いです！！私の代わりに！',
    'カード一枚でずーっと月額無料！',
    'ガッツリ得してください★ﾗﾌﾞｴﾀｰﾅﾙお得情報★',
    'かんたんカンタン',
    'ギャンブルは、好きですか？',
    'グ　レ　ー　ゾ　ー　ン',
    'クリック！クリック！クリック！クリック！クリック！',
    'ゲストさんへ『♂love友♀』よりお知らせ',
    'ゲストさんへ『love』よりお知らせ',
    'ゲストさんへ『neo』よりお知らせ',
    'この『儲かる情報』が正しかった事を、沢山の人が実感しています。お試しあれ。',
    'この募集の公開も残りわずかとなります…',
    'この裏情報で人生が変わる！コレがミニロト黄金法力だ！！',
    'ごめんなさい。これが最後の値下げです',
    'これが「貴方の個人情報」です',
    'これで最後にします。',
    'これヤバすぎない！？',
    'ご入金のお知らせ',
    'ご愛顧ありがとうございました。',
    'ご確認ください',
    'ご自宅テレビの有料番組がずーっと無料で視聴可能',
    'ご自由にお取りください',
    'ご購入のお知らせ〔振込み依頼を受け付けました〕',
    'ご返答いただけませんか？とても悲しいですよ。やりとりは無料になっておりますし',
    'ササッとおっきしてドピュッと抜けちゃうエロ画像',
    'サヨナラ',
    'さらに値下げを断行',
    'じかんのむだ↓',
    'ジャグラー　gogoランプ★ペカッ',
    'ｼﾞｬﾝﾙで選べるｴﾛﾄﾞｳｶﾞ',
    'スカウトします',
    'スカパー！[引き落とし]',
    'スカパー！が永遠に無料で視聴できます。',
    'スター・チャンネルもwowwowもタダです',
    'スマホでポチポチ・・・45秒後・・・数万円get',
    'すみれ様より',
    'セフレや女性スポンサ ー紹介します',
    'タダでぜ～んぶ見せちゃいます♪',
    'たった今、ＡＴＭで50万下ろしてきましたよ',
    'ダメだった情報が、実は正しかったって事、ありますよね。そんな体験ができます。',
    'ち あ き',
    'ちあき',
    'チャンスは１度きり！',
    'ついにロイヤル会員様は【rg無償案内適用制度】適用か！？■【24時迄】',
    'ついに始まるロト7',
    'ってか、裏情報ぐらいだったらタダでやるのに',
    'ディープインパクト復活',
    'できたてがおいしいんです。　ごはんでも、なんでも。',
    'できたばかりの金融会社なのでとにかく貸したがっています',
    'テレビがつまらなくなった。。。',
    'どうせ貧乏でしょ？',
    'どうも、美輪明宏です。偽物に騙されないでくださいね？貴方は今',
    'とても高い位置からの情報です。無料で試せますし、儲かりますが、深入りは厳禁です。',
    'とにかく見て(*´∇`)ﾉ',
    'ナイショサマ',
    'ナイショ様',
    'なんで無視やねん？！',
    'ニートで悪いですか？',
    'にっきゅうごまんえん',
    'ねぇ？ォマンコ好き？写メ送ったから見てくれる？',
    'ノーリスクハイリターン',
    'パソコン',
    'パソコンでポチポチ・・・45秒後・・・数万円get',
    'パソコンばっかりいじるな！！',
    'パソコンメールをご利用中のお客様へ',
    'パチンコ・スロット好きな人必見!!',
    'パチンコ・パチスロを中心とした日払いスタッフ大募集！！',
    'パチンコ・パチスロ出玉ＰＲ派遣スタッフ募集！',
    'パチンコ！！パチンコ！！パチンコ！！パチンコ！！パチンコ！！パチンコ！！',
    'パチンコ＞スロット＞＞競馬＞競艇＞競輪',
    'パチンコに行って嫁に褒められる方法',
    'パチンコバイト',
    'パチンコやスロットを打ってるだけのﾊﾞｲﾄ',
    'パチンコ副業しませんか♪',
    'ばばあでも稼げる！！',
    'ファイナルバーゲン開催中',
    'フルオートシステム',
    'プロ専業主婦の',
    'へそくり',
    'ほっといても金が増えます',
    'ホントに稼ぐ気ある？',
    'まさに運命！？あなた様にピッタリ？の会員様はこちら↓',
    'まさに運命のお相手？素敵な会員様ご紹介♪',
    'まずは50万円を稼いでみてください',
    'マネージャーの長嶋です。',
    'みく',
    'みさき',
    'みさきより',
    'みた？',
    'ミニロトたった５口で当選三昧！【究極の”裏”必儲奥義】遂に公開！',
    'ミニロト予想ソフトの最高傑作初公開！購入口数わずか10口…昨年は2000万円を超えています！',
    'ミリオンゴッド神々の凱旋裏技で万枚',
    'メール・line・スカイプ',
    'メールの閲覧も送信も【完全無料】です。【23億8000万円】を受け取る際に',
    'メッセージが届いてます',
    'メルマガ',
    'もーしつこいわ！！',
    'もう、二度と言いませんわ',
    'もう…無視してください。。。',
    'もうギャンブルは終わりにしましょう。ハマっている人は病気です!',
    'もうすぐ会いに行きますね。',
    'もうどうでもいいわ',
    'もう直ぐ私は死にます',
    'もう直ぐ私は死にますからね？これが人生最後の言葉に',
    'もし・・・',
    'もし…もしも、ですよ！？',
    'もしかして',
    'もしかして、あなたって…',
    'モニタースタッフの募集です。',
    'ゆうこです。',
    'ゆきね　小児科医☆彡様より新着メッセージが届いています　◆vip room◆',
    'よだれが出るほど美味しい',
    'ランキング3部門で１位獲得の商品を驚きの価格で！',
    'リピーター続出！話題のb-casカードが驚きのキャンペーン価格！',
    'ロト６・ミニロト予想',
    'ロト６で１等最高4億円を確実に当選させる方法を伝授！',
    'ロト６で３等４等を連続当選！',
    'ロト6で生活できます。',
    'ロト６の当選数字を無料公開します',
    'ロト6の数字には全て法則があります',
    'ロト６は予想で当たるのか?',
    'ロト６モニター急募！',
    'ロト６をハッキングしました。',
    'わずかな投資で大きな当選金を得たいなら・・',
    'わたしみたいに在宅ワークで死ぬほどお金稼ぎたい人いる？？',
    '一回だけ言います。',
    '一年間で絶対に貯金1000万円を作り出す方法!!',
    '一生涯無限に資金を生み出す安定した投資法',
    '三菱東京ufjより',
    '世の中金がすべてだって、そろそろ分かった？',
    '世界で5本の指に入る支援です。ですからあなたも100％支援金の受取を出来ます。',
    '久しぶりー！覚えてる？流石に忘れちゃったかな？',
    '乗り遅れないでください。2億円当選者が溢れ返っています。',
    '予想的中率91％!!',
    '二度とメールしないね…',
    '二度とメールしません',
    '今、最終支援統合会長、まだ支援を受け取りできていない方の管理をしておりまして',
    '今からupします',
    '今すぐ確認下さい⇒僕が月収最低８０万円以上稼いでいる方法を教えます。',
    '今だけ70％offキャンペーン実施中！全てのチャンネルが無料視聴！',
    '今なら新規登録で100倍獲得キャンペーン☆',
    '今まで最高いくらの現金を見た事がありますか？',
    '今回に限り無料で次回の当選番号をお知らせします',
    '今回の当選番号について重要なお知らせ',
    '今日のおかずにどうですか？',
    '今日のお勧め投資情報',
    '今日は特別に、表と裏があるからギャンブルですが、その裏の方をを少しだけ教えます。',
    '今日も一日お疲れ様。',
    '今月値下げ実施中',
    '今週末の予想配当は1万8600円です。',
    '他社で断られた方でも、うちなら貸す自信があります！',
    '代/开――发/票',
    '代理业务！',
    '以备后用',
    '企業からメッセージが届きました',
    '低収入、借金がある、将来が不安・・・',
    '低金利キャンペーン',
    '低金利キャンペーン実施中です！',
    '佐藤えり',
    '佐藤です。',
    '余命あと僅かの命です',
    '保証人不要で50万円までお貸しします',
    '信管家@搜狗”',
    '信管家@百度”',
    '個人輸入代行をお探しなら絶対ココ！！',
    '優先販売のご案内',
    '先月までの利益1259万円！',
    '入 金 明 細',
    '入金予約完了のお知らせ',
    '入金完了',
    '全ての会員様が最終的な目的である「出会い」に最適のプランをご用意しております。',
    '全員が最大割引６９％でご購入可能',
    '全国支援専任銀行協会(jba)専務理事：錦織　剛さんからメールです♪',
    '全球最全的激情黄色视频云盘账号出售永久使用',
    '全額返金保証あり！70％offキャンペーン実施中！全てのチャンネルが無料視聴！',
    '公正資金管理局より',
    '最低日給３万円以上！短時間、高収入！事業拡大につき緊急追加大募集！',
    '最後になるかも知れません。ですからお別れの挨拶として',
    '最後の値下げで大放出',
    '最後通告',
    '最新リクルート募集【メルマガのみ】',
    '最新リクルート募集【メルマガ配信のみ応募可】',
    '最新最全国产偷拍自拍欧美日韩视频云盘合集',
    '最新版casカード',
    '出勤スケジュールに変更がありました。',
    '出玉prスタッフ',
    '利益確約',
    '副業なび',
    '副業禁止',
    '募集人数に達し次第、締め切らせていただきます↓',
    '勤務地追加につき、スタッフを緊急増員！',
    '勿論、費用は掛からずに受け取りをしたいですよね？任せてください！！',
    '千种游戏，顶级盘口，注册即送28，首存10送18,100起送388，唯一网址：7771584.com',
    '即日50万円までお貸しすることが可能です',
    '即日大金を稼げるのは当社だけです',
    '厳選した素敵な女性をご紹介します',
    '友達が弟と近親相姦してるところを見せてもらいました･･･',
    '収支報告書',
    '取り急ぎ現金が必要な方へ',
    '受信速報',
    '口コミの多い、確実な無料情報だけをお届けしています。ご確認下さい。',
    '口座情報文字化け解除のお知らせ',
    '只今から値下げします',
    '命賭けますよ',
    '国家機密情報',
    '国際支援工作員【真壁　俊哉】さんからメールです♪',
    '在宅で100万は稼げるって本当？？',
    '在宅ワークで120万',
    '在庫一掃売りつくしセール',
    '地元のオバサンを抱きたいですか？レベルは低いですが確実に抱けますよ!!',
    '地域staff急募してます',
    '大変重要なご連絡となりますので、至急のご確認をお願い致します。',
    '大川カズノリと申します',
    '大幅ディスカウント中',
    '大破格でご提供、今期最後のご奉仕品。',
    '大金8000万円全額',
    '大金ダウンロード',
    '大金借りたいなら',
    '奇跡のカードを格安で売却です',
    '契約満了にて補償のお受け取りが可能です。',
    '始めるしかない【超超超稼げる！】手法を大公開！！',
    '娘があやしいんです・・・',
    '嬉しい特典ばかり★',
    '安心のコミコミ価格',
    '完全放置収入システム',
    '完全無料のお知らせ(無料)',
    '完全無料情報です。信じられない方法ですが、数日中に５０万円のお金が手に入ります。',
    '宝くじが毎年当たっている男↓',
    '実質なにもしないで月10万',
    '家具、家電、車、家…何に使っても良いですよ！積極的に',
    '家族にもバレずにひっそりと、へそくりレベルじゃないお金…',
    '対面座位でセックスすると…アソコの密着感がガチでヤバイ',
    '専用url',
    '山本さん',
    '川村沙織様より新着メッセージが届いています　◆vip room◆',
    '希望口座登録所より',
    '年に数回、100万円振り込まれてくる↓',
    '年収1000万円ある人は無視してください。',
    '年収12億の男',
    '幸福への招待状',
    '弁護士の鈴木です。もうわかってますよね？',
    '強制変則打ち（違法）でﾍﾟﾅﾙﾃｨ回避',
    '当サイトを無料でご利用可能となりました',
    '当り予想番号をもらってみてください。',
    '当社の商品価格は総額で表示しています',
    '当選番号が確定',
    '当選確率９０％保証！構想から６年！ミニロト攻略の最終奥儀の秘密を全部公開致します。',
    '待っている状態です',
    '待っております！',
    '必要費用は【1000円】のみで御座います。文字化け解除はこちらをご確認下さいませ。',
    '必見！まさに運命のお相手！？',
    '快適なtv生活!!',
    '怒涛の投げ売りセール中',
    '急に身なりがよくなった嫁…',
    '急募!!!【バイト】',
    '急募!!!【仕事終わりに最適なﾊﾞｲﾄ】',
    '性格悪いヤツ以外、見るな',
    '恋人・割切りご紹介☆',
    '情報公開',
    '愛してます',
    '成功率１３％は完全保証します。',
    '手続き完了していない【手続き】を【無料手続き】完了しました。',
    '打ち子',
    '振り込まれました！！ご確認下さい。',
    '振込完了通知【10万円分】',
    '採用',
    '採用です',
    '操作は簡単！カードの入れ替えだけです。',
    '支払いました。',
    '支援情報登録所より',
    '支援拒否ですか？【23億8000万円】は寄付します…？',
    '支援登録のお知らせ【無料手続き】はこちら',
    '支援統合救済組合・板橋彩乃 さんからメールです♪',
    '支援総会トータルマネージメント理事会さんからメールです♪',
    '支援難民救済機関・藤鷹雅臣',
    '攻略法を無料公開！',
    '政府公認支援金「12億6000万円」の入金予約がありました。',
    '救済支援機構代表：葉山詩織様より文字化け解除要請が御座いました。',
    '数字7個中6個までは判明しております。',
    '数百万数百万数百万数百万数百万数百万数百万',
    '断言します！',
    '新着メッセージ',
    '日本初上陸！たった１錠で本物の男になる！',
    '日本資金取引支援機構総合窓口様より',
    '日本資金取引監査委員会代表・小池真理子様より',
    '旦那を教育してくれませんか？',
    '早急に安心を！',
    '明けましておめでとうございます。フリーライフです。',
    '明朗会計！',
    '昔のあなたなら',
    '映画・スポーツ・バラエティ・ドラマがすべて見放題',
    '昨年度の弊社当選金額',
    '時給：10,000～20,000円',
    '時間給にすると3000円以上',
    '普通の女性はいません',
    '月30万円稼げるのが↓',
    '月50万ぐらい稼いで家族を幸せにしてあげたらいいじゃないですか',
    '月収100万円も夢じゃない!!',
    '月収１００万円以上の簡単副業の紹介！',
    '月収100万円安心保障！！',
    '月収40万円（最低でも）のアルバイト急募',
    '月収50万円確定☆',
    '月収800万円の生活',
    '月額36,665円が、これさえあれば"0円"です♪',
    '有料放送が全て無料で視聴出来るカードを業界最安値で！',
    '期货@360”',
    '期货@ybgykj”',
    '期货@百度”',
    '期货3@百度”',
    '期货4@百度”',
    '期货ykzywlb@百度”',
    '期货交易@百度”',
    '期間限定タイムセールス実施中',
    '期間限定大特価セール',
    '本当に',
    '本心を話しますが、殺したい',
    '本日ログインされたお客様に無料でポイントプレゼント!!',
    '本日中に貴方の口座に1億円振り込ませて頂きます。',
    '本日貴方の口座に1億円',
    '札束でビンタしたりできます',
    '札束札束札束札束札束札束札束札束札束',
    '来店不要で50万円まで貸します',
    '松本真理恵直アド配信',
    '業界一の老舗で安心してお求めください',
    '業界最安値！70％off特価価格でご提供します！販売数1万枚突破！感謝セール大開催！',
    '業界最安値に挑戦',
    '極秘ﾋﾞｼﾞﾈｽ',
    '楽にかせぐ方法はあります',
    '次回の当選番号はこれだ！！！',
    '欲求を満たしませんか？',
    '死にます',
    '毎日の家計やお小遣いにお悩みの皆様へ最新情報',
    '毎月36,665円がなんと！完全無料で！',
    '毎週億万長者が生まれています',
    '気をつけてください！',
    '法律は犯さないが、規約もルールも突破する卑劣なやり方で大金を稼ぐ',
    '法律違反ぎりぎり級の裏サイト',
    '津金澤',
    '無人島に女が1人、男が50人漂着したら…',
    '無料ダウンロードサービス',
    '無料だよ',
    '無料モニターで毎月１５０万円！',
    '無料体験ですのでご安心ください。',
    '無料情報が見事的中！！来週も期待してください！！',
    '無料情報で【本当に稼げるか】試してください。',
    '無料情報で万馬券３本的中！！',
    '無職でもＯＫ',
    '無題',
    '爆裂最終値引き',
    '特別案内中★完全無料指名と20万ポイント無償追加のご依頼有！',
    '現代の錬金術です',
    '現在無料でご利用可能となっております',
    '現金100万円分の＄超豪華特典＄必ず受け取れます!!!',
    '現金1億円の写真',
    '現金30万円が代行で入金されました!',
    '現金50万円が代行で入金されました!',
    '疑ってますか？',
    '登録するだけでお金が増える、飴より美味いものがあるとしたら・・・',
    '皆様の「もう買えないの？」の声に応えて幻のb-casカード延長販売！',
    '目的では「出会い」でお間違えありませんね？',
    '相性98％以上！まさに驚異の数字です☆彡',
    '相性抜群!!98%超えの診断結果が出ております！',
    '相性診断98％超え！そのお相手様はコチラ▼',
    '相性診断結果98％超え！至急ご確認下さいませ!!',
    '知ってますか？',
    '短期・日払・高収入情報',
    '砂漠で水を売ってボロ儲けｗｗｗ',
    '確実に勝つから軍資金も用意します！！',
    '確実に貯金を増やせます。',
    '私から伝えたい要件は一つだけです。私から貴方へ1億円の支援をさせて頂きます。',
    '私が死んだ時の写真ですが',
    '私が死んでしまう前に',
    '私の「個人情報」を公開します。連絡先と住所',
    '私の裸の写真を大公開',
    '私は死にます',
    '秘密厳守できる方。',
    '秘書 飯嶋様より新着メッセージが届いています　◆vip room◆',
    '稼ぎまくるのもほどほどにね☆',
    '稼げすぎますどうしましょ',
    '稼げるモニターの募集情報',
    '競馬が全くわからない貴方もok！',
    '競馬好き必見!!',
    '競馬完全無料情報で「一発百万円」のド回収！！',
    '簡単に無料で儲けさせてくれる情報があります。',
    '簡単に無料で儲けさせてくれる情報があります。でも、数回儲けた後は止めて下さい。',
    '紙ヒコーキ作れたら100万円',
    '細川様があしあとをつけました。',
    '結婚してくれますか？',
    '結果報告',
    '給料最低5万円保証のアルバイト',
    '絶対に、短期で、稼げます',
    '絶対に絶対に最後までお読みください',
    '絶対騙される(ノД`)・゜・',
    '緊急のお知らせになります。',
    '美咲より',
    '美輪明宏です。今日中に私と連絡取れるかしら？このままだと貴方、本当に危険よ？',
    '至急、ご確認下さいませ。こちらより文字化け解除をご利用頂けます。',
    '至急、瀬川みどり様へご連絡し、427,500,000のお受け取り手続きにお進み下さい',
    '芸能人がtvでゴリ押ししていたネット術がマジですごいｗｗｗ',
    '芸能人が勧めていた副収入↓',
    '芸能人並みに稼ぐ！',
    '荒尾市',
    '衛星放送が無料で試聴できます',
    '衛星放送プレミアムなチャンネルがご自宅で無料視聴',
    '裏流出',
    '裏社会の',
    '見ないの？',
    '親子丼はお好きですか？',
    '詐欺ばっかりの業者にうんざり。。。',
    '話題のb-casカードが今なら半額以下！',
    '読む前からウソだって決めつけてるでしょ？',
    '豪華特典で間違いない',
    '貴方が【幸せになりたい】と願うなら、私がその願いを叶えてさし上げましょう。その方法は',
    '貴方が幸せになれる唯一の方法は',
    '貴方だけに教える夢や願望を叶える方法があるの。知りたければこのメールを見るのよ。',
    '貴方に「遺書」を送ります。私が死んだら',
    '貴方のご家族の事ですが',
    '貴方のパトロンになりたいのです',
    '貴方の口座に「1億円」の「返済不要の支援金」を振り込みます',
    '貴方の口座を教えて下さい。そこに「1億円」を振り込みます。',
    '貴方の口座を教えて下さい。銀行名と支店名と口座種別と口座番号と口座名義だけ',
    '貴方の口座を教えて下さいますか？その口座に「1億円」',
    '貴方の口座を教えて下さいますか？その口座に「1億円」の',
    '貴方の口座情報(銀行名/支店名/口座種別/口座番号/口座名義(カタカナ))を教えて下さい。1億円',
    '貴方の口座情報【銀行名/支店名/口座種別/口座番号/口座名義(カタカナ)】今',
    '貴方の運命を教えますね、特別に。貴方はこれから',
    '貴方への要件は一つだけです。私から貴方へ1億円の支援をさせて頂きます。',
    '貴殿へ証書の発行が完了致しました。',
    '購入口数だけが多いロト予想ソフトは捨てて！新法則採用の”本物”のロト６予想ソフト公開',
    '费用明细',
    '趣味がハマればこれ以上の副業はないです。',
    '趣味をお仕事にしてみませんか？',
    '軍資金を完全支援！！',
    '軍資金支給・全額日払いの超高待遇副業情報。',
    '近所の公衆肉便器オバサンだから誰とでもスグ生中出しokです。',
    '返済不要の支援金を1億円',
    '迷惑メールやめろ！',
    '送料・消費税完全無料中',
    '通信制限のお知らせ。',
    '連絡先はコチラ',
    '週末は給料日です。',
    '運が良い人にだけこのメールは届きます',
    '運営史上初？驚きの診断結果が出ております!!',
    '運営部も驚き！？驚異の相性98%超え!!',
    '過去にご契約頂いていた補償内容の確認をお願いいたします。',
    '違法じゃないよ',
    '適切なアドバイスをさせて下さい！',
    '遺言',
    '配信メールの指定受信について',
    '重要案内',
    '野球・サッカー・映画・コンサートなどなど。。。タダで観戦！',
    '金利は普通。とにかく最速',
    '金持ちの人はもういいですから',
    '鈴木志穂様より',
    '鉄板競馬☆攻略情報サイト☆',
    '銀行よりお知らせ',
    '銀行口座・おなまえを登録してください。振込完了',
    '閉店間近！大セール',
    '闇金ではないので',
    '限定！バイナリーオプション必勝法のご案内',
    '隅々まで鮮明に見える私の全裸の写真',
    '電話番号で友だちが追加されました。',
    '青田〓pt譲渡希望〓様より新着メッセージが届いています　◆vip room◆',
    '項目をクリア出来る人限定',
    '騙された！！',
    '驚きの診断結果が出ました！至急ご確認下さいませ!!',
    '驚愕の事実をあなたに',
    '高倉様はご存知でしょうか？特別依頼を承っておりますのでご確認下さいませ♪',
    '高収入モニタースタッフ募集',
    '高級な女性',
    '高額当選者様へ',
    '高額当選者続出の裏ワザを公開します',
    '魔法のb-casカードを叩き売り',
    '鮎川京子',
    '黒木様から500万円ギフトボックス及び動画メッセージが届いております。',
])
