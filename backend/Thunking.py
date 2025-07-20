from typing import List
 
def chunk_text(text: str, max_length: int = 512) -> List[str]:
    # Simple chunking by sentences or words (expand as needed)
    words = text.split()
    return [' '.join(words[i:i+max_length]) for i in range(0, len(words), max_length)] 