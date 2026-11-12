# Image agent

Install the project and its CLI commands:

```bash
uv sync
```

Generate an image using the API key configured in `.env`:

```bash
uv run --env-file .env image-agent "A watercolor fox reading under a street lamp"
```

The `image_agent` command is also supported as an alias for `image-agent`.

