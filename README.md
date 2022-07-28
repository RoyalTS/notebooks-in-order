# notebooks-in-sequence

Don't you just hate it when people commit Jupyter notebooks with output in which cells have been executed out of sequence? In which not all cells have been executed?

`notebooks-in-sequence` is a pre-commit hook that enforces notebooks were executed from top to bottom. That is: every non-empty code cell was executed and the execution counts go from 1 to N.

## Install

To install the hook, just add this to your `.pre-commit-config.yaml`:

```yaml
repos:
- repo: https://github.com/RoyalTS/notebooks-in-order
  rev: 0.1.0
  hooks:
  - id: notebooks-in-order
```
