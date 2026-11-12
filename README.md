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

## macOS import troubleshooting

If Python reports `ModuleNotFoundError: No module named 'image_agent'` after
installation, run `uv run python -v -c 'import image_agent'`. A message saying
`Skipping hidden .pth file` means Python is ignoring the editable install's
import path because its `.pth` file has the macOS hidden flag.

Keep virtual environments outside cloud-synced folders if those flags keep
returning. On this Mac, `.venv` links to
`~/Library/Caches/image-agent/venv`, outside the iCloud-managed Documents folder.
The run commands above still work, and source edits take effect immediately.
