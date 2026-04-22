# Contributing to gitoma-bench-ladder

This document outlines how you can contribute to the gitoma-bench-ladder project.

## Overview

We welcome contributions from everyone! Whether you are a new contributor or a seasoned engineer, your insights and code are valuable to the project.

This repository contains benchmarks and related tools for evaluating different configurations or implementations. Contributions can include:

*   **Feature Development:** Implementing new benchmarks, analysis tools, or features related to the benchmarking framework.
*   **Bug Fixes:** Identifying and resolving issues in existing benchmark logic or tooling.
*   **Documentation:** Improving READMEs, adding explanations for complex benchmarks, or clarifying usage instructions.
*   **Testing:** Writing new unit or integration tests to ensure the correctness of existing logic.

## Development Workflow

1.  **Fork the Repository:** Fork this repository to your own account.
2.  **Clone Locally:** Clone your fork to your local machine:
    ```bash
    git clone <YOUR_FORK_URL>
    cd gitoma-bench-ladder
    ```
3.  **Create a New Branch:** Create a new branch for your changes:
    ```bash
    git checkout -b feature/my-new-benchmark
    ```
4.  **Make Changes:** Implement your changes and ensure they pass any existing tests.
5.  **Commit Changes:** Commit your changes with a clear, descriptive message:
    ```bash
    git add . 
    git commit -m "feat: Add new benchmark for XYZ" 
    ```
6.  **Push to Fork:** Push your branch to your fork:
    ```bash
    git push origin feature/my-new-benchmark
    ```
7.  **Open a Pull Request (PR):** Open a Pull Request against the main branch of the original repository, clearly explaining your changes, testing approach, and any relevant context.

## Code of Conduct

We are committed to maintaining a friendly and inclusive development environment. Please read our [CODE_OF_CONDUCT.md] (if available, otherwise add one) or adhere to the general principles of respectful communication.

## Benchmarking Standards

When adding new benchmarks, please ensure they:

*   Are reproducible.
*   Are clearly documented regarding the setup, expected inputs, and expected outputs.
*   Adhere to the established project style.

## Reporting Issues

If you encounter bugs or have questions, please open an issue on the repository first. For urgent issues, please use the issue tracker.
