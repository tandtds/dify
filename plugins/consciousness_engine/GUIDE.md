# Development Guide: consciousness_engine

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start Development Server**
   ```bash
   python -m main
   ```

3. **Install in Dify**
   - Open Dify → Plugins → Install from local
   - Enter: http://localhost:5003
   - Click Install

4. **Test the Plugin**
   - Create a new workflow
   - Add your plugin node
   - Configure and test

## Development Workflow

1. Make changes to Python files
2. Server auto-reloads
3. Test in Dify
4. Repeat

## File Structure

- `manifest.yaml` - Plugin metadata
- `provider/consciousness_engine.yaml` - Provider configuration
- `tools/` - Tool implementations
- `_assets/` - Icons and assets
- `main.py` - Entry point

## Testing

Run unit tests:
```bash
python -m pytest tests/
```

## Packaging

```bash
dify plugin package ./
```

This creates `consciousness_engine-0.0.1.difypkg`

## Publishing

See main documentation for publishing to:
- Dify Marketplace
- GitHub
- Private distribution
