from aleph_alpha_client import Client
from semantic_text_splitter import HuggingFaceTextSplitter
import os 

TOKEN = os.getenv("AA_TOKEN")

tokenizer = Client(token=TOKEN).tokenizer("luminous-base")
text_splitter =  HuggingFaceTextSplitter(tokenizer)

chunks = text_splitter.chunks("document text", 400)
# or if you want a range
chunks = text_splitter.chunks("document text", (200, 1000))

print(chunks)