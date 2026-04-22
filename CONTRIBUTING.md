# Contributing to gitoma-bench-ladder

This document outlines the guidelines, expectations, and process for contributing to the gitoma-bench-ladder project.

## Overview

We welcome contributions from the community! Whether you are a new contributor or an experienced engineer, your feedback and code are valuable to the project.

This repository focuses on benchmarking and testing related components. Contributions should focus on improving benchmarks, testing infrastructure, core logic, or documentation.

## Code of Conduct

We are committed to maintaining a friendly and inclusive development environment. Please read our [CODE_OF_CONDUCT.md] (if applicable) or adhere to the general principles of respectful communication.

## How to Contribute

### 1. Setup

To get started, please follow these steps:

1. **Fork** the repository.
2. **Clone** your fork locally: `git clone <your-fork-url>`
3. **Navigate** to the repository directory: `cd gitoma-bench-ladder`
4. **Create a new branch** for your feature or fix: `git checkout -b feature/my-new-feature` (or use an issue tracker's suggested branch naming convention).

### 2. Development

*   **Feature/Bug Fixes:** Create a new branch for your changes. Ensure your code adheres to existing coding standards (see `CONTRIBUTING.md` for style guides).
*   **Testing:** Always write comprehensive unit and integration tests for new features or bug fixes. Tests are crucial for maintaining the integrity of our benchmarks.
*   **Benchmarking:** If you are improving a benchmark, ensure it accurately reflects the intended measurement and adheres to best practices for performance testing.

### 3. Submitting Changes

*   **Commit Messages:** Use clear, descriptive commit messages following the Conventional Commits specification (e.g., `feat: add new benchmark for X`, `fix: correct calculation in Y`).
*   **Pull Requests (PRs):** Open a Pull Request targeting the main branch. Clearly describe what your changes do, why they are needed, and how they address any existing issues.
    *   Include a summary of changes in the PR description.
    *   If applicable, link to any related issues.

### 4. Code Style and Formatting

We strive for consistency. Please ensure your code is readable, well-structured, and idiomatic Go.

*   **Linting:** Run `go vet` and any other static analysis tools before submitting your PR.
*   **Formatting:** Use `go fmt` to ensure consistent formatting.

### 5. Reporting Issues

If you encounter bugs or have suggestions, please open an issue on the project tracker first. If it's a minor issue or suggestion that doesn't warrant an issue, consider opening a discussion in the relevant channel.

## Project Structure

*   `server/`: Contains the core server logic.
*   `store/`: Contains data storage or related structures.

## License

This project is licensed under the [LICENSE] license.
