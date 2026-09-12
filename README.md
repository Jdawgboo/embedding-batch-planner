# Embedding Batch Planner

Create deterministic index batches from caller-supplied token lengths and item/token capacity limits.

```bash
cat lengths.json | python tool.py
python -m unittest -v
```

Lengths must come from an appropriate tokenizer or upstream estimate. The tool does not call embedding providers.
