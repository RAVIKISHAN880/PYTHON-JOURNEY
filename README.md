# python-journy

My weekly Python learning journey — one small project at a time.
Goal: code regularly, commit often, keep the GitHub graph green with real work.

## Structure

Each project lives in its own top-level folder:

```
python-journy/
  README.md
  .gitignore
  calculator/
    main.py
    README.md
  todo-cli/
    main.py
    README.md
```

No starter projects yet — you add them as you learn.

## How to add a new project

1. Create a folder (use lowercase + hyphens):
   ```
   mkdir my-project
   ```

2. Inside it, create your code + a short README:
   ```
   my-project/
     main.py      <- your code
     README.md    <- what it does + concepts used
   ```

   Minimal `README.md` template for each project:
   ```markdown
   # my-project
   What it does:
   Concepts used:
   How to run: python main.py
   ```

3. Save + push (for green boxes, commit every day you code):
   ```
   git add .
   git commit -m "add: my-project - short description"
   git push
   ```

   Tip: small frequent commits > one big commit.

## Progress log

| # | Project | Concepts | Date | Status |
|---|---------|----------|------|--------|
| 1 | _example: calculator_ | _variables, input, if/else_ | - | planned |
|   | | | | |
|   | | | | |

Copy the row for each new project.

## First-time push to GitHub

Local git is already initialized. To connect to GitHub:

1. Go to https://github.com/new
2. Repository name: `python-journy`
3. Keep it Public (so contributions show green), don't init with README
4. Then run (replace YOUR-USERNAME):
   ```
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/python-journy.git
   git add .
   git commit -m "init: python-journy learning repo"
   git push -u origin main
   ```

After that, just `git add .`, `git commit -m "..."`, `git push` each time.

## Rules for green boxes

- Commits must be on `main`, on GitHub (not just local), with your GitHub email.
- Check: `git config user.email` should match your GitHub email.
- Push the same day you code.
