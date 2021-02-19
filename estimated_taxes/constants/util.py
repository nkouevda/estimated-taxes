from .. import model

# Given a nested structure like the example below, for each year, add a
# MARRIED_SEPARATELY entry with the value copied from the SINGLE entry:
#
#   SOME_TAX = {
#       2016: {
#           model.FilingStatus.SINGLE: SOME_VALUE,
#           model.FilingStatus.MARRIED_JOINTLY: SOME_OTHER_VALUE,
#       },
#       ...
#   }
def copy_single_to_married_separately(year_to_filing_status_to_values):
  for filing_status_to_values in year_to_filing_status_to_values.values():
    filing_status_to_values[model.FilingStatus.MARRIED_SEPARATELY] = \
      filing_status_to_values[model.FilingStatus.SINGLE]
  return year_to_filing_status_to_values
