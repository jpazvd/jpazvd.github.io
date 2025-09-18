# Session Summary: Debugging and Resolution of Jekyll Build Failures (2025-09-18)

## 1. Initial Problem

The primary issue was the consistent failure of the native "pages build and deployment" GitHub Action. This prevented the site from updating, despite a separate custom GitHub Actions workflow (`Build and Deploy (Jekyll 4 + Scholar)`) appearing to function correctly.

## 2. Root Cause Analysis

The core of the problem was a fundamental conflict between two parallel build systems running on the same codebase:

1.  **Native GitHub Pages Build:** A restrictive, built-in process that uses an older version of Jekyll (v3.x) and a limited, whitelisted set of plugins. This system did not support `jekyll-scholar`.
2.  **Custom GitHub Actions Workflow:** A flexible, user-defined workflow (`.github/workflows/pages.yml`) configured to use a modern stack, including Jekyll v4.x and the `jekyll-scholar` plugin, to generate the site with full functionality.

The native build would fail because it encountered Liquid tags (`{% bibliography %}`) and plugin configurations it did not recognize, halting the deployment process.

## 3. The Solution: A Stable Dual-Build Architecture

After attempting to unify the build process into a single workflow and then reverting, the final, successful solution was to refine and commit to the **dual-build architecture**. This approach allows both systems to coexist by carefully separating their configurations and dependencies.

### How the Fix Works:

1.  **Isolate Configurations:**
    *   `_config.yml`: Contains the base configuration compatible with the native GitHub Pages build. It does **not** include the `jekyll-scholar` plugin.
    *   `_config.scholar.yml`: A separate file containing **only** the `jekyll-scholar` configuration.
    *   `Gemfile`: Specifies the `github-pages` gem, locking the dependency environment to what the native build expects.
    *   `Gemfile.ci`: A separate file used exclusively by the custom workflow, specifying Jekyll 4, `jekyll-scholar`, and other modern dependencies.

2.  **Conditional Rendering in Content:**
    *   Pages that rely on `jekyll-scholar` (e.g., `_pages/publications.md`) were modified to include conditional Liquid logic. This checks if the `jekyll-scholar` plugin is loaded in the current build environment.
    *   **Example:**
        ```liquid
        {% if site.plugins contains 'jekyll-scholar' %}
          {% bibliography %}
        {% else %}
          <!-- Static fallback content or a simple message -->
        {% endif %}
        ```
    *   This allows the native build to "gracefully degrade" by skipping the unsupported tags, thus avoiding a fatal error.

3.  **Authoritative Custom Workflow:**
    *   The custom workflow (`.github/workflows/pages.yml`) is configured to be the **only one that matters for deployment**.
    *   It explicitly uses `Gemfile.ci` and both `_config.yml` and `_config.scholar.yml`.
    *   This ensures it builds the site with all features enabled, generates the final `_site` directory, and successfully deploys it to GitHub Pages.

By implementing this separation of concerns, the native build is allowed to run without failing catastrophically, while the custom workflow handles the actual building and deployment of the feature-rich site.
