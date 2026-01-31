import streamlit as st
from chains import get_helpdesk_chain


st.set_page_config(
    page_title="Smart Helpdesk Chatbot",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>
    .main {
        background-color: #0f1117;
        color: white;
    }
    .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    .stChatMessage {
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)


st.title("🤖 Smart Helpdesk Chatbot")
st.caption("LangChain • Groq • Conversation Memory")

st.divider()


if "chain" not in st.session_state:
    st.session_state.chain = get_helpdesk_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


user_input = st.chat_input("Describe your issue...")

if user_input:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.spinner("Analyzing your issue..."):
        from router import route_query
        response = route_query(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
    with st.chat_message("assistant"):
        st.markdown(response)


st.divider()
st.caption(" Smart Helpdesk Chatbot")
