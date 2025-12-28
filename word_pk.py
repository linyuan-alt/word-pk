import streamlit as st
import random
import base64

# ---------------------------
# 页面配置
# ---------------------------
st.set_page_config(page_title="单词 PK 大赛", layout="centered")

# ---------------------------
# 背景图片
# ---------------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded});
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("bg.jpg")

# ---------------------------
# 背景音乐（自动播放）
# ---------------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
    md = f"""
    <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

autoplay_audio("bgm.mp3")

# ---------------------------
# 单词库
# ---------------------------
WORDS = [
    ("evening", "晚上"), ("forest", "森林"), ("sail", "航行"),
    ("piano", "钢琴"), ("secret", "秘密"), ("message", "信息"),
    ("point", "指向"), ("shout", "大喊"), ("laugh", "大笑"),
    ("invite", "邀请"), ("why", "为什么"), ("again", "再次"),
    ("think", "想"), ("call", "叫"), ("look (like)", "看起来……什么样"),
    ("stop → stopped", "停止（过去式）"),
    ("try → tried", "尝试（过去式）"),
    ("has/have got", "有"),
    ("a lot / lots of", "许多"),
    ("video", "视频"),
    ("together", "一起"),
    ("same", "相同的"),
    ("thing", "事情/事物"),
    ("tell", "讲"),
    ("joke", "笑话"),
    ("sports", "运动"),
    ("be good at", "擅长"),
    ("draw", "画画"),
    ("share", "分享"),
    ("pretty", "美丽的"),
    ("kind", "友好的/善良的"),
    ("chocolate", "巧克力"),
    ("clothes", "衣服"),
    ("special", "特别的"),
    ("singer", "歌手"),
    ("active", "活跃的"),
    ("yoga", "瑜伽"),
    ("attention", "注意"),
    ("detail", "细节"),
    ("curly", "卷曲的"),
    ("skirt", "裙子"),
    ("shoe tongue", "鞋舌"),
    ("correct", "正确的"),
    ("town", "小镇"),
    ("different", "不同的"),
    ("today", "今天"),
    ("sure", "当然"),
    ("buy", "买"),
    ("build", "建造"),
    ("of course", "当然"),
    ("extra", "多余的"),
    ("spider", "蜘蛛"),
    ("real", "真实的"),
    ("go shopping", "去购物"),
    ("heart", "心"),
    ("necklace", "项链"),
]

# ---------------------------
# 状态初始化
# ---------------------------
if "score_a" not in st.session_state:
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)

# ---------------------------
# 标题
# ---------------------------
st.markdown(
    "<h1 style='text-align:center;color:white;'>🔥 单词 PK 大赛 🔥</h1>",
    unsafe_allow_html=True
)

# ---------------------------
# 当前单词
# ---------------------------
st.markdown(
    f"""
    <div style="
        background: rgba(0,0,0,0.6);
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        color: white;
        font-size: 48px;
        font-weight: bold;
    ">
        {st.session_state.word[0]}
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------------------
# 按钮区
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("👤 玩家 A 答对"):
        st.session_state.score_a += 1
        st.session_state.word = random.choice(WORDS)

with col2:
    if st.button("👤 玩家 B 答对"):
        st.session_state.score_b += 1
        st.session_state.word = random.choice(WORDS)

if st.button("➡️ 下一个单词（无人答对）"):
    st.session_state.word = random.choice(WORDS)

# ---------------------------
# 答案
# ---------------------------
with st.expander("📖 查看中文答案"):
    st.markdown(
        f"<h3 style='color:white;'>{st.session_state.word[1]}</h3>",
        unsafe_allow_html=True
    )

# ---------------------------
# 积分板
# ---------------------------
st.markdown(
    f"""
    <div style="
        background: rgba(0,0,0,0.6);
        padding: 20px;
        border-radius: 15px;
        color: white;
        font-size: 24px;
    ">
        🏆 玩家 A：{st.session_state.score_a} 分<br>
        🏆 玩家 B：{st.session_state.score_b} 分
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------
# 重置
# ---------------------------
if st.button("🔄 重置游戏"):
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)
