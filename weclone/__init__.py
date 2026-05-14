# WeClone - A tool for cloning your WeChat persona using LLMs
# Fork of xming521/WeClone

__version__ = "0.1.0"
__author__ = "WeClone Contributors"
__description__ = "Clone your digital persona from WeChat chat history using LLMs"

# Personal fork notes:
# - Using this for experimenting with local LLMs (llama.cpp / Ollama)
# - Main upstream: https://github.com/xming521/WeClone
# - Tested with: llama3.2:3b, mistral:7b, gemma3:4b via Ollama
# - Default Ollama base URL: http://localhost:11434
# - Switched default model to mistral:7b for better response quality

# Default backend config for local Ollama usage
DEFAULT_MODEL = "mistral:7b"
DEFAULT_API_BASE = "http://localhost:11434/v1"
DEFAULT_TEMPERATURE = 0.7  # slightly lower than upstream default for more consistent persona output
