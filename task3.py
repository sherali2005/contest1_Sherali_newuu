import time

def decorator_1(func):
 def wrapper(*args, **kwargs):
  started_at = time.time()
  res = func(*args, **kwargs)
  ended_at = time.time()
  print(f"{func.__name__} call executed in {ended_at - started_at:.10f} sec\n")
  return res
 return wrapper

