# AI Text-to-SQL Agent 🤖📊

This is an intelligent AI Data Analyst agent built to bridge the gap between natural language and databases. 

## 🌟 Key Features
- **Natural Language to SQL**: Converts conversational user queries into exact PostgreSQL commands.
- **Clarification Engine**: Features a unique two-pass architecture. If a user's question is ambiguous, the AI detects it and asks for context before generating code, ensuring 100% accurate queries.
- **Structured Outputs**: Uses Pydantic to enforce strict JSON schemas for all AI responses.

## 🛠️ Tech Stack
- **Language**: Python
- **Database**: PostgreSQL
- **AI Model**: Google Gemini 3.0 Flash API
- **Libraries**: Pydantic, Psycopg2
