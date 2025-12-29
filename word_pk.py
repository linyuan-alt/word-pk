import streamlit as st
import random

# =========================
# 页面设置
# =========================
st.set_page_config(
    page_title="单词 PK 游戏",
    layout="centered"
)

# =========================
# 单词库（已合并）
# =========================
WORDS = [
    # 原有词汇
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
    ("thing", "事情 / 事物"),
    ("tell", "讲"),
    ("joke", "笑话"),
    ("sports", "运动"),
    ("be good at", "擅长"),
    ("draw", "画画"),
    ("share", "分享"),
    ("pretty", "美丽的"),
    ("kind", "友好的 / 善良的"),
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

    # 家庭与人物
    ("age", "年龄"),
    ("aunt", "阿姨 / 姑姑"),
    ("boy", "男孩"),
    ("brother", "兄弟"),
    ("child", "孩子"),
    ("children", "孩子们"),
    ("cousin", "堂 / 表兄弟姐妹"),
    ("dad", "爸爸"),
    ("daughter", "女儿"),
    ("family", "家庭"),
    ("father", "父亲"),
    ("friend", "朋友"),
    ("girl", "女孩"),
    ("grandad", "爷爷 / 外公"),
    ("grandchild", "孙子 / 孙女"),
    ("granddaughter", "孙女"),
    ("grandfather", "祖父"),
    ("grandma", "奶奶 / 外婆"),
    ("grandmother", "祖母"),
    ("grandpa", "爷爷"),
    ("grandparent", "祖父母"),
    ("grandson", "孙子"),
    ("grown-up", "成年人"),
    ("kid", "孩子"),
    ("love", "爱"),
    ("man (men)", "男人"),
    ("mother", "母亲"),
    ("Mr", "先生"),
    ("Mrs", "太太"),
    ("Ms", "女士"),
    ("mum (mom)", "妈妈"),
    ("old", "年老的"),
    ("parent", "父母"),
    ("people", "人们"),
    ("person", "人"),
    ("sister", "姐妹"),
    ("son", "儿子"),
    ("uncle", "叔叔 / 舅舅"),
    ("who", "谁"),
    ("woman (women)", "女人"),
    ("young", "年轻的"),

    # 关系 / 身份
    ("adult", "成年人"),
    ("aged", "年老的"),
    ("birth", "出生"),
    ("born", "出生的"),
    ("boyfriend", "男朋友"),
    ("friendly", "友好的"),
    ("girlfriend", "女朋友"),
    ("granny", "奶奶"),
    ("group", "群体"),
    ("guest", "客人"),
    ("guy", "家伙 / 男子"),
    ("husband", "丈夫"),
    ("identification", "身份证明"),
    ("married", "已婚的"),
    ("neighbour (neighbor)", "邻居"),
    ("partner", "伴侣"),
    ("penfriend", "笔友"),
    ("surname", "姓"),
    ("teenager", "青少年"),
    ("wife", "妻子"),
    ("first name", "名"),
    ("get married", "结婚"),
    ("ID card", "身份证"),
    ("pen", "钢笔"),

    # 亲属关系 / 动作
    ("anniversary", "纪念日"),
    ("childhood", "童年"),
    ("father-in-law", "岳父 / 公公"),
    ("middle-aged", "中年的"),
    ("mother-in-law", "岳母 / 婆婆"),
    ("nephew", "侄子 / 外甥"),
    ("niece", "侄女 / 外甥女"),
    ("relative", "亲戚"),
    ("bring up", "抚养"),
    ("get divorced", "离婚"),
    ("get on with", "与……相处"),
]

# =========================
# 初始化状态
# =========================
if "score_a" not in st.session_state:
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)

# =========================
# 页面标题
# =========================
st.title("🎮 单词 PK 游戏（双人）")

# =========================
# 当前单词
# =========================
st.markdown("## 🔤 当前单词")
st.markdown(
    f"<h1 style='text-align:center'>{st.session_state.word[0]}</h1>",
    unsafe_allow_html=True
)

# =========================
# PK 按钮
# =========================
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

if st.button("➡️ 下一个单词（无人答对）"):
    st.session_state.word = random.choice(WORDS)

# =========================
# 查看答案
# =========================
with st.expander("📖 查看中文答案"):
    st.write(st.session_state.word[1])

# =========================
# 积分板
# =========================
st.markdown("## 🏆 当前积分")
st.write(f"👤 玩家 A：**{st.session_state.score_a} 分**")
st.write(f"👤 玩家 B：**{st.session_state.score_b} 分**")

# =========================
# 重置
# =========================
if st.button("🔄 重置游戏"):
    st.session_state.score_a = 0
    st.session_state.score_b = 0
    st.session_state.word = random.choice(WORDS)
