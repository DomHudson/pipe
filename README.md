# pipe

Simple and lightweight package to easily multithread work but retain the ordering. Provide a callable and an iterable of arguments. `pipe.Pipe` will yield the results in the correct order.

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

for item in pipe.Pipe(threads=2).run(range(6), work):
  print(item, end=' ')
```
> 0 1 4 9 16 25

## Exception Handling

Easily retrieve exceptions from within threads.

```python
import pipe

def work(item):
  if item == 3:
    raise Exception('Cannot process.')
  return item ** 2

def handler(e):
  print(e, end=' ')

for item in pipe.Pipe(exception_handler=handler).run(range(6), work):
  print(item, end=' ')
```
> 0 1 4 Cannot process. 16 25 

## Run Post-Processing on Results

Easily handle the results in the main-thread as they're yielded.

```python
import pipe

def work(item):
  return item ** 2
  
def processor(result):
  return [result]

for item in pipe.Pipe(post_processor=processor).run(range(6), work):
  print(item, end=' ')
```
> [0] [1] [4] [9] [16] [25] 
