from newspaper import Article
import requests # Added requests for proper handling of headers and session

def extract_article(url):
    # Added headers for robustness against website blocking
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    session = requests.Session()
    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status() # Raise an exception for HTTP errors
        
        article = Article(url)
        # Use downloaded HTML directly with newspaper3k
        article.download(input_html=response.text) 
        article.parse()
        
        if not article.title or not article.text:
            # You might want to raise an exception or return (None, None)
            # and handle it in the calling function (app.py)
            print(f"Warning: Could not extract title or text from {url}")
            return None, None
            
        return article.title, article.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching article from {url}: {e}")
        return None, None
    except Exception as e:
        print(f"Error occurred while processing article at {url}: {e}")
        return None, None