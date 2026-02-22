---
name: postman-collection-management
description: Create and manage Postman collections for API testing in the healthcare automation project
---

# Postman Collection Management Skill

## Purpose
Guide the creation, management, and troubleshooting of Postman collections generated from the healthcare test-case JSON files.

## When to Use
- Setting up new Postman collections
- Troubleshooting collection generation issues
- Optimizing API testing workflows
- Managing collection configurations

## Collection Generation Process

### 1. Basic Collection Generation
```bash
# Generate collection for specific model
python main_processor.py --wgs_csbd --CSBDTS01

# Generate without Postman collections
python main_processor.py --wgs_csbd --CSBDTS01 --no-postman

# Batch generate for all models
python main_processor.py --all
```

### 2. Collection Structure
Generated collections follow this structure:
```
postman_collections/[Category]/
├── Collection_Name.json
├── environment.json (if applicable)
└── documentation/
```

### 3. Collection Features
- **Request Organization**: Grouped by test case categories
- **Environment Variables**: Auto-generated for dynamic values
- **Test Scripts**: Automated response validation
- **Documentation**: Auto-generated from JSON structure

## Configuration Options

### Environment Variables
- `ENABLE_REPORT_GENERATION` - Controls collection reporting
- Custom headers and authentication settings
- Base URLs and endpoint configurations

### Collection Settings
- Request timeouts
- Retry policies
- Response validation rules
- Test data management

## Troubleshooting Common Issues

### Issue: Collections not generated
**Check:**
- Postman generation not disabled with `--no-postman`
- `postman_generator.py` exists and is accessible
- Output directory permissions

### Issue: Invalid collection format
**Solutions:**
- Verify source JSON structure
- Check for malformed test case files
- Review collection generation logs

### Issue: Missing environment variables
**Steps:**
1. Check `postman_generator.py` for variable definitions
2. Verify environment file generation
3. Manually add missing variables if needed

## Best Practices

### 1. Collection Organization
- Use descriptive collection names
- Group related test cases together
- Maintain consistent naming conventions

### 2. Environment Management
- Separate environments for different stages
- Use variable inheritance effectively
- Document environment variable purposes

### 3. Test Script Optimization
- Keep test scripts modular
- Use reusable functions
- Implement proper error handling

### 4. Documentation
- Document collection purposes
- Include setup instructions
- Provide usage examples

## Advanced Features

### 1. Dynamic Data Handling
- Random data generation for WGS_CSBD models
- KEY_CHK_DCN_NBR generation (11-digit random)
- Header/footer transformations

### 2. Batch Operations
- Multi-collection generation
- Cross-collection dependencies
- Bulk environment updates

### 3. Integration Testing
- End-to-end workflow testing
- Cross-system validation
- Performance testing integration

## Files Involved
- `postman_generator.py` - Core collection generation logic
- `postman_cli.py` - Command-line interface for Postman operations
- `postman_collections/` - Generated collection output directory
- `reports/Collection_Reports/` - Generation reports and statistics

## Commands and Utilities

```bash
# Generate with specific configuration
python postman_generator.py --config custom_config.json

# Validate existing collections
python postman_cli.py --validate --collection path/to/collection.json

# Export collection documentation
python postman_cli.py --export-docs --collection path/to/collection.json

# Batch update collections
python postman_cli.py --batch-update --source-dir source_folder/
```

## Integration with CI/CD
- Automated collection generation in pipelines
- Collection versioning and deployment
- Integration with testing frameworks
- Automated collection validation
