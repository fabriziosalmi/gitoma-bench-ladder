# Contributing to gitoma-bench-ladder

This document outlines the guidelines and expectations for contributing to the gitoma-bench-ladder project.

## Overview

We welcome contributions from everyone! Whether you are a new contributor or a seasoned engineer, your feedback and code are valuable to the project.

This repository is focused on benchmarking and calculator logic, and contributions should focus on improving correctness, performance, documentation, and maintainability.

## Code of Conduct

We are committed to maintaining a friendly and inclusive development environment. Please read our [CODE_OF_CONDUCT.md] (if one exists, otherwise state the policy) and adhere to respectful communication.

## How to Contribute

### 1. Setup

To get started, please follow these steps:

1. **Fork** the repository.
2. **Clone** your fork locally: `git clone <your-fork-url>`
3. **Navigate** to the repository directory: `cd gitoma-bench-ladder`
4. **Create a new branch** for your feature or fix: `git checkout -b feature/my-new-feature` (or use an issue tracker for tracking).

### 2. Development

*   **Feature/Bug Fixes:** Create a new branch for your changes. Ensure your changes address the specific issue or feature described in the corresponding issue ticket.
*   **Testing:** Always write unit tests for new logic or complex calculations. Ensure existing tests pass after your changes.
*   **Code Style:** Adhere to Rust community standards and the style conventions established in the repository. Use `cargo fmt` to keep code formatting consistent.
*   **Documentation:** Update or add comments where necessary, especially for complex logic in `src/calculator.rs`.

### 3. Submitting Changes

*   **Commit Messages:** Use clear, descriptive commit messages following the Conventional Commits specification (e.g., `feat: add new calculation module [scope]`, `fix: correct bug in benchmark logic [scope]`).
*   **Pull Requests (PRs):** Open a Pull Request targeting the main branch.
    *   Clearly describe what your PR does, why it is needed, and how it addresses any open issues.
    *   Include necessary information about tests that were added or modified.

## Project Structure

*   `src/`: Contains the core Rust source code, including the calculator logic.
*   `tests/`: Contains unit and integration tests for the code in `src/`.
*   `README.md`: Provides an overview of the project and how to run basic examples.

## Reporting Issues

If you encounter bugs or have suggestions, please open an issue on the [Issues] tracker first. This helps us prioritize work effectively.

Thank you for considering contributing to gitoma-bench-ladder!
