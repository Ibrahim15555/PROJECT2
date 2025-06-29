import re

def clean_text(text):
    """
    Lowercase, remove punctuation, and split into tokens.
    """
    text = text.lower()
    text = re.sub(r"[^a-z\s]", '', text)
    tokens = text.split()
    return tokens


positive_words = {
    'happy', 'joy', 'love', 'excellent', 'awesome', 'fantastic', 'wonderful',
    'amazing', 'great', 'superb', 'perfect', 'delight', 'pleasure', 'brilliant',
    'outstanding', 'fabulous', 'terrific', 'smiling', 'cheerful', 'ecstatic'
}

negative_words = {
    'sad', 'angry', 'hate', 'terrible', 'awful', 'horrible', 'bad',
    'worst', 'dislike', 'upset', 'depressed', 'miserable', 'annoying',
    'disappointing', 'frustrating', 'painful', 'tragic', 'unhappy', 'gloomy'
}


print("Positive Lexicon:")
print(positive_words)
print("\nNegative Lexicon:")
print(negative_words)


print("\nEnter sentences to analyze sentiment (type 'exit' to quit):")
while True:
    text = input('> ').strip()
    if text.lower() in ('exit', 'quit'):
        print("Goodbye!")
        break

    tokens = clean_text(text)
    pos_count = sum(1 for t in tokens if t in positive_words)
    neg_count = sum(1 for t in tokens if t in negative_words)
    total = len(tokens)

  
    score = pos_count - neg_count

   
    if score > 0:
        sentiment = 'Positive'
    elif score < 0:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

  
    print(f"Tokens: {tokens}")
    print(f"+ matches: {pos_count}, - matches: {neg_count}")
    print(f"Score: {score:.3f} => {sentiment}\n")

# 5. Reflection:
# Strengths: This approach is simple to implement and fast to execute, making it good for basic sentiment analysis.
# Limitations: It lacks context understanding (like sarcasm or negations) and depends heavily on the lexicon quality.
# The approach also doesn't account for word intensity or phrases that change meaning when combined.