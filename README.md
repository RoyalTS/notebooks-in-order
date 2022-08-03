# notebooks-in-order

Don't you just hate it when people commit Jupyter notebooks with output in which cells have been executed out of sequence? In which not all cells have been executed?

`notebooks-in-order` is a pre-commit hook that enforces notebook execution from top to bottom. That is: every non-empty code cell was executed and the execution counts go from 1 to N.

## Install

To install the hook, just add this to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/RoyalTS/notebooks-in-order
  rev: 0.2.0
  hooks:
  - id: notebooks-in-order
```

You can additionally add

```yaml
  args: [--strip-on-fail]
```

to strip all output cells from the notebook if the check fails. That way a committer has the choice between re-running the notebook to generate the correct output, or choosing instead to commit input cells only.
