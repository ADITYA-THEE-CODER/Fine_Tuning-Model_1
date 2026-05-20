import streamlit as st
from pypdf import PdfReader
from groq import Groq

st.set_page_config(page_title="AI PDF Chatbot", page_icon="📄", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #2b1055, #1f3b73, #000000);
    background-attachment: fixed;
}
.block-container {padding-top: 2rem;}
.title {text-align:center;font-size:42px;font-weight:800;color:#D8C3A5;}
.sub {text-align:center;color:white;margin-bottom:20px;}
.chat-box {padding:12px;border-radius:14px;background:rgba(255,255,255,0.05);margin-bottom:10px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">📄 AI PDF CHATBOT</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Upload your PDF, get summaries, and ask questions.</div>', unsafe_allow_html=True)

# ---------- HELPERS ----------
def extract_pdf_text(file):
    reader = PdfReader(file)
    data = []
    for i, page in enumerate(reader.pages, start=1):
        txt = page.extract_text()
        if txt:
            clean = txt.replace("\n\n", "\n").strip()
            data.append(f"[Page {i}]\n{clean}")
    return "\n\n".join(data)


def ask_groq(client, model, prompt, temperature=0.3):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    return response.choices[0].message.content

# ---------- MAIN ----------
api_key = st.secrets.get("GROQ_API_KEY", None)
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if "history" not in st.session_state:
    st.session_state.history = []

if not api_key:
    st.warning("Add GROQ_API_KEY in Streamlit secrets.")
    st.stop()

# Sidebar small improvements
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.selectbox("Choose Model", ["llama-3.1-8b-instant", "llama-3.3-70b-versatile"])
    temp = st.slider("Creativity", 0.0, 1.0, 0.3, 0.1)

if uploaded_file:
    with st.spinner("Reading PDF..."):
        text = extract_pdf_text(uploaded_file)

    if not text.strip():
        st.error("No readable text found in this PDF.")
        st.stop()

    client = Groq(api_key=api_key)
    short_text = text[:8000]

    st.success("PDF uploaded successfully!")
    st.caption(f"Characters loaded: {len(text):,}")

    option = st.radio("Choose Action", ["Summary", "Ask Question"], horizontal=True)

    if option == "Summary":
        summary_type = st.selectbox(
            "Choose Summary Type",
            ["Detailed Summary", "Short Summary", "Key Points", "Exam Notes"]
        )

        if st.button("Generate Summary", use_container_width=True):
            try:
                with st.spinner("Generating summary..."):
                    instructions = {
                        "Detailed Summary": "Give a detailed and easy-to-understand summary.",
                        "Short Summary": "Give a short simple summary in a few paragraphs.",
                        "Key Points": "Give only key points in bullets.",
                        "Exam Notes": "Create quick exam notes with concepts, definitions and revision points."
                    }
                    prompt = f"{instructions[summary_type]}\n\nPDF Content:\n{short_text}"
                    answer = ask_groq(client, model_name, prompt, temp)
                    st.subheader("📌 Summary Result")
                    st.write(answer)
                    st.download_button("⬇️ Download Summary", answer, file_name="summary.txt")
            except Exception as e:
                st.error("Could not generate summary.")
                st.write(e)

    else:
        question = st.text_input("Ask something from the PDF")
        col1, col2 = st.columns(2)
        ask_btn = col1.button("Get Answer", use_container_width=True)
        clear_btn = col2.button("Clear History", use_container_width=True)

        if clear_btn:
            st.session_state.history = []
            st.rerun()

        if ask_btn and question:
            try:
                with st.spinner("Thinking..."):
                    prompt = f"""
                    Answer using ONLY the PDF content below.
                    If answer is missing, say: I could not find that in the PDF.
                    Keep the answer clear and simple.

                    PDF Content:
                    {short_text}

                    Question: {question}
                    """
                    answer = ask_groq(client, model_name, prompt, temp)
                    st.session_state.history.append((question, answer))
            except Exception as e:
                st.error("Error while getting answer.")
                st.write(e)

        if st.session_state.history:
            st.subheader("💬 Chat History")
            for q, a in reversed(st.session_state.history):
                st.markdown(f'<div class="chat-box"><b>Q:</b> {q}<br><br>{a}</div>', unsafe_allow_html=True)
else:
    st.info("Upload a PDF to begin.")
