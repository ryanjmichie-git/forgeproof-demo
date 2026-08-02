# ForgeProof Demo

A deliberately small Python calculator library, used to demonstrate
[ForgeProof](https://github.com/ryanjmichie-git/forgeproof-plugin) — provenance-tracked
code generation with a cryptographically signed audit trail.

## What this repo is for

Each open issue describes one small feature. Running `/forgeproof:run <issue>` in
Claude Code implements it and seals the entire process — requirements, design
decisions, file edits, and test results — into an Ed25519-signed `.rpack`
provenance bundle that any reviewer can verify independently.

Every pull request from a `forgeproof/*` branch is checked automatically by the
[forgeproof-verify](https://github.com/marketplace/actions/forgeproof-verify) Action:
the check goes green when the code matches what was signed, and red the moment
anything changes after signing.

## Current API

```python
import calculator

calculator.add(2, 3)       # 5
calculator.multiply(3, 4)  # 12
```

## Running the tests

```bash
python -m pytest -q
```
