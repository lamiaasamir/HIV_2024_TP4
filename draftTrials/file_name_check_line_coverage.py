from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
import coverage

# Start code coverage
cov = coverage.Coverage()
cov.start()

# Execute test cases
test_file_name_check()

# Stop code coverage
cov.stop()

# Save coverage data
cov.save()

# Generate line coverage report
cov.report(show_missing=True)
cov.html_report(directory='coverage_html_report')

