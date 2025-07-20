import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from backend.Recommender import Recommender

st.set_page_config(page_title="MovieGenie: GenAI Movie Recommender", page_icon="🎬", layout="centered")

st.markdown("""
<style>
body {
    background: #18181b;
    color: #f4f4f5;
}
.big-title {
    font-size: 2.5rem;
    font-weight: bold;
    color: #4F8BF9;
    letter-spacing: 1px;
    margin-bottom: 0.5rem;
}
.movie-card {
    background: linear-gradient(135deg, #23232a 80%, #2d2d36 100%);
    color: #fff;
    border-radius: 1.2rem;
    padding: 1.5rem 1.5rem 1.2rem 1.5rem;
    margin-bottom: 2.2rem;
    box-shadow: 0 6px 32px rgba(79,139,249,0.18), 0 1.5px 8px rgba(0,0,0,0.10);
    border: 2px solid #4F8BF9;
    transition: all 0.25s cubic-bezier(.4,2,.6,1), box-shadow 0.13s, border-color 0.13s;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.7rem;
    min-height: 110px;
    max-width: 700px;
}
.movie-card.expanded {
    padding-bottom: 2.2rem;
    box-shadow: 0 12px 48px rgba(79,139,249,0.28), 0 2px 12px rgba(0,0,0,0.13);
    border-color: #fff;
    min-height: 220px;
}
.poster-thumb {
    width: 120px;
    height: 180px;
    object-fit: cover;
    border-radius: 1.2rem 0 0 1.2rem;
    background: #23232a;
    flex-shrink: 0;
    border: 1.5px solid #4F8BF9;
    box-shadow: 0 2px 8px rgba(79,139,249,0.13);
}
.card-content {
    padding: 0.2rem 0.2rem 0.2rem 0.2rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.card-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.2rem;
}
.card-title {
    font-size: 1.4rem;
    font-weight: 900;
    color: #fff;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 8px rgba(79,139,249,0.10);
}
.expand-btn {
    background: none;
    border: none;
    font-size: 1.5rem;
    color: #4F8BF9;
    cursor: pointer;
    outline: none;
    margin-left: 0.5rem;
    transition: color 0.2s;
}
.expand-btn:hover {
    color: #1e40af;
}
.card-details {
    margin-top: 0.7rem;
    font-size: 1.08rem;
    color: #e0e0e6;
    background: #23232a;
    border-radius: 0.7rem;
    padding: 0.7rem 1rem;
    box-shadow: 0 2px 8px rgba(79,139,249,0.10);
    border: 1.5px solid #4F8BF9;
}
.explanation {
    color: #4F8BF9;
    font-style: italic;
    margin-top: 0.5rem;
}
.stButton>button {
    background: linear-gradient(90deg, #4F8BF9 60%, #1e40af 100%);
    color: #fff;
    font-weight: bold;
    border-radius: 2.2rem;
    border: none;
    padding: 0.5rem 1.5rem;
    font-size: 1.2rem;
    box-shadow: 0 2px 12px rgba(79,139,249,0.13);
    transition: background 0.2s, box-shadow 0.2s, transform 0.13s;
    margin-top: 0.7rem;
    margin-bottom: 0.2rem;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1e40af 60%, #4F8BF9 100%);
    box-shadow: 0 4px 24px #4F8BF9, 0 2px 8px rgba(0,0,0,0.10);
    transform: scale(1.07);
}
input, textarea, .stTextInput>div>div>input {
    background: #23232a !important;
    color: #f4f4f5 !important;
    border-radius: 0.5rem !important;
    border: 1px solid #333 !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.10);
    transition: box-shadow 0.2s, border 0.2s, transform 0.2s;
    font-size: 1.1rem;
}
.stTextInput>div>div>input:focus {
    border: 2px solid #4F8BF9 !important;
    box-shadow: 0 4px 24px #4F8BF9, 0 2px 8px rgba(0,0,0,0.10);
    outline: none !important;
    transform: scale(1.03);
    background: #23232a !important;
    color: #fff !important;
    z-index: 10;
    position: relative;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎬 MovieGenie</div>', unsafe_allow_html=True)
st.write("Describe what you feel like watching, and get smart, meaningful recommendations!")

if 'recommender' not in st.session_state:
    st.session_state['recommender'] = Recommender()

user_query = st.text_input("What do you feel like watching?", placeholder="e.g. A slow-paced emotional sci-fi like Interstellar")
if st.button("Recommend") and user_query:
    with st.spinner("Finding the best movies for you..."):
        recommendations = st.session_state['recommender'].recommend(user_query)
        st.session_state['last_recommendations'] = recommendations

if 'last_recommendations' in st.session_state:
    st.subheader("Recommended Movies:")
    recs = st.session_state['last_recommendations']
    if recs and isinstance(recs, list):
        for idx, rec in enumerate(recs):
            if rec is None:
                continue
            if not rec.get('title', '').strip() and not rec.get('explanation', '').strip():
                continue
            if 'expand_states' not in st.session_state:
                st.session_state['expand_states'] = {}
            if idx not in st.session_state['expand_states']:
                st.session_state['expand_states'][idx] = False
            # Now render the card with updated state
            card_class = 'movie-card expanded' if st.session_state['expand_states'][idx] else 'movie-card'
            
            # Create the card HTML without details
            movie_card_html = f"""
            <div class='{card_class}'>
                <div class='card-title-row'>
                    <span class='card-title' style='color:#fff; font-size:1.4rem; font-weight:900;'>{rec.get('title','')}</span>
                </div>
                <div class='explanation'>{rec.get('explanation','')}</div>
            </div>
            """
            
            st.markdown(movie_card_html, unsafe_allow_html=True)
            
            # Render details separately if expanded
            if st.session_state['expand_states'][idx]:
                st.markdown(f"""
                <div class='card-details'>
                    <b>Summary:</b> {rec.get('summary','')}<br>
                    <b>Year:</b> {rec.get('year','')}<br>
                    <b>Genre:</b> {rec.get('genre','')}<br>
                    <b>Director:</b> {rec.get('director','')}<br>
                    <b>Cast:</b> {rec.get('cast','')}<br>
                    <b>Duration:</b> {rec.get('duration','')} min<br>
                    <b>Language:</b> {rec.get('language','')}<br>
                    <b>Country:</b> {rec.get('country','')}<br>
                </div>
                """, unsafe_allow_html=True)
            
            # Place the button after the card HTML, below the explanation
            if st.button(f"{'➖' if st.session_state['expand_states'][idx] else '➕'}", key=f"expand_btn_{idx}"):
                st.session_state['expand_states'][idx] = not st.session_state['expand_states'][idx]
                st.rerun()  # Force rerun to update the display
    else:
        st.markdown("<div class='explanation'>Sorry, no recommendations could be parsed. Please try again or refine your query.</div>", unsafe_allow_html=True)

    followup = st.text_input("Ask a follow-up (e.g. Why did you recommend Inception?)", key="followup")
    if st.button("Ask", key="ask_btn") and followup:
        with st.spinner("Getting explanation..."):
            followup_recs = st.session_state['recommender'].recommend(followup)
            if followup_recs and isinstance(followup_recs, list):
                for rec in followup_recs:
                    st.markdown(f"<div class='explanation'><b>{rec.get('title','')}</b>: {rec.get('explanation','')}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='explanation'>Sorry, no explanation could be parsed.</div>", unsafe_allow_html=True) 