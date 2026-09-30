import streamlit as st
import requests

st.set_page_config(
    page_title="Ollama AI Chat",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Ollama AI Chat")
st.write("Ask anything to Llama 3.2")

prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Java in simple terms..."
)

if st.button("Generate Response"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=data)

            if response.status_code == 200:
                result = response.json()

                st.subheader("🤖 Ollama Response")
                st.write(result["response"])

            else:
                st.error("Ollama returned an error.")
                st.write(response.text)

        except requests.exceptions.ConnectionError:
            st.error("❌ Ollama is not running!")
            st.info("Start Ollama first and try again.")

        except Exception as e:
            st.error(f"Error: {e}")