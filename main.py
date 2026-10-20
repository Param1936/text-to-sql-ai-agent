import os
from pydantic import BaseModel
from google import genai
from google.genai import types
from dotenv import load_dotenv

# .env file se API key load karna
load_dotenv()
client = genai.Client(api_key="ENTER_YOUR_API_KEY_HERE")



class ClarificationResponse(BaseModel):
    is_clear: bool
    clarification_question: str | None
    
class SQLGenerationResponse(BaseModel):
    sql_query: str

def run_agent():
    print("🤖 Welcome to AI Data Analyst!")
    user_query = input("\nKya janna hai aapko? (Example: 'Who is best customer?'): ")
    
    # AI se poochna ki sawal clear hai ya nahi
    prompt = f"Schema: customers(id, name), orders(id, customer_id, total_amount). User asked: '{user_query}'. Is this ambiguous? If yes, set is_clear to false and ask a question. If clear, set to true."
    
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=ClarificationResponse, temperature=0.0)
    )
    clarification = ClarificationResponse.model_validate_json(response.text)
    
    context = user_query
    if not clarification.is_clear:
        print(f"\n[AI Doubt]: {clarification.clarification_question}")
        ans = input("Your answer: ")
        context += f" Clarification: {ans}"
        
    print("\n✅ SQL Generate ho raha hai...")
    # Ab final SQL banana
    sql_prompt = f"Schema: customers(id, name), orders(id, customer_id, amount). Write exact Postgres SQL query for: {context}. ONLY output raw SQL."
    
    sql_resp = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=sql_prompt,
        config=types.GenerateContentConfig(response_mime_type="application/json", response_schema=SQLGenerationResponse, temperature=0.0)
    )
    final_sql = SQLGenerationResponse.model_validate_json(sql_resp.text).sql_query
    print(f"Generated SQL: {final_sql}")

if __name__ == "__main__":
    run_agent()
