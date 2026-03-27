# 🚀 FastAPI Template -- Quick Start Guide

This guide shows how to clone and start a new project from your FastAPI
template.

------------------------------------------------------------------------

## 1. Create a new repository from the template

1.  Go to your template repository on GitHub\
2.  Click **"Use this template"**\
3.  Choose a name for your new project\
4.  Click **Create repository**

------------------------------------------------------------------------

## 2. Clone the new repository

``` bash
git clone https://github.com/your-username/your-new-project.git
cd your-new-project
```

------------------------------------------------------------------------

## 3. Install dependencies

This project uses `uv` for dependency management.

``` bash
uv sync
```

------------------------------------------------------------------------

## 4. Activate the virtual environment (optional)

### macOS / Linux

``` bash
source .venv/bin/activate
```

### Windows

``` bash
.venv\Scripts\activate
```

------------------------------------------------------------------------

## 5. Run the development server

``` bash
uv run fastapi dev
```

------------------------------------------------------------------------

## 6. Open the app

-   API: http://127.0.0.1:8000\
-   Docs: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 7. Customize your project

Before starting development, update:

-   Project name (`pyproject.toml`)
-   README.md
-   Environment variables (`.env`)
-   App title and metadata

------------------------------------------------------------------------

## 💡 Tips

-   Always run `uv sync` when starting a new project
-   Do not rely on globally installed packages
-   Keep your template updated with improvements

------------------------------------------------------------------------

## ✅ You're ready!

You can now start building your FastAPI project 🚀
