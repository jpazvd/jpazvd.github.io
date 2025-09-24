# Deployment Architecture & Debugging Guide

This document explains the specific deployment process for this Jekyll website. Understanding this architecture is critical for effective debugging and future maintenance.

**The most important thing to know is: This site does NOT use the standard GitHub Pages build process. It uses a custom GitHub Actions workflow to build and deploy.**

---

## I. Core Architecture Overview

The site relies on a **CI/CD (Continuous Integration/Continuous Deployment)** pipeline managed by GitHub Actions. This approach provides the flexibility to use modern versions of Jekyll and plugins that are not natively supported by GitHub Pages (like `jekyll-scholar`).

The process is as follows:
1.  You push a commit to the `main` branch.
2.  This push triggers the GitHub Actions workflow defined in `.github/workflows/`.
3.  The workflow builds the Jekyll site in a controlled environment using the dependencies from `Gemfile.ci`.
4.  Once the build is complete, the workflow pushes the resulting static HTML files to a separate branch (typically `gh-pages`).
5.  GitHub Pages is configured to serve the content directly from the `gh-pages` branch, without running its own build.

---

## II. Key Files and Their Roles

-   **`.github/workflows/`**: This directory contains the YAML file(s) that define the entire build and deploy process. **This is the brain of your deployment.** When debugging, the logs from this workflow are the most important source of information.

-   **`.nojekyll`**: This file is **ESSENTIAL** and **MUST NOT be deleted**. Its presence tells GitHub Pages to *not* run a Jekyll build and to simply serve the files as they are. This is what allows our custom workflow to function correctly.

-   **`Gemfile.ci`**: This file lists the exact Ruby gems (Jekyll version, plugins) used by the GitHub Actions workflow to build the site. It ensures a consistent and reproducible build environment.

-   **`gh-pages` branch**: This branch contains only the *output* of the build—the static HTML, CSS, and JavaScript files that make up the live website. You should never edit this branch directly.

---

## III. Future Debugging Checklist

If you encounter a 404 error or other deployment issues in the future, follow these steps in order:

**Step 1: Check the GitHub Actions Workflow Logs**
- Go to your repository on GitHub.
- Click on the **"Actions"** tab.
- Look for the most recent workflow run. If it has a red "X", it failed.
- Click on the failed run, then click on the "build" or "deploy" job to see the detailed logs. The error message will almost always be in these logs.

**Step 2: Review Common Pitfalls (The "Do Not Do This" List)**
- **DO NOT** delete the `.nojekyll` file. This will break the deployment process.
- **DO NOT** assume the plugin limitations of standard GitHub Pages apply to this site. Because we use a custom workflow, we can use almost any Jekyll plugin.
- **DO NOT** look for build errors in the repository's "Settings" > "Pages" section. The errors will be in the "Actions" tab.

**Step 3: Local Verification**
- If you can't solve the issue from the logs, try to replicate the build locally using the CI environment's configuration:
  ```bash
  # Make sure your dependencies are installed
  bundle install --gemfile Gemfile.ci

  # Run the build command
  bundle exec jekyll build --config _config.yml,_config.scholar.yml
  ```
- This will often show you the error on your local machine before you even have to push a commit.

By following this guide, you should be able to quickly diagnose and resolve future deployment issues.
