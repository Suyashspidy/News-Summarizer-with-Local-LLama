import streamlit as st
# import requests # No longer needed directly in app.py for scraping
# from newspaper import Article # No longer needed directly in app.py for scraping
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate

# Import your custom summarizer functions
from summarizer import extract_article # <--- IMPORTANT CHANGE HERE

# Load environment variables
load_dotenv()

# --- Configuration ---
MODEL_PATH = "models/Meta-Llama-3-8B-Instruct.Q4_0.gguf"

# --- Streamlit UI Setup ---
st.set_page_config(page_title="News Article Summarizer", layout="wide")
st.title("📰 News Article Summarizer")
st.markdown("Enter a news article URL to get a concise summary.")

# --- Local LLM Initialization ---
try:
    llm = LlamaCpp(
        model_path=MODEL_PATH,
        temperature=0.1,
        max_tokens=500,
        n_ctx=8192,
        f16_kv=True,
        verbose=False,
        n_gpu_layers=0,
        streaming=True,
    )
except Exception as e:
    st.error(f"Error loading local LLM model. Make sure '{MODEL_PATH}' exists and `llama-cpp-python` is correctly installed with necessary build tools (e.g., C++ compiler). Error: {e}")
    st.stop()

# --- Functions (only generate_summary remains here) ---
# The scrape_article function is now in summarizer.py

def generate_summary(title, text, summary_type="default", language="english"):
    if not title or not text:
        return "Cannot summarize, missing article title or text."

    if summary_type == "bullet_points":
        template_instructions = f"summarizes online articles into bulleted lists in {language}."
        summary_request = "Now, provide a summarized version of the article in a bulleted list format."
    elif summary_type == "french_bullet_points":
        template_instructions = "summarizes online articles into bulleted lists in French."
        summary_request = "Now, provide a summarized version of the article in a bulleted list format, in French."
        language = "French"
    else: # default
        template_instructions = f"summarizes online articles in {language}."
        summary_request = "Write a concise summary of the previous article."

    template = f"""You are a very good assistant that {template_instructions}

Here's the article you want to summarize.

==================
Title: {{article_title}}

{{article_text}}
==================

{summary_request}
"""
    
    prompt = PromptTemplate(
        input_variables=["article_title", "article_text"],
        template=template,
    )
    
    formatted_prompt = prompt.format(article_title=title, article_text=text)

    try:
        with st.spinner(f"Generating {language} summary ({summary_type.replace('_', ' ')})..."):
            summary_content = ""
            for chunk in llm.stream(formatted_prompt):
                summary_content += chunk
            return summary_content
    except Exception as e:
        st.error(f"Error generating summary: {e}. The model might have encountered an issue or the context window is too small.")
        return "Summary generation failed."

# --- Streamlit App Logic ---

article_url = st.text_input("Enter News Article URL:")

summary_option = st.selectbox(
    "Select Summary Type:",
    ("Concise Summary", "Bulleted List", "Bulleted List (French)")
)

if st.button("Summarize Article"):
    if article_url:
        with st.spinner("Scraping article..."):
            # Call the function from your summarizer.py
            title, text = extract_article(article_url) 
        
        if title and text:
            st.subheader("Original Article")
            st.write(f"**Title:** {title}")
            st.markdown(f"**Text Preview:** {text[:1000]}...") 
            
            st.subheader("Generated Summary")
            
            if summary_option == "Concise Summary":
                summary = generate_summary(title, text, "default")
            elif summary_option == "Bulleted List":
                summary = generate_summary(title, text, "bullet_points")
            elif summary_option == "Bulleted List (French)":
                summary = generate_summary(title, text, "french_bullet_points")
            
            st.write(summary)
    else:
        st.warning("Please enter a valid article URL.")

st.markdown("---")
st.markdown("Project by: Suyash Saxena")