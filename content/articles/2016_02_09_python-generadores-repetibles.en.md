Title: Python: Create Repeating Generators
Date: 2016-02-09 10:10
Tags: python, generators, itertools, decorators, yield
Lang: en
Category: Python
Slug: python-generadores-repetibles
Summary: Techniques in Python to create generators that can be iterated multiple times, overcoming the "one-shot" limitation of standard generators

**Generators in Python are "one-shot"** - they can only be iterated once. How to create generators that can be reused multiple times?

## The Problem

```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(list(gen))  # [1, 2, 3]
print(list(gen))  # [] - Empty!
```

## Solution 1: Class Approach (Most Robust)

```python
def multigen(gen_func):
    class _multigen(object):
        def __init__(self, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs
        def __iter__(self):
            return gen_func(*self.__args, **self.__kwargs)
    return _multigen

# Usage
@multigen
def my_repeatable_generator(max_num):
    for i in range(max_num):
        yield i

gen = my_repeatable_generator(3)
print(list(gen))  # [0, 1, 2]
print(list(gen))  # [0, 1, 2] - Works!
```

## Solution 2: itertools.cycle() for Infinite Sequences

```python
import itertools

# Repeat a sequence infinitely
repeating_gen = itertools.cycle([1, 2, 3])

# Take only the first 9 elements
result = list(itertools.islice(repeating_gen, 9))
print(result)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## Solution 3: Lambda Wrapper (Simple)

```python
def my_generator():
    yield 1
    yield 2
    yield 3

# Wrapper to create new instance each time
repeatable_generator = lambda: my_generator()

print(list(repeatable_generator()))  # [1, 2, 3]
print(list(repeatable_generator()))  # [1, 2, 3]
```

## Solution 4: Factory Function

```python
def create_generator(data):
    def generator():
        for item in data:
            yield item
    return generator

# Usage
gen_factory = create_generator([1, 2, 3])
gen1 = gen_factory()
gen2 = gen_factory()

print(list(gen1))  # [1, 2, 3]
print(list(gen2))  # [1, 2, 3]
```

## When to use each approach?

### Decorator Class (`@multigen`)
- **Complex generators** with parameters
- **Maximum flexibility** and reuse
- **Preserves metadata** of the original generator

### `itertools.cycle()`
- **Infinite repetition** of small sequences
- **Known cyclic patterns**
- **Very efficient** in memory

### Lambda Wrapper
- **Simple cases** without parameters
- **Rapid prototyping**
- **Stateless generators**

### Factory Function
- **Balance** between simplicity and flexibility
- **Generators with initial configuration**
- **More explicit code**

## Performance Considerations

⚠️ **Memory**: Repeatable generators may require storing initial parameters
⚠️ **CPU**: Each iteration recalculates from the start

The choice depends on whether you need **exact repetition** or **efficient reuse**.

*Original source*: [Stack Overflow](http://stackoverflow.com/questions/1376438/how-to-make-a-repeating-generator-in-python/1376531#1376531)
