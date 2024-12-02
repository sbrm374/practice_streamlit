import streamlit as st

print("page reloaded")
st.set_page_config(
    page_title="ポケモンずかん",
    page_icon="./images/monsterball.png"
)
st.markdown("""
<style>
img {
    max-height: 300px;
}
.st-emotion-cache-1clstc5 div {
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.st-emotion-cache-p5msec {
    pointer-events: none;
}

[data-testid="stBaseButton-elementToolbar"] {
    visibility: hidden;
}
</style>        
""", unsafe_allow_html=True)

st.title("streamlit ポケモンずかん")
st.markdown("**ポケモン**を1匹ずつ追加して図鑑を完成させましょう！")

type_emoji_dict = {
    "ノーマル": "⚪",
    "かくとう": "✊",
    "ひこう": "🕊",
    "どく": "☠️",
    "じめん": "🌋",
    "いわ": "🪨",
    "むし": "🐛",
    "ゴースト": "👻",
    "はがね": "🤖",
    "ほのお": "🔥",
    "みず": "💧",
    "くさ": "🍃",
    "でんき": "⚡",
    "エスパー": "🔮",
    "こおり": "❄️",
    "ドラゴン": "🐲",
    "あく": "😈",
    "フェアリー": "🧚"
}

initial_pokemons = [
    {
        "name": "ピカチュウ",
        "types": ["でんき"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "ヌオー",
        "types": ["みず", "じめん"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "ギャラドス",
        "types": ["みず", "ひこう"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "ゲッコウガ",
        "types": ["みず", "あく"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "ルカリオ",
        "types": ["かくとう", "はがね"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "エースバーン",
        "types": ["ほのお"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon = {
    "name": "ディグダ（アローラのすがた）",
    "types": ["じめん", "はがね"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons
    
auto_complete = st.toggle("サンプルデータで埋める")
print("page_reload, auto_complete", auto_complete)
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="ポケモンの名前",
            value=example_pokemon["name"] if auto_complete else ""
        )
    with col2:
        types = st.multiselect(
            label="ポケモンのタイプ", 
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="ポケモンのイメージ URL",
        value=example_pokemon["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("ポケモンの名前を入力してください。")
        elif len(types) == 0:
            st.error("ポケモンのタイプを少なくとも1つ選んでください。")
        else:
            st.success("ポケモンを追加できます。")
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url": image_url if image_url else "./images/default.png"
            })

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):    
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon["name"]}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types)) 
                delete_button = st.button(label="削除", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    st.rerun()
