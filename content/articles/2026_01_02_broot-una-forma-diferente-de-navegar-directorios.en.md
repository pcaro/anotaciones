---
Title: broot, a different way to navigate your directories
Date: 2026-01-02 10:00
Tags: terminal, cli, broot, rust, tools
Lang: en
Category: Tools
Slug: broot-una-forma-diferente-de-navegar-directorios
Summary: broot is a terminal tool that allows you to explore your directories in an interactive way and much more powerful than traditional commands like ls or tree.
Status: draft
---

Hello! How are you? Today I want to tell you about a tool that blew my mind for moving through directories on my computer: it's called **broot**. If you are one of those who get tangled up with `ls` or `cd` and always end up lost, you are going to love this.

### broot, a different way to navigate your directories

Imagine you have a bunch of folders and files, and you want to find something quickly or just understand what's there. With the usual commands, sometimes it's a drag, right? Well, broot comes to solve that in a super visual and efficient way.

**What is broot?**

In short, broot is a terminal tool that allows you to explore your directories in an interactive way and much more powerful than traditional commands like `ls` or `tree`. It's like having a graphical file explorer, but directly in your terminal.

**What is it for? Its main features:**

*   **Instant overview:** It gives you a tree view of your directories, even if they are huge, but intelligently. It doesn't overwhelm you with thousands of lines, but hides what is not relevant (like files ignored by Git) so you can focus on what matters. But if you want to see them, you can too!
*   **Fast navigation:** Remember that directory you don't know where you put? With broot, you just have to type a few letters of what you are looking for, and it finds it for you. You can move between results, go up and down the hierarchy, and when you find the place, an `alt + enter` takes you directly to that directory in your terminal. Goodbye to `cd ../../stuff/more_stuff`!
*   **Don't get lost in the search:** Unlike other searchers, broot always shows you where the file or directory you are looking for is within the folder structure. So, you never lose context. You can search by name, by file content, and even use regular expressions!
*   **Blind file manipulation:** Need to move, copy, delete or create a directory? With broot, you can do it seeing the file structure at all times. It is much safer and visual than doing it "blindly" with `mv` or `cp`.
*   **Panels to work better:** One of the coolest things is that you can open multiple panels. Imagine you want to copy something from one folder to another: you open a panel with the source, another with the destination, and drag (well, not drag, but almost) the files between them. Ideal for organizing!
*   **File preview:** If you select a file, you can preview its content directly in a side panel. Even images if your terminal supports it!
*   **Execute commands on files:** You find a file you want to edit, type `:e` and `enter`, and broot opens it with your favorite editor. You can configure your own "verbs" (commands) to do whatever you want with the selected files.
*   **Replaces `ls` on steroids:** If you want to see sizes, dates, permissions, etc., broot shows it to you clearly and orderly. In addition, you can sort by size or date to see what is taking up the most space or what you have modified recently.
*   **Git control:** If you work with Git, broot shows you the status of your files (modified, new, etc.), the current branch and change statistics. You can even see only the files that `git status` would show you!

In short, broot is a Swiss Army knife for the terminal that makes your life much easier when interacting with your files and directories. If you spend a lot of time in the terminal, I recommend you take a look at it. You're going to love it!

![broot help]({static}/images/broot_help.png)
