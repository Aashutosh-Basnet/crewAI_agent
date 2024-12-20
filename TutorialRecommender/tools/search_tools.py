import json
import os

import requests
from langchain.tools import tool


class SearchTools():
    @tool("search the internet")
    def search_internet(query):
        """Searches the internet about a given topic and returns relevant results."""
        
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        
        try:
            payload = json.dumps({"q": query})
            headers = {
                'X-API-KEY': os.environ['SERPER_API_KEY'],
                'content-type': 'application/json',
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            response.raise_for_status()  # Raise exception for bad status codes
            
            data = response.json()
            if 'organic' not in data:
                return "No results found or API error occurred."
                
            results = data['organic']
            formatted_results = []
            
            for result in results[:top_result_to_return]:
                try:
                    formatted_results.append('\n'.join([
                        f"Title: {result['title']}", 
                        f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", 
                        "\n-----------------"
                    ]))
                except KeyError as e:
                    continue
                    
            return '\n'.join(formatted_results) if formatted_results else "No valid results found."
            
        except requests.RequestException as e:
            return f"Error accessing search API: {str(e)}"
        except KeyError as e:
            return f"Missing API key: {str(e)}"
                    