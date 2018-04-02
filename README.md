# pipe

Simple and lightweight package to easily multithread work but retain the job ordered.

## Installation
```bash
git clone https://github.com/DomHudson/pipe && cd pipe
pip install .
```

## Usage

```python
import pipe

def work(item):
  return item ** 2

for item in pipe.Pipe().run(list(range(10)), work):
  print(item, end=' ')
```
> 0 1 4 9 16 25 36 49 64 81 
