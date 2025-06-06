AI_MODEL_REGISTRY = {
    # OpenAI
    "gpt-4.1": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/chat/completions"
    },
    "gpt-4.1-mini": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/chat/completions"
    },
    "gpt-4o": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/chat/completions"
    },
    "gpt-4o-mini": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/chat/completions"
    },
    "gpt-image-1": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/images/generations"
    },
    "dalle-3": {
        "provider": "openai",
        "endpoint": "https://api.openai.com/v1/images/generations"
    },

    # Anthropic
    "claude-3.5-haiku": {
        "provider": "anthropic",
        "endpoint": "https://api.anthropic.com/v1/messages"
    },
    "claude-3.7-sonnet": {
        "provider": "anthropic",
        "endpoint": "https://api.anthropic.com/v1/messages"
    },

    # Google Gemini
    "gemini-2.5-pro": {
        "provider": "google",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    },
    "gemini-1.5-pro": {
        "provider": "google",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    },
    "gemini-2.0-flash": {
        "provider": "google",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    },
    "gemini-1.5-flash": {
        "provider": "google",
        "endpoint": "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    },

    # DeepSeek
    "deepseek-r1": {
        "provider": "deepseek",
        "endpoint": "https://api.deepseek.com/v1/chat/completions"
    },
    "deepseek-v3": {
        "provider": "deepseek",
        "endpoint": "https://api.deepseek.com/v1/chat/completions"
    },

    # Llama 4
    "llama-4-scout": {
        "provider": "meta",
        "endpoint": "https://api.meta.ai/v1/chat/completions"
    },
    "llama-4-maverick": {
        "provider": "meta",
        "endpoint": "https://api.meta.ai/v1/chat/completions"
    },

    # Amazon Nova
    "nova-micro": {
        "provider": "amazon",
        "endpoint": "https://api.amazonai.com/v1/chat/completions"
    },
    "nova-lite": {
        "provider": "amazon",
        "endpoint": "https://api.amazonai.com/v1/chat/completions"
    },
    "nova-pro": {
        "provider": "amazon",
        "endpoint": "https://api.amazonai.com/v1/chat/completions"
    },
    "nova-canvas": {
        "provider": "amazon",
        "endpoint": "https://api.amazonai.com/v1/images/generations"
    },
    "nova-reel": {
        "provider": "amazon",
        "endpoint": "https://api.amazonai.com/v1/video/generations"
    },

    # Cohere
    "cohere-command-r": {
        "provider": "cohere",
        "endpoint": "https://api.cohere.ai/v1/chat"
    },
    "cohere-command-r-plus": {
        "provider": "cohere",
        "endpoint": "https://api.cohere.ai/v1/chat"
    },

    # Mistral
    "mistral-small": {
        "provider": "mistral",
        "endpoint": "https://api.mistral.ai/v1/chat/completions"
    },
    "mistral-large": {
        "provider": "mistral",
        "endpoint": "https://api.mistral.ai/v1/chat/completions"
    },

    # Ninja Flux
    "flux-schnell": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/flux"
    },
    "flux-1.1-pro": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/flux"
    },

    # Ninja Ultra Features
    "deep-research-2.0": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/deep-research"
    },
    "superagent-apex": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/superagent"
    },
    "superagent-r-2.0": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/superagent"
    },
    "file-upload-analysis": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/file-analysis"
    },
    "stable-diffusion-core": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/image"
    },
    "video-generation-beta": {
        "provider": "ninja",
        "endpoint": "https://api.myninja.ai/video"
    }
}
