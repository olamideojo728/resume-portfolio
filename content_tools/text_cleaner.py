import re

def clean_text(text):
    # 1. Remove HTML tags
    text = re.sub(r"<.*?>", "", text)

    # 2. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 3. Remove special characters (keep letters, numbers, spaces)
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)

    # 4. Remove numbers (optional — comment out if you want to keep them)
    text = re.sub(r"\d+", "", text)

    # 5. Collapse multiple spaces into one
    text = re.sub(r"\s+", " ", text)

    # 6. Trim leading/trailing spaces
    return text.strip()

if __name__ == "__main__":
    sample = "<p>This is   a   test with numbers 123 and a URL: https://olamidefiction.com !!!</p>"
    print("Original:", sample)
    print("Cleaned:", clean_text(sample))
