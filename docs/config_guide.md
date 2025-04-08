# Configuration Parameters for Gemini

## 🔧 Parameters

- `temperature`: Controls creativity (0.1 = deterministic, 0.9 = creative)
- `top_p`: Controls diversity by nucleus sampling

## 🔍 Examples

```python
model.generate_content("Tell a joke", generation_config={"temperature": 0.1})
```

```python
model.generate_content("Tell a joke", generation_config={"top_p": 0.9})
```