import sys
import streamlit as st
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Add the project root to Python's module search path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.rag_chain import answer_question
from app.initialize_db import initialize_knowledge_base


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Northstar | Knowledge Hub",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# INITIALIZE KNOWLEDGE BASE
# ==========================================

with st.spinner("Initializing enterprise knowledge base..."):
    collection = initialize_knowledge_base()

# ==========================================
# DARK ENTERPRISE THEME
# ==========================================

st.markdown("""
<style>

/* Main background and default text */
.stApp {
    background: #0B1118;
    color: #E5EAF0;
}

html, body, [class*="css"] {
    color: #E5EAF0;
}

[data-testid="stAppViewContainer"] {
    background: #0B1118;
}

[data-testid="stHeader"] {
    background: rgba(11, 17, 24, 0.95);
}

/* Hide default Streamlit branding */
#MainMenu, footer {
    visibility: hidden;
}

/* Main content */
.block-container {
    max-width: 1150px;
    padding-top: 2.5rem;
    padding-bottom: 10rem;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #101A24;
    border-right: 1px solid #263442;
}

[data-testid="stSidebar"] > div:first-child {
    background: #101A24;
}

[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div {
    color: #D5DFE8;
}

/* Brand */
.brand {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0 22px;
}

.brand-logo {
    height: 46px;
    width: 46px;
    border-radius: 13px;
    background: #153C3A;
    color: #5EEAD4;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 25px;
    font-weight: 800;
}

.brand-name {
    font-size: 19px;
    font-weight: 800;
    color: #F8FAFC;
    letter-spacing: 1.5px;
}

.brand-subtitle {
    font-size: 10px;
    color: #94A3B8;
    letter-spacing: 1.5px;
}

/* Headings */
.eyebrow {
    display: block;
    color: #5EEAD4;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 2px;
    line-height: 1.8;
    padding: 4px 0;
    margin-bottom: 8px;
    overflow: visible;
}

.main-heading {
    color: #F8FAFC;
    font-size: clamp(30px, 4vw, 43px);
    font-weight: 750;
    letter-spacing: -1.5px;
    margin: 10px 0;
}

.sub-heading {
    color: #A8B5C2;
    font-size: 15px;
    line-height: 1.7;
}

/* Dashboard cards */
.info-card {
    background: #15212D;
    border: 1px solid #293B4A;
    border-radius: 14px;
    padding: 19px;
    min-height: 105px;
}

.info-label {
    color: #9AAABA;
    font-size: 11px;
    letter-spacing: 1px;
}

.info-value {
    color: #F8FAFC;
    font-size: 22px;
    font-weight: 750;
    margin-top: 9px;
}

/* All buttons */
.stButton > button {
    background: #172431 !important;
    color: #E5EDF5 !important;
    border: 1px solid #344555 !important;
    border-radius: 11px !important;
    min-height: 45px;
    font-weight: 600;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: #203B43 !important;
    border-color: #36B9A7 !important;
    color: #FFFFFF !important;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: #15212D;
    border: 1px solid #293B4A;
    border-radius: 15px;
    padding: 18px;
    margin-bottom: 15px;
}

[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span {
    color: #E5EDF5 !important;
    line-height: 1.7;
}

/* Chat input */
[data-testid="stChatInput"] {
    background: #101A24 !important;
    border: 1px solid #344555 !important;
    border-radius: 15px !important;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.25);
}

[data-testid="stChatInput"]:focus-within {
    border-color: #36B9A7 !important;
    box-shadow: 0 0 0 1px #36B9A7;
}

[data-testid="stChatInput"] textarea {
    color: #F8FAFC !important;
    background: transparent !important;
    caret-color: #5EEAD4;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #91A2B2 !important;
    opacity: 1;
}

[data-testid="stChatInput"] button {
    color: #5EEAD4 !important;
}

/* Text inputs and expanders */
input, textarea {
    color: #F8FAFC !important;
}

[data-testid="stExpander"] {
    background: #15212D;
    border: 1px solid #344555;
    border-radius: 12px;
}

[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary span {
    color: #E5EDF5 !important;
}

/* Source references */
.source-card {
    background: #122C2C;
    border: 1px solid #28534F;
    color: #B9E9DF;
    border-radius: 9px;
    padding: 12px;
    margin: 8px 0;
    font-size: 13px;
}

/* Sidebar separators */
[data-testid="stSidebar"] hr {
    border-color: #2A3947;
}

/* Footer */
.app-footer {
    color: #718394;
    text-align: center;
    font-size: 11px;
    padding-top: 40px;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .main-heading {
        font-size: 29px;
    }
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_question" not in st.session_state:
    st.session_state.pending_question = None


# ==========================================
# DOCUMENTS
# ==========================================

data_folder = Path("data")

pdf_files = (
    sorted(data_folder.glob("*.pdf"))
    if data_folder.exists()
    else []
)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div class="brand">
        <div class="brand-logo">N</div>
        <div>
            <div class="brand-name">NORTHSTAR</div>
            <div class="brand-subtitle">ENTERPRISE KNOWLEDGE HUB</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    st.caption("WORKSPACE")

    st.markdown("**🧭 Knowledge Assistant**")

    st.divider()

    st.caption("KNOWLEDGE BASE")

    st.write(f"📄  {len(pdf_files)} documents indexed")

    with st.expander("View documents"):
        for pdf in pdf_files:
            st.write(f"📄 {pdf.name}")

    st.divider()

    if st.button("＋  New conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_question = None
        st.rerun()

    st.divider()

    st.caption("SYSTEM STATUS")

    st.markdown("🟢  Assistant ready")

    st.markdown("""
    <div style="
        margin-top: 65px;
        color: #8194A5;
        font-size: 11px;
        line-height: 1.9;
    ">
        NORTHSTAR KNOWLEDGE HUB<br>
        Powered by RAG technology<br>
        Fictional demonstration environment
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MAIN HEADER
# ==========================================

st.markdown(
    '<div class="eyebrow">EMPLOYEE KNOWLEDGE PORTAL</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-heading">Your knowledge, connected.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-heading">'
    'Find accurate answers from company documents '
    'with AI-powered semantic search.'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# ==========================================
# DASHBOARD CARDS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="info-card">
        <div class="info-label">DOCUMENTS</div>
        <div class="info-value">{len(pdf_files):02d}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">SEARCH ENGINE</div>
        <div class="info-value">Semantic Search</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-label">AI ENGINE</div>
        <div class="info-value">Gemini AI</div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# ==========================================
# SUGGESTED QUESTIONS
# ==========================================

if not st.session_state.messages:

    st.markdown("### Explore your knowledge base")

    st.markdown(
        '<div class="sub-heading">'
        'Select a question or type your own below.'
        '</div>',
        unsafe_allow_html=True
    )

    suggestions = [
        "When will I receive my monthly salary?",
        "What deductions apply to the sample salary?",
        "What documents should I bring when joining?",
        "What is the leave application process?"
    ]

    col1, col2 = st.columns(2)

    for index, suggestion in enumerate(suggestions):

        target_col = col1 if index % 2 == 0 else col2

        with target_col:

            if st.button(
                suggestion,
                key=f"suggestion_{index}",
                use_container_width=True
            ):
                st.session_state.pending_question = suggestion
                st.rerun()


# ==========================================
# CHAT HISTORY
# ==========================================

for message in st.session_state.messages:

    avatar = "👤" if message["role"] == "user" else "🧭"

    with st.chat_message(message["role"], avatar=avatar):

        st.markdown(message["content"])

        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander(
                    f"📚 View sources ({len(sources)})"
                ):

                    for source in sources:

                        st.markdown(
                            f"""
                            <div class="source-card">
                                📄 {source["file"]}
                                &nbsp; • &nbsp;
                                Page {source["page"]}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


# ==========================================
# QUESTION INPUT
# ==========================================

typed_question = st.chat_input(
    "Ask a question about employee policies, salary or documents..."
)

question = (
    st.session_state.pending_question
    or typed_question
)

if question:

    st.session_state.pending_question = None

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(question)

    with st.chat_message("assistant", avatar="🧭"):

        with st.spinner("Searching company knowledge base..."):

            try:

                result = answer_question(question)

                answer = result["answer"]
                sources = result["sources"]

                st.markdown(answer)

                if sources:

                    with st.expander(
                        f"📚 View sources ({len(sources)})",
                        expanded=True
                    ):

                        for source in sources:

                            st.markdown(
                                f"""
                                <div class="source-card">
                                    📄 {source["file"]}
                                    &nbsp; • &nbsp;
                                    Page {source["page"]}
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "sources": sources
                })

            except Exception as error:

                error_message = (
                    f"Unable to process your question. Please try again. Error:{error}"
                )

                st.error(error_message)
                st.caption(str(error))

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message,
                    "sources": []
                })


# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="app-footer">
    NORTHSTAR KNOWLEDGE HUB
    &nbsp; • &nbsp;
    AI-POWERED DOCUMENT INTELLIGENCE
</div>
""", unsafe_allow_html=True)