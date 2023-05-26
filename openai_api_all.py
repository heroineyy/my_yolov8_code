import os
import openai
OPENAI_API_KEY="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"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
