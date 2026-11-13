# pacmanboard-test-package

A minimal Python package for validating the Pacman Board workflow from GitHub through Posit Package Manager.

## Package layout

- `src/pacmanboard_test_package/`: installable package source.
- `tests/`: simple smoke tests.
- `dist/`: built wheel artifact. Commit the wheel here so the scheduled Pacman Board R Markdown job can find it in the GitHub repository.

## Build a wheel

Use Python 3.9 or later. From this project directory, create and activate a virtual environment if desired, install the build frontend, and run:

```text
python -m pip install --upgrade build
python -m build --wheel --outdir dist
```

This produces a wheel like `dist/pacmanboard_test_package-0.1.0-py3-none-any.whl`. The current Pacman Board importer expects the standard wheel filename layout without an optional build tag.

To test the package locally:

```text
python -m pip install --force-reinstall dist/pacmanboard_test_package-0.1.0-py3-none-any.whl
python -c "from pacmanboard_test_package import greet; print(greet())"
```

Optional tests (install pytest first):

```text
python -m pip install pytest
python -m pytest
```

## Push the test artifact to GitHub

Create an empty GitHub repository for this package, then from this directory initialize Git if needed, stage the source and wheel, commit, and push to your branch. The built wheel under `dist/` is intentionally not ignored because the Rmd searches that configured path in GitHub.

In the Pacman Board Shiny app, use:

- Domain: `DSS`
- Package Language: `Python`
- GitHub URL: your new repository URL
- Branch: the branch you push (for example `main`)
- Path in branch: `dist`

Ensure the Connect-side GitHub identity can read the repository. The Rmd stages the wheel under a package-named directory in the shared custom root. The PPM pod's `script.py` then scans it and invokes `rspm add` after the vulnerability scan succeeds.

## Publish a new test version

For each new test build, update `version` in `pyproject.toml` and `__version__` in `src/pacmanboard_test_package/__init__.py` to the same new version, build the wheel again, and push the source and wheel. Use a new version each time: the staging/import pipeline does not overwrite or replace an existing package version.
