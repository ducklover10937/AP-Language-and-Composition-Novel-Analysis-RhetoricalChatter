import streamlit as st

#The following code has been revised from a previous project to fit the functions of RhetoricalChatter!!

st.set_page_config(
    page_title="RhetoricalChatter",
    page_icon="RhetoricalChatter.ico",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown("""<style>.stApp { background-color: #a6a085; color: #332815; } </style>""", unsafe_allow_html=True)
st.markdown("""<style>.stButton { background-color: #fffbd4; color: #c9924f; }</style>""", unsafe_allow_html=True)
st.markdown("<h1 style = 'text-align: center;'>RhetoricalChatter</h1>", unsafe_allow_html=True)
st.markdown("<p style = 'text-align: center;'>Learn about <i>The Catcher in the Rye</i> with RhetoricalChatter!</p>", unsafe_allow_html=True)

#msg = ""
errorMsg = "I'm sorry, I couldn't understand your request."

chatContainer = st.container()
chat = st.text_input("What would you like to learn about The Catcher in the Rye?", value="", key="chatInput")

analysisDict = {
    ("introduce", "introduction", "summary", "summarize", "overview"): "The Catcher in the Rye by J.D. Salinger explores the coming-of-age experience through the "
    "viewpoint of a struggling adolescent—Holden Caulfield. Salinger introduces Holden as a delinquent who had recently been expelled from Pencey Prep. "
    "Pressured to fit in, appear mature, and face the demands of approaching adulthood, Holden shares casual anecdotes about his shifting identity to communicate "
    "a firsthand account about his desires to escape 'phoniness.'",
    ("theme","thematic","themes","idea","topic"): "The Catcher in the Rye explores the loss of childhood innocence and the search for acceptance in the adult world.",
    ("rhetoric","device","rhetorical device"): "In The Catcher in the Rye, Salinger combines the use of colloquial diction, symbolism, hypophora, and anecdotes to develop a complex account of the adolescent concerns.",
   # ("examples", "example", "rhetorical device examples"): ["1. Colloquial Diction: "]
}

if "chatHistory" not in st.session_state:
    st.session_state.chatHistory = [] 

def respond(chat): 
    chat = chat.lower() 

    for theme, ans in analysisDict.items(): 
        return ans
    return errorMsg

if st.button("Send") and chat.strip() != "": 
    st.session_state.chatHistory.append(chat)
    
    analysis = respond(chat) 
    st.session_state.chatHistory.append(analysis)

    st.rerun()

with chatContainer: #chat history
    for chatEntry in st.session_state.chatHistory:        
        if "The Catcher in the Rye by J.D. Salinger explores the coming-of-age" in chatEntry or "The Catcher in the Rye explores the loss of childhood innocence" in chatEntry or "In The Catcher in the Rye, Salinger combines the use of colloquial diction," in chatEntry or errorMsg in chatEntry:
            st.markdown("<div style='background-color: #61503b; color: #f7ecd5; text-align: left; overflow-wrap:break-word; display:inline-block; padding: 10px; border-radius: 20px;'>"+chatEntry+"</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div style='background-color: #fffbd4; color: #332815; text-align: left; overflow-wrap:break-word; float: right;display:inline-block; padding: 10px; border-radius: 20px;'>"+chatEntry+"</div>", unsafe_allow_html=True)




