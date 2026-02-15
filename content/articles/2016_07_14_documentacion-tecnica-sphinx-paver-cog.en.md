Title: Technical Documentation with Sphinx, Paver, and Cog
Date: 2016-07-14 00:47
Tags: sphinx, paver, cog, documentation, rst, automation
Lang: en
Category: Documentation
Slug: documentacion-tecnica-sphinx-paver-cog
Summary: Automated workflow to create technical documentation using Sphinx, Paver, and Cog, eliminating repetitive tasks and manual errors in code examples

**Doug Hellmann** presents a robust workflow for technical documentation that eliminates repetitive manual work and errors in code examples.

## The Problem to Solve

> "Automation is important for my sense of well being. I hate dealing with mundane repetitive tasks."

**Common Challenges**:
- Keeping **code examples updated**
- **Multiple output formats** (HTML, PDF, blog)
- **Repetitive tasks** of building and publishing
- **Copy-paste errors** in program output

## The Solution: Trio of Tools

### Sphinx: Documentation Engine
- **reStructuredText conversion** to multiple formats
- **Customizable themes** with Jinja templates
- **Automatic generation** of indices and cross-references

### Paver: Build Automation
```python
# pavement.py
@task
def html():
    """Build HTML documentation"""
    call_task('cog')
    sphinx_build('html')

@task  
def pdf():
    """Build PDF documentation"""
    call_task('cog')
    sphinx_build('latex')
    make_pdf()
```

**Solves**: Automation of repetitive build processes

### Cog: Automatic Code Insertion
```rst
.. cog::
   
   import cog
   import subprocess
   
   result = subprocess.run(['python', 'example.py'], 
                          capture_output=True, text=True)
   cog.out(result.stdout)

.. cog::
```

**Key Advantage**: Program output is **automatically updated** when regenerating documentation.

## Production Workflow

### 1. Writing in reStructuredText
```rst
Usage Example
=============

We run the script:

.. cog::
   cog.out("$ python my_script.py\n")
   result = subprocess.run(['python', 'my_script.py'], 
                          capture_output=True, text=True)
   cog.out(result.stdout)
.. cog::
```

### 2. Automated Build
```bash
# A single command for everything
paver html

# Or for multiple destinations
paver all_formats
```

### 3. Multi-Destination Publishing
- **Python Module of the Week (PyMOTW)**
- **Personal Blog**
- **Project Website**
- **O'Reilly Blog**
- **PDF Documentation**

## Advantages of the Approach

### Guaranteed Consistency
- **Examples always updated** with real code
- **Uniform format** across multiple destinations
- **No manual transcription** errors

### Maximized Efficiency
- **One source, multiple outputs**
- **Complete automation** of the pipeline
- **Focus on content**, not process

### Maintainability
- **Changes in a single source** propagate automatically
- **Integrated testing** of code examples
- **Unique versioning** for all documentation

## Practical Implementation

```python
# full pavement.py
from paver.easy import *
import paver.doctools

@task
def cog():
    """Run Cog to update code examples"""
    sh('cog -r *.rst')

@task
@needs('cog')
def html():
    """Build HTML docs"""
    paver.doctools.html()

@task
@needs('cog') 
def blog_post():
    """Generate blog post version"""
    # Custom blog formatting
    pass
```

This workflow represents **intelligent automation** of technical documentation: write once, publish everywhere, always updated.

*Original source*: [Doug Hellmann](https://doughellmann.com/blog/2009/02/02/writing-technical-documentation-with-sphinx-paver-and-cog/)
