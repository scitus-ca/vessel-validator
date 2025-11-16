# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-01-16

### Added
- Added `py.typed` marker file for better type checking support in IDEs and type checkers
- Fixed Pylance type stub warnings

### Changed
- Improved package metadata for type hint support

## [0.1.0] - 2025-01-16

### Added
- Initial beta release of Vessel Validator
- IMO number validation with mathematical check digit verification
- MMSI number validation with MID country code verification
- Support for 8 MMSI types (ship, coast, group, handheld, SAR, AtoN, SART, craft)
- 200+ MID to country mappings
- Batch validation support for both IMO and MMSI numbers
- Comprehensive error messages and warnings
- Type detection and classification for MMSI numbers
- Era estimation for IMO numbers
- Zero external dependencies
- Full type hints (Typing:: Typed)
- MIT License

### Features
- `validate_imo()` - Validate IMO numbers
- `validate_mmsi()` - Validate MMSI numbers
- `VesselIdentifierValidator` class for advanced usage
- Batch validation methods
- Detailed `ValidationResult` with errors, warnings, and info

### Documentation
- Comprehensive README with examples
- API reference documentation
- Usage examples in `/examples`
- Test suite in `/tests`

[0.1.0]: https://github.com/scitus-ca/vessel-validator/releases/tag/v0.1.0
