# Security & API Key Setup

## ⚠️ IMPORTANT: API Key Security

**NEVER commit API keys to git or share them publicly!**

## Setup Instructions

### 1. Create `.env` file

Copy the example file and add your actual key:

```bash
cp .env.example .env
```

### 2. Edit `.env` file

Open `.env` in a text editor and replace `your-api-key-here` with your actual OpenAI API key:

```
OPENAI_API_KEY=sk-proj-YOUR-ACTUAL-KEY-HERE
```

### 3. Load environment variables

**Option A: In Jupyter Notebook**

```python
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Verify it's loaded
api_key = os.environ.get('OPENAI_API_KEY')
print(f"API key loaded: {api_key[:10]}..." if api_key else "Not found")
```

**Option B: Terminal/Shell**

```bash
# Linux/Mac
export $(cat .env | xargs)

# Or manually
export OPENAI_API_KEY='your-key-here'
```

## Verify `.env` is Ignored

The `.env` file should **never** appear in git:

```bash
git status
# Should NOT show .env file
```

If `.env` appears, it means `.gitignore` is not working properly.

## What to Do If You Exposed Your Key

1. **Immediately revoke** the exposed key at https://platform.openai.com/api-keys
2. **Generate a new key**
3. **Update your `.env` file** with the new key
4. **Check git history** - if the key was committed, the repository may need to be cleaned

## Additional Security

- Install `python-dotenv` to load `.env` files automatically:
  ```bash
  pip install python-dotenv
  ```

- Add to `requirements.txt`:
  ```
  python-dotenv
  ```

- Never log or print full API keys
- Use environment variables in production
- Consider using secret management tools (AWS Secrets Manager, Azure Key Vault, etc.) for production
