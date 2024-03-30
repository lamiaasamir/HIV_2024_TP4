from poly_llm.to_test.file_name_check import test_file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
import coverage

# Start code coverage with branch coverage enabled
cov = coverage.Coverage(branch=True)
cov.start()

# Execute test cases
test_file_name_check()

# Stop code coverage
cov.stop()

# Save coverage data
cov.save()

# Generate branch coverage report
cov.report()
cov.html_report(directory='branch_coverage_html_report')


