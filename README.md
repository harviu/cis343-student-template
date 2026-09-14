# CIS343 cumulative interpreter labs

Python Lox starter for a single repository used throughout the course.
Python 3.12 and Git are required; no third-party Python packages are needed.

## Start your repository

1. Select **Use this template → Create a new repository**.
2. Create a **private** repository named `cis343-mylox-YOUR-USERNAME`.
3. Invite `harviu` through **Settings → Collaborators** so the instructor can grade it.
4. Clone your repository and work in that checkout.

## Lab 1

Implement `Token` in `src/lox_token.py` and `Scanner` in `src/scanner.py`.
Token names and an error handler are provided. The entry point is provided as
plumbing; later labs extend its `run` method. See the [test contract](https://github.com/harviu/cis343-tests/blob/main/CONTRACT.md).

```sh
python3 src/lox.py examples/scanner.lox
python3 src/lox.py
python3 scripts/test.py
```

The starter intentionally raises `NotImplementedError`. Lab 1 checks will fail
until you implement it; a red check is expected at the beginning.

## Automatic feedback

Every push runs **Cumulative lab tests**. Open **Actions**, select the run, and
open a lab job to see individual checks. **Actions → Cumulative lab tests → Run
workflow** starts a fresh check without a new commit.

The workflow and tests come from `harviu/cis343-tests` at run time. You do not
need to copy new tests when another lab is released. `python3 scripts/test.py`
also downloads the current tests every time. Internet access is required for
that command. If fetching fails, it reports an error instead of using stale tests.

Only released labs run. Each lab has a separate result. Earlier labs continue
running as regression checks. The logs identify the test commit used.
Do not change `.github/workflows/tests.yml` to bypass checks.

## Submission

Keep your implementation in this repository for all cumulative labs. Put reports
in `reports/`. Push your changes and submit the exact **commit URL** in Blackboard
for each lab, along with any materials required by the instructor. This preserves
which version you submitted while you continue working on the next lab.

These practice tests check the Python Lox reference interfaces. If you implement
another language or grammar, agree on an equivalent testing interface with the
instructor. Automated feedback is not the whole grade: reports, design,
readability, and the remaining course rubric are reviewed separately.

Provided scaffold files are instructor starter material. Follow the course's
attribution policy for code you add. Future lab instructions will be released by
the instructor; this repository does not replace them.
