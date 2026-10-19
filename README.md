# Ashwin's Chronicles (ashwinschronicles.github.io)

Personal blog and technical notebook of **Ashwin Kumar Karnad**, Research Software Engineer at the Jülich Supercomputing Centre (JSC), Forschungszentrum Jülich, Germany.

Built using [Pelican](https://getpelican.com/) and the [Elegant](https://pelican-elegant.github.io/) theme.

---

## Architecture & Branches

- **`source` branch**: Contains all markdown content, images, configuration files (`pelicanconf.py`, `publishconf.py`), themes, and GitHub Actions workflows. All development and writing happens here.
- **`master` branch**: Contains the generated HTML/CSS/JS output produced by Pelican, served directly by GitHub Pages at [ashwinschronicles.github.io](https://ashwinschronicles.github.io).

---

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/) (recommended) or Python >= 3.11
- Git with submodule support

### Setup

1. **Clone the repository with submodules:**
   ```bash
   git clone --recursive -b source https://github.com/ashwinschronicles/ashwinschronicles.github.io.git
   cd ashwinschronicles.github.io
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure environment (optional):**
   Copy `.env.example` to `.env` if you need custom analytics or site credentials during production builds:
   ```bash
   cp .env.example .env
   ```

---

## Local Development

- **Build and serve locally (with livereload/autoreload):**
  ```bash
  make devserver
  ```
  Then open [http://localhost:8000](http://localhost:8000).

- **Standard build:**
  ```bash
  make html
  ```

- **Clean output directory:**
  ```bash
  make clean
  ```

---

## Deployment

### 1. Automated CI/CD (Recommended)

Every push to the `source` branch automatically triggers the GitHub Actions workflow (`.github/workflows/deploy.yml`), which:
1. Runs inside the `ghcr.io/astral-sh/uv:debian-slim` container.
2. Installs dependencies using `uv sync --frozen`.
3. Compiles the production site using `publishconf.py`.
4. Deploys the generated output to the `master` branch via `ghp-import`.

Simply push your changes to `source`:
```bash
git push origin source
```

### 2. Manual Deployment (Fallback)

If you need to build and push directly from your local terminal:
```bash
make github
# or using aliases:
make ghpage
make deploy
```

---

## Writing Content

New articles should be placed in the appropriate subfolder inside `content/` (`content/Science/`, `content/Engineering/`, `content/Blog/`, or `content/LectureNotes/`).

See [`Template.md`](Template.md) for available metadata and frontmatter fields.