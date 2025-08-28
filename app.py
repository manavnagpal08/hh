import streamlit as st

st.set_page_config(page_title="Visme Style Form", layout="wide")

# Custom CSS to mimic Visme style
st.markdown("""
    <style>
    body {
        background-color: #4267F5;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    .left {
        flex: 1;
        text-align: center;
    }
    .right {
        flex: 1;
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin-right: 10%;
        margin-left: 5%;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        text-align: center;
        color: #333;
    }
    input, textarea {
        border-radius: 10px !important;
        padding: 0.8rem !important;
        margin-bottom: 1rem !important;
        border: 1px solid #ddd !important;
    }
    .stButton button {
        background: linear-gradient(135deg, #28a745, #34d058);
        color: white;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 0.8rem;
        border-radius: 10px;
        width: 100%;
        transition: background 0.3s ease-in-out;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #34d058, #28a745);
    }
    </style>
""", unsafe_allow_html=True)

# Layout (2 columns)
col1, col2 = st.columns([1,1])

with col1:
    st.image("https://cdn3d.iconscout.com/3d/premium/thumb/businessman-5678594-4731219.png", width=350)  # sample 3D character

with col2:
    st.markdown('<div class="right">', unsafe_allow_html=True)
    st.markdown('<div class="title">What’s your name?</div>', unsafe_allow_html=True)

    name = st.text_input("Name", placeholder="First Name")
    surname = st.text_input("Surname", placeholder="Last Name")
    email = st.text_input("Email", placeholder="Ex. yourname@company.com")

    if st.button("Next"):
        # TODO: Integrate with Firebase
        st.success(f"Saved: {name} {surname}, {email}")

    st.markdown('</div>', unsafe_allow_html=True)
