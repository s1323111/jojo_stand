import streamlit as st
import random

# スタンドデータ
STANDS = {
    "スタープラチナ": {
        "user": "空条承太郎",
        "part": "第3部",
        "ability": "精密な動作と圧倒的なパワー",
        "description": "近距離パワー型の最強格スタンド。「オラオラオラ」の連続攻撃と精密動作性でどんな敵も粉砕する。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "C", "持続力": "A", "精密動作性": "A", "成長性": "A"},
        "color": "#4169E1"
    },
    "ハーミットパープル": {
        "user": "ジョセフ・ジョースター",
        "part": "第3部",
        "ability": "念写と透視能力",
        "description": "茨状のスタンドで情報収集に特化。写真や液晶画面を通じて遠くの情報を得ることができる。",
        "stats": {"破壊力": "D", "スピード": "C", "射程距離": "D", "持続力": "A", "精密動作性": "D", "成長性": "E"},
        "color": "#8B4513"
    },
    "ハイエロファントグリーン": {
        "user": "花京院典明",
        "part": "第3部",
        "ability": "遠距離攻撃とエメラルドスプラッシュ",
        "description": "緑色の人型スタンド。体を解体して遠距離攻撃や偵察が可能。エメラルドスプラッシュで敵を貫く。",
        "stats": {"破壊力": "C", "スピード": "B", "射程距離": "A", "持続力": "B", "精密動作性": "C", "成長性": "D"},
        "color": "#228B22"
    },
    "シルバーチャリオッツ": {
        "user": "ジャン・ピエール・ポルナレフ",
        "part": "第3部",
        "ability": "高速剣技と鎧脱着",
        "description": "西洋騎士の姿をしたスタンド。レイピアによる高速剣技で敵を圧倒。鎧を脱ぐことでさらなる高速化が可能。",
        "stats": {"破壊力": "C", "スピード": "A", "射程距離": "C", "持続力": "C", "精密動作性": "B", "成長性": "C"},
        "color": "#C0C0C0"
    },
    "ザ・ワールド": {
        "user": "DIO",
        "part": "第3部",
        "ability": "時間停止",
        "description": "時を止める究極の能力を持つスタンド。停止時間中は自分だけが動くことができる最強の能力。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "C", "持続力": "A", "精密動作性": "A", "成長性": "B"},
        "color": "#FFD700"
    },
    "クレイジーダイヤモンド": {
        "user": "東方仗助",
        "part": "第4部",
        "ability": "物体の修復・復元",
        "description": "壊れた物を直すことができる治癒系スタンド。ただし本人だけは治せない。「ドラララ」の拳撃も強力。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "D", "持続力": "B", "精密動作性": "B", "成長性": "C"},
        "color": "#FF1493"
    },
    "ゴールド・エクスペリエンス": {
        "user": "ジョルノ・ジョバァーナ",
        "part": "第5部",
        "ability": "生命創造",
        "description": "無機物に生命を与える創造の力。攻撃を受けた相手の感覚を暴走させる能力も持つ。",
        "stats": {"破壊力": "C", "スピード": "A", "射程距離": "E", "持続力": "D", "精密動作性": "C", "成長性": "A"},
        "color": "#FFD700"
    },
    "キング・クリムゾン": {
        "user": "ディアボロ",
        "part": "第5部",
        "ability": "時間飛躍と未来予知",
        "description": "時を飛び越し、エピタフで未来を予知する。運命を見通し、危険な時間を削り取る恐るべき能力。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "E", "持続力": "A", "精密動作性": "?", "成長性": "?"},
        "color": "#DC143C"
    },
    "ストーン・フリー": {
        "user": "空条徐倫",
        "part": "第6部",
        "ability": "糸状化と操作",
        "description": "自分の体を糸状に分解して様々な用途に使用。ネットや罠を作ったり、遠距離攻撃も可能。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "C", "持続力": "A", "精密動作性": "C", "成長性": "A"},
        "color": "#4682B4"
    },
    "スティッキィ・フィンガーズ": {
        "user": "ブローノ・ブチャラティ",
        "part": "第5部",
        "ability": "ジッパー創造",
        "description": "あらゆるものにジッパーを付けて開閉可能。空間移動や攻撃、防御など多彩な戦術が可能。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "E", "持続力": "C", "精密動作性": "C", "成長性": "C"},
        "color": "#0000FF"
    },
    "エアロスミス": {
        "user": "ナランチャ・ギルガ",
        "part": "第5部",
        "ability": "戦闘機型攻撃",
        "description": "小型戦闘機の形をした攻撃特化スタンド。機銃とミサイルで敵を爆撃。CO2感知レーダー付き。",
        "stats": {"破壊力": "B", "スピード": "B", "射程距離": "A", "持続力": "C", "精密動作性": "E", "成長性": "C"},
        "color": "#FF4500"
    },
    "セックス・ピストルズ": {
        "user": "グイード・ミスタ",
        "part": "第5部",
        "ability": "弾丸軌道操作",
        "description": "6体の小さな精霊が弾丸の軌道を操作。No.1〜7（4を除く）の個性豊かなピストルズたち。",
        "stats": {"破壊力": "E", "スピード": "C", "射程距離": "B", "持続力": "A", "精密動作性": "A", "成長性": "B"},
        "color": "#800080"
    },
    "スパイス・ガール": {
        "user": "トリッシュ・ウナ",
        "part": "第5部",
        "ability": "軟化能力",
        "description": "触れた物を柔らかくして攻撃を無効化したり、ゴムのような弾性を与える防御特化のスタンド。",
        "stats": {"破壊力": "A", "スピード": "A", "射程距離": "C", "持続力": "B", "精密動作性": "C", "成長性": "A"},
        "color": "#FF69B4"
    },
    "キラークイーン": {
        "user": "吉良吉影",
        "part": "第4部",
        "ability": "爆破能力",
        "description": "触れたものを爆弾に変える恐るべき能力。シアーハートアタックという自動追尾爆弾も操る。",
        "stats": {"破壊力": "A", "スピード": "B", "射程距離": "D", "持続力": "B", "精密動作性": "B", "成長性": "A"},
        "color": "#FFB6C1"
    },
    "ヘブンズドア": {
        "user": "岸辺露伴",
        "part": "第4部",
        "ability": "記憶読み取り・書き込み",
        "description": "相手を本のページにして記憶を読み取り、新たな記憶や命令を書き込める情報操作系スタンド。",
        "stats": {"破壊力": "E", "スピード": "B", "射程距離": "B", "持続力": "B", "精密動作性": "A", "成長性": "A"},
        "color": "#00CED1"
    },
    "エコーズ": {
        "user": "広瀬康一",
        "part": "第4部",
        "ability": "音響効果",
        "description": "成長型スタンド。ACT1は擬音を実体化、ACT2は擬音効果を与え、ACT3は重力操作が可能。",
        "stats": {"破壊力": "B", "スピード": "B", "射程距離": "B", "持続力": "B", "精密動作性": "C", "成長性": "A"},
        "color": "#32CD32"
    }
}

# 質問データ
QUESTIONS = [
    {
        "question": "困った状況に直面した時、あなたはどうしますか？",
        "options": [
            ("正面から力で解決する", ["スタープラチナ", "クレイジーダイヤモンド", "キラークイーン"]),
            ("情報収集してから行動する", ["ハーミットパープル", "ヘブンズドア", "エコーズ"]),
            ("戦略的に迂回して解決する", ["ハイエロファントグリーン", "スティッキィ・フィンガーズ", "スパイス・ガール"]),
            ("時を待って機会を狙う", ["ザ・ワールド", "キング・クリムゾン", "エアロスミス"])
        ]
    },
    {
        "question": "戦闘スタイルはどれが好みですか？",
        "options": [
            ("近距離で拳と拳の勝負", ["スタープラチナ", "クレイジーダイヤモンド", "スティッキィ・フィンガーズ"]),
            ("遠距離から安全に攻撃", ["ハイエロファントグリーン", "エアロスミス", "セックス・ピストルズ"]),
            ("トリッキーな戦法で翻弄", ["キラークイーン", "ストーン・フリー", "スパイス・ガール"]),
            ("頭脳戦で相手を出し抜く", ["ハーミットパープル", "ヘブンズドア", "キング・クリムゾン"])
        ]
    },
    {
        "question": "仲間との関係はどうですか？",
        "options": [
            ("リーダーシップを取る", ["スタープラチナ", "ゴールド・エクスペリエンス", "ストーン・フリー"]),
            ("サポートに回る", ["ハーミットパープル", "セックス・ピストルズ", "スパイス・ガール"]),
            ("単独行動を好む", ["キラークイーン", "ザ・ワールド", "キング・クリムゾン"]),
            ("チームワークを重視", ["シルバーチャリオッツ", "スティッキィ・フィンガーズ", "エコーズ"])
        ]
    },
    {
        "question": "どんな能力に魅力を感じますか？",
        "options": [
            ("圧倒的な破壊力", ["スタープラチナ", "クレイジーダイヤモンド", "エアロスミス"]),
            ("時間や空間の操作", ["ザ・ワールド", "キング・クリムゾン", "スティッキィ・フィンガーズ"]),
            ("創造や修復の力", ["クレイジーダイヤモンド", "ゴールド・エクスペリエンス", "ストーン・フリー"]),
            ("情報や心理の操作", ["ハーミットパープル", "ヘブンズドア", "スパイス・ガール"])
        ]
    },
    {
        "question": "普段の性格は？",
        "options": [
            ("熱血で情熱的", ["スタープラチナ", "シルバーチャリオッツ", "エアロスミス"]),
            ("冷静で分析的", ["ハイエロファントグリーン", "ヘブンズドア", "キング・クリムゾン"]),
            ("優しく思いやりがある", ["クレイジーダイヤモンド", "ゴールド・エクスペリエンス", "スパイス・ガール"]),
            ("マイペースで個性的", ["ハーミットパープル", "ストーン・フリー", "エコーズ"])
        ]
    },
    {
        "question": "ピンチの時の対処法は？",
        "options": [
            ("全力で正面突破", ["スタープラチナ", "クレイジーダイヤモンド", "スティッキィ・フィンガーズ"]),
            ("冷静に状況分析", ["ハーミットパープル", "ハイエロファントグリーン", "ヘブンズドア"]),
            ("機転を利かせて逆転", ["ゴールド・エクスペリエンス", "ストーン・フリー", "エコーズ"]),
            ("決定的な一撃を狙う", ["ザ・ワールド", "キラークイーン", "キング・クリムゾン"])
        ]
    },
    {
        "question": "理想的な戦場環境は？",
        "options": [
            ("開けた場所での正面勝負", ["スタープラチナ", "シルバーチャリオッツ", "エアロスミス"]),
            ("入り組んだ地形を活かす", ["ハイエロファントグリーン", "ストーン・フリー", "スティッキィ・フィンガーズ"]),
            ("準備時間がある計画戦", ["ハーミットパープル", "キラークイーン", "ヘブンズドア"]),
            ("予測不能な乱戦", ["ゴールド・エクスペリエンス", "セックス・ピストルズ", "エコーズ"])
        ]
    },
    {
        "question": "最も大切にするものは？",
        "options": [
            ("正義と仲間", ["スタープラチナ", "クレイジーダイヤモンド", "ゴールド・エクスペリエンス"]),
            ("知識と真実", ["ハーミットパープル", "ハイエロファントグリーン", "ヘブンズドア"]),
            ("自由と個性", ["ストーン・フリー", "エアロスミス", "エコーズ"]),
            ("静寂と完璧", ["ザ・ワールド", "キラークイーン", "キング・クリムゾン"])
        ]
    }
]

def calculate_stand_score(answers):
    """回答からスタンドのスコアを計算"""
    score = {}
    
    # すべてのスタンドのスコアを0で初期化
    for stand in STANDS.keys():
        score[stand] = 0
    
    # 各回答からスコアを加算
    for answer in answers:
        for stand in answer:
            if stand in score:
                score[stand] += 1
    
    return score

def get_result_stand(score):
    """スコアから結果のスタンドを決定"""
    max_score = max(score.values())
    candidates = [stand for stand, s in score.items() if s == max_score]
    
    # 同点の場合はランダムで選択
    return random.choice(candidates)

def display_stand_result(stand_name):
    """スタンドの結果を表示"""
    stand = STANDS[stand_name]
    
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, {stand['color']}22, {stand['color']}11); 
                padding: 2rem; border-radius: 15px; border: 2px solid {stand['color']}; margin: 1rem 0;">
        <h2 style="color: {stand['color']}; text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">
            🌟 あなたのスタンドは... 🌟
        </h2>
        <h1 style="color: {stand['color']}; text-align: center; font-size: 3rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
            {stand_name}
        </h1>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"""
        ### 📋 基本情報
        - **スタンド使い**: {stand['user']}  
        - **登場部**: {stand['part']}  
        - **能力**: {stand['ability']}
        
        ### 📖 説明
        {stand['description']}
        """)
    
    with col2:
        st.markdown("### 📊 スタンド能力値")
        for stat, value in stand['stats'].items():
            st.markdown(f"**{stat}**: `{value}`")

def main():
    # ページ設定
    st.set_page_config(
        page_title="ジョジョ スタンド能力診断",
        page_icon="⭐",
        layout="wide"
    )
    
    # カスタムCSS
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4, #FFEAA7);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        border: 3px solid #FFD700;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .question-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 2px solid #4169E1;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: bold;
        width: 100%;
        margin: 0.2rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # メインヘッダー
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; font-size: 3.5rem; text-shadow: 3px 3px 6px rgba(0,0,0,0.5); margin: 0;">
            ⭐ ジョジョ スタンド能力診断 ⭐
        </h1>
        <h3 style="color: #FFD700; text-shadow: 2px 2px 4px rgba(0,0,0,0.7); margin: 0.5rem 0 0 0;">
            〜 あなたに最適なスタンド能力を診断します 〜
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # セッション状態の初期化
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.answers = []
        st.session_state.finished = False
    
    if not st.session_state.finished:
        # 診断中
        if st.session_state.current_question < len(QUESTIONS):
            question = QUESTIONS[st.session_state.current_question]
            
            st.markdown(f"""
            <div class="question-container">
                <h2 style="color: white; text-align: center;">
                    質問 {st.session_state.current_question + 1} / {len(QUESTIONS)}
                </h2>
                <h3 style="color: #FFD700; text-align: center;">
                    {question['question']}
                </h3>
            </div>
            """, unsafe_allow_html=True)
            
            # 選択肢をボタンで表示
            col1, col2 = st.columns(2)
            
            for i, (option_text, stands) in enumerate(question['options']):
                col = col1 if i % 2 == 0 else col2
                
                if col.button(option_text, key=f"option_{i}"):
                    st.session_state.answers.append(stands)
                    st.session_state.current_question += 1
                    st.rerun()
            
            # プログレスバー
            progress = st.session_state.current_question / len(QUESTIONS)
            st.progress(progress)
            
        else:
            # 診断完了
            st.session_state.finished = True
            st.rerun()
    
    else:
        # 結果表示
        score = calculate_stand_score(st.session_state.answers)
        result_stand = get_result_stand(score)
        
        display_stand_result(result_stand)
        
        # 再診断ボタン
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🔄 もう一度診断する", key="restart"):
                st.session_state.current_question = 0
                st.session_state.answers = []
                st.session_state.finished = False
                st.rerun()
        
        # スタンド一覧表示
        with st.expander("📚 全スタンド一覧を見る"):
            cols = st.columns(3)
            for i, (name, data) in enumerate(STANDS.items()):
                with cols[i % 3]:
                    st.markdown(f"""
                    **{name}**  
                    使い手: {data['user']}  
                    {data['part']}  
                    """)

if __name__ == "__main__":
    main()