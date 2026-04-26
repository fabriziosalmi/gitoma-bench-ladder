# Contribution Guidelines

## Getting Started
Clone the repository:
```bash
 git clone https://github.com/your-org/gitoma-bench-ladder.git
```

## Prerequisites
Ensure you have:
- Python 3.x (for benchmarks in `bench/`)
- Go 1.20+ (for `rung-1/` benchmarks)
- Rust 1.70+ (for `rung-0/` benchmarks)
- Node.js 18+ (for JavaScript benchmarks)

## Branching Strategy
Create feature branches:
```bash
 git checkout -b feature/your-improvement
```

## Commit Messages
Use conventional commits:
- `feat`: New functionality
- `fix`: Bug fixes
- `docs`: Documentation changes
- `chore`: Maintenance/

## Pull Request Guidelines
1. Include tests for new functionality
2. Ensure 100% test coverage for modified code
3. Add benchmarks if implementing performance changes
4. Update documentation as needed

## Code Style
Follow language-specific conventions:
- Python: PEP8 (run `flake8`)
- Go: Google Go Style Guide
- Rust: Rustfmt (run `rustfmt --check`)
- JavaScript: ESLint (run `npm run lint`)

## Testing
Run full test suite:
```bash
 npm test && go test ./... && poetry run pytest
```

## Documentation
Update `README.md` and this file when adding new benchmarks or features.

## Code of Conduct
Please maintain a respectful and inclusive community as per our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).