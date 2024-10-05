## 2.2 Data representation
A tensor is a multi-dimensional **array**, I mean  **arrays** inside arrays.

### 2.2.1 tensor

By packing a tensor, you increase it's rank.

```python
x = np.array(12) # rank 1
xii = np.array([12] # rank 2
...
xn = np.array)[[[...]]]
```

A tensor has three elements

- shape (.shape)
- type (dtype)
- number of axis (ndim) or rank
