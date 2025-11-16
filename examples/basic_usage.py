"""Basic usage examples for IMO and MMSI Validator.

This example demonstrates the core functionality of the validator library.
"""

from vessel_validator import validate_imo, validate_mmsi, vessel_validator


def print_separator(title: str):
    """Print a formatted separator."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def example_imo_validation():
    """Demonstrate IMO number validation."""
    print_separator("IMO Number Validation Examples")

    # Example 1: Valid IMO with prefix
    print("1. Valid IMO with prefix:")
    result = validate_imo("IMO 9074729")
    print(f"   Input: 'IMO 9074729'")
    print(f"   Valid: {result.valid}")
    print(f"   Normalized: {result.normalized}")
    print(f"   Check digit: {result.info['check_digit']}")
    print(f"   Era: {result.info.get('estimated_era', 'N/A')}")

    # Example 2: Valid IMO without prefix
    print("\n2. Valid IMO without prefix:")
    result = validate_imo("9176187")
    print(f"   Input: '9176187'")
    print(f"   Valid: {result.valid}")
    print(f"   Normalized: {result.normalized}")
    print(f"   Check digit: {result.info['check_digit']}")

    # Example 3: Invalid IMO (wrong check digit)
    print("\n3. Invalid IMO (wrong check digit):")
    result = validate_imo("9074728")
    print(f"   Input: '9074728'")
    print(f"   Valid: {result.valid}")
    if result.errors:
        print(f"   Errors: {result.errors[0]}")

    # Example 4: Historical vessel
    print("\n4. Historical vessel (pre-1990s):")
    result = validate_imo("1234567")
    print(f"   Input: '1234567'")
    print(f"   Valid: {result.valid}")
    print(f"   Warnings: {result.warnings}")
    print(f"   Era: {result.info.get('estimated_era', 'N/A')}")


def example_mmsi_validation():
    """Demonstrate MMSI number validation."""
    print_separator("MMSI Number Validation Examples")

    # Example 1: Valid ship station MMSI
    print("1. Valid ship station MMSI (US):")
    result = validate_mmsi("366123000")
    print(f"   Input: '366123000'")
    print(f"   Valid: {result.valid}")
    print(f"   Type: {result.info.get('type', 'N/A')}")
    print(f"   Country: {result.info.get('country', 'N/A')}")
    print(f"   MID: {result.info.get('mid', 'N/A')}")

    # Example 2: Valid coast station MMSI
    print("\n2. Valid coast station MMSI (Italy):")
    result = validate_mmsi("002470002")
    print(f"   Input: '002470002'")
    print(f"   Valid: {result.valid}")
    print(f"   Type: {result.info.get('type', 'N/A')}")
    print(f"   Country: {result.info.get('country', 'N/A')}")

    # Example 3: Valid SAR aircraft MMSI
    print("\n3. Valid SAR aircraft MMSI (UK):")
    result = validate_mmsi("111232000")
    print(f"   Input: '111232000'")
    print(f"   Valid: {result.valid}")
    print(f"   Type: {result.info.get('type', 'N/A')}")
    print(f"   Country: {result.info.get('country', 'N/A')}")

    # Example 4: Invalid MMSI (starts with 1)
    print("\n4. Invalid MMSI (starts with 1):")
    result = validate_mmsi("123456789")
    print(f"   Input: '123456789'")
    print(f"   Valid: {result.valid}")
    if result.errors:
        print(f"   Errors: {result.errors[0]}")

    # Example 5: Ship MMSI not ending in 000
    print("\n5. Ship MMSI not ending in 000 (warning):")
    result = validate_mmsi("366123456")
    print(f"   Input: '366123456'")
    print(f"   Valid: {result.valid}")
    if result.warnings:
        print(f"   Warnings: {result.warnings[0]}")


def example_batch_validation():
    """Demonstrate batch validation."""
    print_separator("Batch Validation Examples")

    # IMO batch validation
    print("1. IMO Batch Validation:")
    imo_numbers = ["9074729", "9176187", "8814275", "9074728", "1234567"]
    result = vessel_validator.validate_imo_batch(imo_numbers)

    print(f"   Total IMO numbers: {result['summary']['total']}")
    print(f"   Valid: {result['summary']['valid']}")
    print(f"   Invalid: {result['summary']['invalid']}")
    print(f"   Success rate: {result['summary']['success_rate']}")

    print("\n   Individual results:")
    for item in result["results"]:
        status = "✓" if item["result"].valid else "✗"
        print(f"   {status} {item['imo']}: Valid={item['result'].valid}")

    # MMSI batch validation
    print("\n2. MMSI Batch Validation:")
    mmsi_numbers = ["366123000", "002470002", "111232000", "123456789"]
    result = vessel_validator.validate_mmsi_batch(mmsi_numbers)

    print(f"   Total MMSI numbers: {result['summary']['total']}")
    print(f"   Valid: {result['summary']['valid']}")
    print(f"   Invalid: {result['summary']['invalid']}")
    print(f"   Success rate: {result['summary']['success_rate']}")

    print("\n   Individual results:")
    for item in result["results"]:
        status = "✓" if item["result"].valid else "✗"
        mmsi_type = item["result"].info.get("type", "N/A")
        print(
            f"   {status} {item['mmsi']}: Valid={item['result'].valid}, Type={mmsi_type}"
        )


def example_using_validator_class():
    """Demonstrate using the validator class directly."""
    print_separator("Using VesselIdentifierValidator Class")

    from vessel_validator import VesselIdentifierValidator

    validator = VesselIdentifierValidator()

    # Validate IMO
    print("1. IMO Validation:")
    result = validator.validate_imo("9074729", number_type="ship")
    print(f"   IMO 9074729: {result.valid}")
    print(f"   Check digit info: {result.info['check_digit']}")

    # Validate MMSI with type detection
    print("\n2. MMSI Validation with type detection:")
    result = validator.validate_mmsi("366123000", mmsi_type="auto")
    print(f"   MMSI 366123000: {result.valid}")
    print(f"   Detected type: {result.info['type']}")
    print(f"   Country: {result.info['country']}")

    # Validate MMSI with expected country
    print("\n3. MMSI Validation with expected country:")
    result = validator.validate_mmsi(
        "366123000", expected_country="United States of America"
    )
    print(f"   MMSI 366123000 (expecting USA): {result.valid}")
    print(f"   Warnings: {result.warnings if result.warnings else 'None'}")


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("  IMO and MMSI Validator - Basic Usage Examples")
    print("  Scitus Solutions Ltd.")
    print("=" * 70)

    example_imo_validation()
    example_mmsi_validation()
    example_batch_validation()
    example_using_validator_class()

    print("\n" + "=" * 70)
    print("  Examples completed successfully!")
    print("=" * 70 + "\n")
