from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    # Application
    app_name: str = "Agentic Incident Intelligence and Resolution System"
    app_env: str = "development"

    # LLM
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.5-flash-lite"

    # Embeddings
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    # Vector Database
    pinecone_api_key: str = ""
    pinecone_index_name: str = "incident-intelligence-kb"
    pinecone_namespace: str = "incident-kb"

    # Web Search
    tavily_api_key: str = ""

    # Retrieval
    top_k: int = 5
    max_retries: int = 1

    admin_api_key: str = "admin-password"

    # Application data
    knowledge_base_dir: str = str(BASE_DIR / "data" / "sample_kb")

    model_config = SettingsConfigDict(env_file=str(BASE_DIR / ".env"), extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
