import os
from dotenv import load_dotenv
from pydantic import BaseSettings

# Load environment variables
load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    
    # API Keys
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    FIGMA_ACCESS_TOKEN: str = os.getenv("FIGMA_ACCESS_TOKEN", "")
    
    # Server Settings
    PORT: int = int(os.getenv("PORT", "8080"))
    HOST: str = os.getenv("HOST", "localhost")
    
    # Model Settings
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    
    # Analysis Settings
    MIN_FINDINGS_PER_AGENT: int = 3
    CONFIDENCE_THRESHOLD: int = 7
    
    # Report Settings
    ENABLE_ROI_CALCULATIONS: bool = True
    ENABLE_IMPLEMENTATION_TIMELINE: bool = True
    ENABLE_BEFORE_AFTER: bool = True
    
    # Slack settings
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN")
    SLACK_APP_TOKEN: str = os.getenv("SLACK_APP_TOKEN")
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Create settings instance
settings = Settings()

def validate_settings():
    """Validate required settings."""
    if not settings.OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is required")
    
    return settings 