MODELS = [
    {
        "name": "gpt-4o-mini",
        "max_input_tokens": 128000,
        "max_output_tokens": 16384,
        "provider": "openai",
        "batch_support": True,
    },
    {
        "name": "gpt-4o",
        "max_input_tokens": 128000,
        "max_output_tokens": 16384,
        "provider": "openai",
        "batch_support": False,
    },
    {
        "name": "gpt-4.1-nano",
        "max_input_tokens": 1047576,
        "max_output_tokens": 32768,
        "provider": "openai",
        "batch_support": True,
    },
    {
        "name": "o4-mini",
        "max_input_tokens": 200000,
        "max_output_tokens": 100000,
        "provider": "openai",
        "batch_support": True,
    },
    {
        "name": "claude-sonnet-4-20250514",
        "max_input_tokens": 200000,
        "max_output_tokens": 64000,
        "provider": "anthropic",
        "batch_support": True,
    },
]
