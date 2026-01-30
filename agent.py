# Placeholder AI agent for bid analysis
# This module can be extended to use OpenAI, transformers, or other models


def analyze_bid_text(bid_text):
    """Simple heuristic: returns "positive" if text contains confident words, else "neutral". """
    confident_words = ['sure', 'definitely', 'guarantee', 'win', 'best']
    lower = bid_text.lower()
    for w in confident_words:
        if w in lower:
            return 'positive'
    return 'neutral'
