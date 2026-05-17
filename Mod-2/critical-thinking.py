import re
from collections import Counter
import pandas as pd

# 1. Read speech file
with open("sotu.txt", "r", encoding="utf-8") as file:
    text = file.read()

# 2. Character count
character_count = len(text)

# 3. Word extraction
words = re.findall(r'\b\w+\b', text)
word_count = len(words)

# 4. Average word length
avg_word_length = sum(len(word) for word in words) / word_count

# 5. Sentence extraction
sentences = re.split(r'[.!?]+', text)
sentences = [s for s in sentences if s.strip()]
avg_sentence_length = word_count / len(sentences)

# 6. Word frequency distribution
word_freq = Counter(word.lower() for word in words)
top_words = word_freq.most_common(20)

# 7. Top ten longest words
longest_words = sorted(set(words), key=len, reverse=True)[:10]

# 8. Display results in table format
summary_table = pd.DataFrame({
    "Metric": [
        "Word Count",
        "Character Count",
        "Average Word Length",
        "Average Sentence Length"
    ],
    "Value": [
        word_count,
        character_count,
        round(avg_word_length, 2),
        round(avg_sentence_length, 2)
    ]
})

print("\n===== SUMMARY =====")
print(summary_table.to_string(index=False))

print("\n===== TOP 20 WORD FREQUENCIES =====")
print(pd.DataFrame(top_words, columns=["Word","Frequency"]).to_string(index=False))

print("\n===== TOP 10 LONGEST WORDS =====")
print(longest_words)