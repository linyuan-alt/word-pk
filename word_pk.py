import streamlit as st
import random

# ---------------------------
# 单词库（英文 - 中文）
# ---------------------------
WORDS = [
    ("evening", "晚上"),
    ("forest", "森林"),
    ("sail", "航行"),
    ("piano", "钢琴"),
    ("secret", "秘密"),
    ("message", "信息"),
    ("point", "指向"),
    ("shout", "大喊"),
    ("laugh", "大笑"),
    ("invite", "邀请"),
    ("why", "为什么"),
    ("again", "再次"),
    ("think", "想"),
    ("call", "叫"),
    ("look (like)", "看起来……什么样"),
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
# 初始化状态
# ---------------------------
if "score_a" not in st.session_state:
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)

# ---------------------------
# 页面标题
# ---------------------------
st.title("🎮 单词 PK 游戏（双人）")

# ---------------------------
# 显示当前单词
# ---------------------------
st.markdown("## 🔤 当前单词")
st.markdown(
    f"<h1 style='text-align:center'>{st.session_state.word[0]}</h1>",
    unsafe_allow_html=True
)

# ---------------------------
# 按钮区
# ---------------------------
st.markdown("### ✅ 谁答对了？")

col1, col2 = st.columns(2)

with col1:
    if st.button("👤 玩家 A 答对"):
        st.session_state.score_a += 1
        st.session_state.word = random.choice(WORDS)

with col2:
    if st.button("👤 玩家 B 答对"):
        st.session_state.score_b += 1
        st.session_state.word = random.choice(WORDS)

# ---------------------------
# 下一个单词
# ---------------------------
if st.button("➡️ 下一个单词（无人答对）"):
    st.session_state.word = random.choice(WORDS)

# ---------------------------
# 显示答案（可选）
# ---------------------------
with st.expander("📖 查看中文答案"):
    st.write(st.session_state.word[1])

# ---------------------------
# 积分板
# ---------------------------
st.markdown("## 🏆 当前积分")
st.write(f"👤 玩家 A：**{st.session_state.score_a} 分**")
st.write(f"👤 玩家 B：**{st.session_state.score_b} 分**")

# ---------------------------
# 重置按钮
# ---------------------------
if st.button("🔄 重置游戏"):
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)
