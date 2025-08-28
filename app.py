import streamlit as st
import streamlit.components.v1 as components

def main():
    st.set_page_config(page_title="Visme Form Test", layout="wide")
    st.title("Test Visme Form in Streamlit")

    visme_html = """
    <div class="visme_d"
        data-title="Webinar Registration Form"
        data-url="g7ddqxx0-untitled-project?fullPage=true"
        data-domain="forms"
        data-full-page="true"
        data-min-height="100vh"
        data-form-id="133190">
    </div>

    <script src="https://static-bundles.visme.co/forms/vismeforms-embed.js"></script>
    """

    components.html(visme_html, height=900, scrolling=True)

if __name__ == "__main__":
    main()
