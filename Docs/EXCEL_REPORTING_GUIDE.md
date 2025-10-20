# Excel Reporting Guide

## Overview

The JSON renaming system now includes comprehensive Excel reporting functionality that tracks timing information for all operations. This feature automatically generates detailed Excel reports with timing data for file renaming and Postman collection generation operations.

## Features

### Automatic Timing Tracking
- **Naming Convention Time**: Tracks time taken for JSON file renaming operations
- **Postman Collection Time**: Tracks time taken for Postman collection generation
- **Total Time**: Sum of both operations
- **Average Time**: Average time per operation

### Excel Report Columns
1. **TC#ID** - Test Case ID extracted from directory names (e.g., TS_01, TS_47, TS_139)
2. **Model LOB** - Line of Business (WGS_CSBD, GBDF_MCR, GBDF_GRS)
3. **Model Name** - Model name (Covid, Multiple E&M Same day, Laterality Policy, etc.)
4. **Edit ID** - Edit identifier (e.g., RULEEM000001, RULEEMSD000002, RULELATE000001)
5. **EOB Code** - EOB code (e.g., W04, v04, 00W17, v09)
6. **Naming Convention Time (ms)** - Time taken for file renaming
7. **Postman Collection Time (ms)** - Time taken for Postman collection generation
8. **Total Time (ms)** - Sum of naming convention and Postman collection times
9. **Average Time (ms)** - Average time per operation
10. **Timestamp** - When the operation was performed
11. **Status** - Operation status (Success, Failed, etc.)

### Report Features
- **Professional Formatting**: Headers, borders, and color coding
- **Summary Statistics Sheet**: Totals, averages, and breakdowns
- **Model Breakdown**: Count of records by model type
- **Status Breakdown**: Count of records by status
- **Auto-sizing Columns**: Optimal column widths for readability

## Usage

### Automatic Generation
Excel reports are automatically generated when using the main processor:

```bash
# Single model processing
python main_processor.py --wgs_csbd --TS01
python main_processor.py --gbdf_mcr --TS47
python main_processor.py --gbdf_grs --TS139

# Batch processing
python main_processor.py --wgs_csbd --all
python main_processor.py --gbdf_mcr --all
python main_processor.py --gbdf_grs --all
```

### Manual Testing
Test the Excel reporting functionality:

```bash
# Test the Excel report generator
python excel_report_generator.py

# Test integration
python test_timing_integration.py
```

## Report Output

### File Locations
- **Excel Reports**: `reports/JSON_Renaming_Timing_Report_YYYYMMDD_HHMMSS.xlsx`
- **CSV Reports**: `reports/JSON_Renaming_Timing_Report_YYYYMMDD_HHMMSS.csv`

### Report Structure

#### Main Sheet: "Timing Report"
Contains all timing data with the following columns:
- TC#ID, Model LOB, Model Name, Edit ID, EOB Code
- Naming Convention Time (ms)
- Postman Collection Time (ms)
- Total Time (ms), Average Time (ms)
- Timestamp, Status

#### Summary Sheet: "Summary Statistics"
Contains comprehensive statistics:
- Total Records
- Total Naming Convention Time (ms)
- Total Postman Collection Time (ms)
- Total Time (ms)
- Average Naming Convention Time (ms)
- Average Postman Collection Time (ms)
- Average Total Time (ms)
- Model Breakdown (count by model type)
- Status Breakdown (count by status)

## Integration Details

### Timing Tracking Integration
The timing tracking is integrated into the main processing flow:

1. **Initialization**: Timing trackers are created at the start of operations
2. **Naming Convention Timing**: Tracks file renaming and transformation operations
3. **Postman Collection Timing**: Tracks Postman collection generation
4. **Record Creation**: Timing data is automatically added to the Excel reporter
5. **Report Generation**: Excel reports are generated at the end of processing

### Code Integration Points
- `main_processor.py`: Main timing integration
- `excel_report_generator.py`: Core reporting functionality
- `test_timing_integration.py`: Testing and demonstration

## Dependencies

### Required Packages
```bash
pip install pandas>=1.5.0
pip install openpyxl>=3.0.0
```

### Installation
```bash
pip install -r requirements.txt
```

## Example Output

### Console Output
```
[TIMING] Naming convention operations completed in 150.50ms
[TIMING] Postman collection generation completed in 75.20ms
[TIMING] Added timing record: TS_01_12345 - WGS_CSBD - Total: 225.70ms

============================================================
GENERATING EXCEL TIMING REPORT
============================================================
Excel timing report generated: reports\JSON_Renaming_Timing_Report_20251016_082415.xlsx

TIMING SUMMARY:
  Total Records: 3
  Total Naming Time: 531.50ms
  Total Postman Time: 265.80ms
  Total Time: 797.30ms
  Average Time: 265.77ms
  Model LOBs: WGS_CSBD, GBDF_MCR, GBDF_GRS
  Model Names: Covid, Multiple E&M Same day, Laterality Policy
```

### Excel Report Sample
| TC#ID | Model LOB | Model Name | Edit ID | EOB Code | Naming Convention Time (ms) | Postman Collection Time (ms) | Total Time (ms) | Average Time (ms) | Timestamp | Status |
|-------|-----------|------------|---------|----------|----------------------------|------------------------------|-----------------|-------------------|-----------|--------|
| TS_01 | WGS_CSBD | Covid | RULEEM000001 | W04 | 150.50 | 75.20 | 225.70 | 112.85 | 2025-10-16 08:24:15 | Success |
| TS_47 | GBDF_MCR | Covid | RULEEM000001 | v04 | 200.30 | 100.10 | 300.40 | 150.20 | 2025-10-16 08:24:16 | Success |
| TS_139 | GBDF_GRS | Multiple E&M Same day | RULEEMSD000002 | v09 | 180.70 | 90.50 | 271.20 | 135.60 | 2025-10-16 08:24:17 | Success |

## Benefits

### Performance Monitoring
- Track performance of different operations
- Identify bottlenecks in processing
- Monitor improvements over time

### Quality Assurance
- Verify all operations completed successfully
- Track processing times for different models
- Generate audit trails for compliance

### Reporting and Analysis
- Professional Excel reports for stakeholders
- Detailed timing breakdowns for analysis
- Historical data for trend analysis

## Troubleshooting

### Common Issues
1. **Missing Dependencies**: Install required packages with `pip install -r requirements.txt`
2. **Permission Errors**: Ensure write permissions to the `reports` directory
3. **Encoding Issues**: Reports are generated with UTF-8 encoding

### Debug Mode
Enable detailed timing output by checking console messages:
- `[TIMING]` messages show timing information
- `[SUCCESS]` messages confirm report generation
- `[ERROR]` messages indicate issues

## Future Enhancements

### Planned Features
- Real-time timing dashboard
- Historical trend analysis
- Performance benchmarking
- Custom report templates
- Email report distribution

### Extensibility
The Excel reporting system is designed to be extensible:
- Add new timing metrics
- Customize report formats
- Integrate with external systems
- Add visualization components

## Support

For issues or questions regarding the Excel reporting functionality:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Test with the provided test scripts
4. Review the integration points in the code

The Excel reporting system provides comprehensive timing analysis for all JSON renaming operations, enabling better performance monitoring and quality assurance.
