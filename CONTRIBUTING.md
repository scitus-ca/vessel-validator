# Contributing to vessel-validator

Thank you for your interest in contributing to vessel-validator! This document provides guidelines for contributing to this project.

## Branching Strategy

We use a protected branch workflow to ensure code quality and stability:

```
feature-branch → dev → main
```

### Branch Descriptions

- **`main`**: Production-ready code. All code here has been tested and reviewed.
- **`dev`**: Integration branch for testing features before production.
- **`feature-*`**: Feature branches for new development work.
- **`bugfix-*`**: Branches for bug fixes.
- **`hotfix-*`**: Urgent fixes for production issues.

### Branch Protection Rules

Both `main` and `dev` branches are protected:

✅ **Require pull request reviews before merging**
- At least 1 approval required from repository owner
- Dismiss stale pull request approvals when new commits are pushed

✅ **Require status checks to pass before merging**
- All tests must pass
- Code quality checks must pass

✅ **Require branches to be up to date before merging**

✅ **Do not allow bypassing the above settings**

---

## Development Workflow

### 1. Create a Feature Branch

```bash
# Update your local repository
git checkout dev
git pull origin dev

# Create a new feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

- Write clean, well-documented code
- Follow the existing code style (Black formatting)
- Add tests for new functionality
- Update documentation as needed

### 3. Test Your Changes

```bash
# Activate virtual environment
source venv/bin/activate

# Run tests
pytest tests/ -v

# Check code quality
black vessel_validator/ tests/ examples/ --check
flake8 vessel_validator/ --max-line-length=120 --extend-ignore=E203,W503
mypy vessel_validator/ --ignore-missing-imports

# Run examples
python examples/basic_usage.py
```

### 4. Commit Your Changes

```bash
git add .
git commit -m "Brief description of changes

- Detailed point 1
- Detailed point 2
- Fixes #issue_number (if applicable)"
```

### 5. Push Your Branch

```bash
git push origin feature/your-feature-name
```

### 6. Create Pull Request to `dev`

1. Go to GitHub repository
2. Click "Pull requests" → "New pull request"
3. Set base: `dev` ← compare: `your-feature-branch`
4. Fill in the PR template with:
   - Description of changes
   - Related issues
   - Testing performed
   - Screenshots (if applicable)
5. Request review from repository owner
6. Wait for approval

### 7. Merge to `dev`

- After approval, the PR will be merged to `dev`
- The feature branch can be deleted

### 8. Release to `main`

When ready for production release:

1. Create PR from `dev` to `main`
2. Owner reviews and approves
3. Merge to `main`
4. Create release tag

---

## Code Quality Standards

### Python Style

- Follow PEP 8
- Use Black for code formatting
- Maximum line length: 120 characters
- Full type hints required

### Testing

- Minimum 80% code coverage
- All tests must pass
- Add tests for new features
- Update existing tests when modifying features

### Documentation

- Update README.md for user-facing changes
- Update CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/)
- Add docstrings for all public functions/classes
- Include examples for new features

---

## Pull Request Guidelines

### PR Title Format

```
[Type] Brief description

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation changes
- style: Code style changes (formatting, etc.)
- refactor: Code refactoring
- test: Adding or updating tests
- chore: Maintenance tasks
```

### PR Description Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Related Issues
Fixes #(issue number)

## Testing Performed
- [ ] All existing tests pass
- [ ] Added new tests for new features
- [ ] Tested manually with examples

## Checklist
- [ ] Code follows the project's style guidelines
- [ ] Self-review of code completed
- [ ] Code is well-commented
- [ ] Documentation updated
- [ ] No new warnings generated
- [ ] Tests added/updated
- [ ] CHANGELOG.md updated
```

---

## Commit Message Guidelines

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Example:**
```
feat(mmsi): add support for EPIRB validation

- Added EPIRB MMSI type detection
- Updated MID validation for emergency beacons
- Added 15 new tests for EPIRB validation

Closes #42
```

---

## Setting Up Development Environment

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool

### Setup Steps

```bash
# Clone the repository
git clone git@github.com-scitus:scitus-ca/vessel-validator.git
cd vessel-validator

# Create virtual environment
python3.9 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -e .
pip install pytest pytest-cov black flake8 mypy

# Run tests
pytest tests/ -v

# Run code quality checks
black vessel_validator/ tests/ examples/ --check
flake8 vessel_validator/
mypy vessel_validator/
```

---

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Steps

1. Create release PR from `dev` to `main`
2. Update version in:
   - `pyproject.toml`
   - `setup.py`
   - `vessel_validator/validator.py`
3. Update `CHANGELOG.md`
4. Get approval from owner
5. Merge to `main`
6. Create and push tag:
   ```bash
   git tag -a v0.1.2 -m "Release v0.1.2"
   git push origin v0.1.2
   ```
7. Build and publish to PyPI:
   ```bash
   python -m build
   twine upload dist/*
   ```
8. Create GitHub Release with changelog

---

## Getting Help

- Check existing issues and pull requests
- Create a new issue for bugs or feature requests
- Email: info@scitus.ca
- Repository: https://github.com/scitus-ca/vessel-validator

---

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

---

## License

By contributing to vessel-validator, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to vessel-validator! 🚢⚓
