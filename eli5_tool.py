# ELI5 Tool
# Python 3.x
# This requires openai package. Install via: pip install openai

import openai

# 1. Set your OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"  # replace with your key

def eli5(text):
    """
    Rewrites a complex paragraph into a child-friendly ELI5 explanation.
    """
    prompt = f"Explain this like I'm five years old:\n\n{text}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",  # or gpt-3.5-turbo if using chat API
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    
    return response.choices[0].text.strip()


# 2. Input your complex paragraph here
complex_paragraph = """
Quantum entanglement is a physical phenomenon that occurs when pairs or groups of particles are generated, interact, or share spatial proximity in such a way that the quantum state of each particle cannot be described independently of the others, even when the particles are separated by a large distance.
"""

# 3. Get ELI5 version
simple_text = eli5(complex_paragraph)
print("=== ELI5 Version ===")
print(simple_text)
