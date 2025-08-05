MODELS = {
    "gpt-4o-mini": {
        "model_name": "gpt-4o-mini",
        "max_input_tokens": 128000,
        "max_output_tokens": 16384,
        "provider": "openapi",
        "batch_support": True
    },
    "gpt-4o": {
        "model_name": "gpt-4o",
        "max_input_tokens": 128000,
        "max_output_tokens": 16384,
        "provider": "openapi",
        "batch_support": False
    },
    "gpt-4.1-nano": {
        "model_name": "gpt-4.1-nano",
        "max_input_tokens": 1047576,
        "max_output_tokens": 32768,
        "provider": "openapi",
        "batch_support": True
    },
    "o4-mini": {
        "model_name": "o4-mini",
        "max_input_tokens": 200000,
        "max_output_tokens": 100000,
        "provider": "openapi",
        "batch_support": True
    },
    "claude-sonnet-4": {
        "model_name": "claude-sonnet-4-20250514",
        "max_input_tokens": 200000,
        "max_output_tokens": 64000,
        "provider": "ANTHROPIC",
        "batch_support": True
    }
}