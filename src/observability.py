"""Langfuse client setup.

Import this module (or at least call `load_dotenv()` yourself) before
importing any LLM SDK client, e.g. `from openai import OpenAI` — Langfuse
needs to patch those clients at import time, and it needs the
LANGFUSE_* env vars loaded before `get_client()` builds the singleton.
"""

from dotenv import load_dotenv

load_dotenv()

from langfuse import get_client  # noqa: E402 (must follow load_dotenv())

langfuse = get_client()


def shutdown() -> None:
    """Flush any pending traces. Call before process exit in short-lived scripts."""
    langfuse.flush()
