from skllm import DynamicFewShotGPTClassifier
import os

key = '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'
os.environ['SKLLM_CONFIG_OPENAI_KEY'] = key

X = [
    "I love reading science fiction novels, they transport me to other worlds.",
    "A good mystery novel keeps me guessing until the very end.",
    "Historical novels give me a sense of different times and places.",
    "I love watching science fiction movies, they transport me to other galaxies.",
    "A good mystery movie keeps me on the edge of my seat.",
    "Historical movies offer a glimpse into the past.",
]

y = ["books", "books", "books", "movies", "movies", "movies"]

query = "I have fallen deeply in love with this sci-fi book; its unique blend of science and fiction has me spellbound."

clf = DynamicFewShotGPTClassifier(n_examples=1).fit(X, y)

prompt = clf._get_prompt(query)
print(prompt)