# News Article Summarizer with Local Llama 3
![Capture](https://github.com/user-attachments/assets/6f08c7dc-cffd-456f-8db6-826dd2430f33)
![Capture2](https://github.com/user-attachments/assets/2fb66079-62f0-44ff-8c8d-178d2f99e61d)

Table of Contents
Overview

Features

Technical Stack

Generative AI & Agentic AI Concepts

Getting Started

Prerequisites

Installation

Running the Application

Usage

Project Structure

Future Enhancements

Contributing

License

Contact

Overview
In today's fast-paced world, staying updated with news can be time-consuming. This project addresses that challenge by providing a News Article Summarizer application that leverages the power of Large Language Models (LLMs) to condense lengthy articles into concise summaries.

A key differentiator of this project is its commitment to local LLM inference. Instead of relying on external API calls to models like OpenAI's GPT, this application runs a state-of-the-art Meta Llama 3 8B Instruct model directly on your local machine, showcasing the capabilities of privacy-preserving and cost-effective AI solutions.

This project goes beyond simple summarization, exploring foundational concepts in Generative AI and demonstrating early principles of Agentic AI through its multi-step automated workflow.

Features
Article Scraping: Extracts clean title and text content from various online news article URLs.

Local LLM Inference: Summarizes articles using the Meta Llama 3 8B Instruct model, running entirely on your local CPU (with optional GPU acceleration).

Multiple Summary Formats: Generate concise paragraph summaries or detailed bulleted lists.

Multilingual Summarization: Support for generating summaries in English and French.

Intuitive Web Interface: A user-friendly front-end built with Streamlit for easy URL input and summary display.

Modular Codebase: Clean separation of concerns with dedicated modules for article extraction and application logic.

Technical Stack
Python 3.13.5: The core programming language.

Streamlit: For building the interactive web user interface.

Meta-Llama-3-8B-Instruct.Q4_0.gguf: The large language model (LLM) used for summarization, an 8-billion parameter instruction-tuned model by Meta, quantized to 4-bit for efficient local execution.

llama-cpp-python: Python bindings for llama.cpp, enabling efficient CPU (and optionally GPU) inference of GGUF models.

LangChain: A framework for developing applications powered by LLMs. Used here for prompt templating and integrating with llama-cpp-python.

langchain-core

langchain-community

newspaper3k: A Python library for article scraping, content extraction, and curation. (Specifically tested with version 0.2.8).

lxml_html_clean: A dependency required by newspaper3k for HTML cleaning.

requests: For making HTTP requests to fetch article content.

python-dotenv: For loading environment variables (though not strictly necessary for this local LLM setup, it's good practice for API keys in other projects).

Generative AI & Agentic AI Concepts
This project serves as a practical demonstration of several key AI concepts:

Generative AI: At its heart, the application leverages the generative capabilities of the Meta Llama 3 LLM. Given an article's content and a specific instruction (e.g., "summarize this," "make a bulleted list"), the LLM generates new, coherent, and contextually relevant text as output. This showcases how LLMs can transform raw information into structured, digestible insights.

Agentic AI (Foundational): While simple, this project embodies the initial principles of Agentic AI. An AI agent is designed to achieve a goal by autonomously executing a series of steps, often involving external tools and planning. In this application:

The user provides a goal (summarize an article at a given URL).

The system acts as a basic agent by:

Tool Usage: Invoking a web scraping tool (newspaper3k + requests) to gather information from the internet.

Processing: Feeding the gathered information into the LLM.

Action: Generating the desired summary.
This multi-step, autonomous process, driven by a user's request, is a fundamental characteristic of more complex agentic systems. It demonstrates how AI can perform actions beyond just generating text directly from a simple prompt.

Getting Started
Follow these steps to set up and run the News Article Summarizer on your local machine.

Prerequisites
Python 3.13.5 (or compatible 3.x version)

git (for cloning the repository)

Sufficient RAM (16 GB recommended for Meta Llama 3 8B Q4_0)

A C++ compiler (like Visual Studio Build Tools on Windows, or build-essential on Linux) for llama-cpp-python installation.

Installation
Clone the repository:

Bash

git clone https://github.com/Suyashspidy/News-Summarizer-with-Local-LLama.git
cd News-Summarizer-with-Local-LLama
Create and activate a virtual environment:

Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
Install the required Python packages:

Bash

pip install streamlit python-dotenv requests "newspaper3k==0.2.8" llama-cpp-python langchain langchain-core langchain-community lxml_html_clean
Note on llama-cpp-python: Installation can sometimes be complex if you need GPU support. For CPU-only, it's generally straightforward but requires a C++ compiler. Refer to the llama-cpp-python GitHub page for detailed installation instructions if you encounter issues, especially for GPU acceleration.

Download the Meta Llama 3 Model:
You need to download the Meta-Llama-3-8B-Instruct.Q4_0.gguf model file. You can usually find this on Hugging Face (e.g., search for "Llama 3 8B Instruct GGUF Q4_0").

Create a directory named models in your project root:

Bash

mkdir models
Place the downloaded Meta-Llama-3-8B-Instruct.Q4_0.gguf file inside the models directory.
Your project structure should look like this:

News-Summarizer-with-Local-LLama/
├── app.py
├── summarizer.py
├── .env  (can be empty for this project)
└── models/
    └── Meta-Llama-3-8B-Instruct.Q4_0.gguf
Running the Application
Ensure your virtual environment is active.

Run the Streamlit application:

Bash

streamlit run app.py
This command will open the application in your default web browser (usually http://localhost:8501).

Usage
Once the Streamlit app loads in your browser, you will see a text input field for the News Article URL.

Enter the full URL of the news article you wish to summarize.

Select your desired Summary Type from the dropdown:

Concise Summary (paragraph format)

Bulleted List (bullet points)

Bulleted List (French) (bullet points in French)

Click the "Summarize Article" button.

The application will scrape the article and then generate the summary. Please be patient, as the initial loading of the LLM and the summarization process can take some time, especially on CPU-only setups.

Project Structure
.
├── app.py                  # Main Streamlit application file
├── summarizer.py           # Module for article extraction logic
├── .env                    # Environment variables (can be empty)
└── models/                 # Directory to store the GGUF LLM model
    └── Meta-Llama-3-8B-Instruct.Q4_0.gguf
├── README.md               # This README file
├── requirements.txt        # (Optional: good practice to add dependencies here)
└── venv/                   # Python virtual environment
Future Enhancements
Batch summarization: Allow users to input multiple URLs at once.

Customizable LLM parameters: Add UI elements to adjust temperature, max_tokens, etc.

Persistence: Save generated summaries.

Error handling for scraping: More robust error messages for unsupported websites.

GPU offloading configuration: Provide a clearer way to configure n_gpu_layers in the UI for users with compatible GPUs.

Support for other local LLMs: Make it easier to swap in different GGUF models.

Contributing
Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
Suyash Saxena
[Your LinkedIn Profile (https://www.linkedin.com/in/suyashsaxena1/)]
