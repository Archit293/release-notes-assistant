\# Release Notes Assistant



\## What this project is

A command-line tool that turns raw implementation tickets and commit

comments into clean, customer-readable release notes, grouped into

categories. Built as an answer to a Bosch internship task about

automating release notes with AI.



\## Who is building it

The owner does not write code and is learning Claude Code. Explain every

change in plain language before making it. Keep changes small, one at a time.



\## Scope (do not add beyond this)

\- One file: release\_notes.py, a command-line tool

\- Paste in commit messages and ticket titles/descriptions (multi-line,

&#x20; ended by a line with just END)

\- Output: release notes grouped into Features, Fixes, Improvements, Other

\- If an entry is unclear or too vague to describe safely, flag it for

&#x20; human review instead of inventing a description

\- Clearly mark that a human must review and approve before publishing

\- Save each result to release\_notes\_log.md with a timestamp

\- Uses the Google Gemini API (model gemini-flash-latest)

\- Packaged in a Dockerfile

\- A clear README with an example run and a workflow diagram showing the

&#x20; human approval step



\## Not in scope

Reading directly from Git or Jira, web interface, user accounts.

List these as "future work" in the README only.



\## Hard constraints

\- Zero cost. Free tier only.

\- The API key lives in .env only. Never write it elsewhere. Never commit .env.



\## How to work with me

\- Ask before creating, changing, or deleting files.

\- Explain what a change does before doing it, in plain language.

\- One step at a time.

