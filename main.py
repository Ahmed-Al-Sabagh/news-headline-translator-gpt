# API KEY ... 
# API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx ... 
# .env
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("API_KEY")

