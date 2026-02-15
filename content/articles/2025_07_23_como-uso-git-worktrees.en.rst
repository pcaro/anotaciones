How I Use Git Worktrees for Concurrent Work
###########################################

:date: 2025-07-23 06:12
:tags: git, worktrees, workflow, productivity
:lang: en
:category: Programming
:slug: como-uso-git-worktrees
:summary: A practical approach to using git worktrees and maximizing productivity with multiple simultaneous work contexts

Aleksey Kladov shares his unique approach to using git worktrees, which goes beyond simply switching branches and becomes a complete methodology for concurrent work.

.. image:: https://matklad.github.io/images/worktree-structure.png
   :alt: Worktree structure
   :align: center

The Core Philosophy
===================

**"Git is not a version control system, Git is a toolbox for building a VCS"**

This perspective completely changes how we think about git. Instead of limiting ourselves to basic functionalities, we can create our own optimized workflow.

The 5 Specialized Worktrees
===========================

The author maintains 5 worktrees, each with a specific purpose:

1. **main** - Read-only snapshot
   - Clean reflection of remote main
   - Reference for comparisons
   - Never modified locally

2. **work** - Main workspace
   - Day-to-day active development
   - Frequent commits with minimal messages
   - Detached HEAD for maximum flexibility

3. **review** - Dedicated to code reviews
   - Clean context to analyze PRs
   - Without interfering with ongoing work

4. **fuzz** - Long-running tests
   - Fuzzing and tests that last hours
   - Runs in parallel without blocking development

5. **scratch** - Unrelated quick tasks
   - Experiments
   - Urgent fixes
   - Ad-hoc investigations

.. code-block:: bash

    # Typical directory structure
    ~/projects/my-project/
    ├── main/        # main worktree
    ├── work/        # active development
    ├── review/      # reviews
    ├── fuzz/        # testing
    └── scratch/     # experiments

Advantages of the Approach
==========================

**Truly Concurrent Work**
   - Multiple coding activities simultaneously
   - No need for stash or complex branch switching
   - Clean separation of contexts

**Frictionless Workflow**
   - Instant switching between tasks
   - Frequent commits without pressure for perfect messages
   - Free experimentation on detached HEAD

**Real Parallelization**
   - Fuzzing running while you develop
   - Reviews without interrupting main work
   - Background tests without blocks

Advanced Techniques
===================

**Strategic Detached HEAD**

.. code-block:: bash

    # In the 'work' worktree, work without a branch
    git checkout --detach HEAD
    # Frequent commit, reorganize later
    git commit -m "wip"

**Custom Scripts for Common Operations**

.. code-block:: bash

    # Script to quickly create/switch worktrees
    #!/bin/bash
    git worktree add "../$1" "$2"
    cd "../$1"

**Integration Flow**

.. code-block:: bash

    # From the 'work' worktree
    git log --oneline  # review commits
    git reset HEAD~5   # undo temporary commits
    git add -p         # select changes
    git commit         # clean final commit

Key Lessons
===========

1. **Git is flexible**: There is no "one right way" to use git
2. **Automate the repetitive**: Custom scripts for common operations
3. **Separate contexts**: Each type of work deserves its own space
4. **Cheap commits**: Commit frequently, organize later

This approach transforms git from a versioning tool into a complete workflow management platform, maximizing productivity through truly concurrent work.

*Original article*: `How I Use Git Worktrees`_

.. _How I Use Git Worktrees: https://matklad.github.io/2024/07/25/git-worktrees.html
