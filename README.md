# pipe

Simple and lightweight package to easily multithread work but retain the job ordering.

## Installation
```bash
git clone https://github.com/DomHudson/pipe && cd pipe
pip install .
```

## Basic Usage

```python
import pipe

def work(item):
  return item ** 2

for item in pipe.Pipe(threads=2).run(list(range(10)), work):
  print(item, end=' ')
```
> 0 1 4 9 16 25 36 49 64 81 

## Exception Handling

Easily retrieve exceptions from within threads.

```python
import pipe

def work(item):
  if item == 3:
    raise Exception('Cannot handle \'3\'')
  return item ** 2

def handler(e):
  print(e, end=' ')

for item in pipe.Pipe(exception_handler=handler).run(list(range(10)), work):
  print(item, end=' ')
```
> 0 1 4 Cannot handle '3' 16 25 36 49 64 81
