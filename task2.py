from task3 import decorator_1

@decorator_1
def typeBasedTransformer(**kwargs):
 res = {}
 for key, val in kwargs.items():
  if isinstance(val, bool):
   res[key] = not val
  elif isinstance(val, (int, float)):
   res[key] = val ** 2
  elif isinstance(val, (list, tuple)):
   res[key] = type(val)(reversed(val))
  elif isinstance(val, str):
   res[key] = val[::-1]
  elif isinstance(val, dict):
    res[key] = {b: a for a, b in val.items()}
  else:
   res[key] = val
 return res
