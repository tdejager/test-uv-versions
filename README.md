## uv example workspace

This repository shows how to configure a `uv`-managed project that pulls in local packages in three different ways:

- `pkg-editable`: An editable path dependency.
- `pkg-dynamic`: A regular path dependency whose version is provided dynamically from the package.
- `pkg-versioned`: A workspace member that declares an explicit version.

### Layout

- `pyproject.toml`: Declares the application along with the three dependency types and the workspace configuration.
- `packages/pkg_editable`: Simple package exposed as an editable dependency.
- `packages/pkg_dynamic`: Package that reports its version from code via `tool.setuptools.dynamic`.
- `packages/pkg_versioned`: Workspace member with a pinned version.

### Using the project

1. Install `uv` from https://docs.astral.sh/uv/.
2. Create a virtual environment for the project:
   ```bash
   uv venv
   ```
3. Install dependencies, including the local path packages:
   ```bash
   uv pip install -e .
   ```
4. Run the sample script to exercise the packages:
   ```bash
   uv run python main.py
   ```

`uv` will install `pkg-editable` in editable mode, resolve `pkg-dynamic` from the path while reading its dynamic version, and treat `pkg-versioned` as a workspace member with the declared `1.0.0` version.
