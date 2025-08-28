import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Animated Login", layout="centered")

# Inject CSS animations
st.markdown("""
    <style>
    body {
        background: #f5f7fa;
    }
    .card {
        max-width: 400px;
        margin: auto;
        padding: 2rem;
        background: white;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.5s ease-in-out;
    }
    .card:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }
    .title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        text-align: center;
        color: #333;
    }
    .btn {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 0.7rem;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        width: 100%;
        font-size: 1rem;
        transition: background 0.3s ease-in-out;
    }
    .btn:hover {
        background: linear-gradient(135deg, #764ba2, #667eea);
    }
    </style>
""", unsafe_allow_html=True)

# Tabs for Login / Register
tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">Login</div>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login", key="login", help="Sign in with Firebase"):
        # TODO: Call your Firebase sign-in logic here
        st.success(f"Logged in as {email}")

    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">Register</div>', unsafe_allow_html=True)

    new_email = st.text_input("Email", key="reg_email")
    new_password = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Register", key="register", help="Create new Firebase account"):
        # TODO: Call your Firebase register logic here
        st.success(f"Account created for {new_email}")

    st.markdown('</div>', unsafe_allow_html=True)
