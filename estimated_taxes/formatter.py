def format(data, fed_withholding, ca_withholding, fed_tax, ca_tax):
  return f"""
# General

year: {data.year}
filing status: {data.filing_status.name.lower()}

W-2 wages: {data.w2_wages:.2f}
AGI: {data.agi:.2f}

# Federal

taxable wages: {fed_withholding.taxable_wages:.2f}
estimated withholding: {fed_withholding.tax:.2f} ({100 * fed_withholding.tax_rate:.2f}%)

taxable income: {fed_tax.taxable_income:.2f}
total tax: {fed_tax.total_tax:.2f} ({100 * fed_tax.total_tax_rate:.2f}%)
paid tax: {fed_tax.paid_tax:.2f} ({100 * fed_tax.paid_tax_rate:.2f}%)
error: {fed_tax.tax_error:.2f}

# CA

taxable wages: {ca_withholding.taxable_wages:.2f}
estimated withholding: {ca_withholding.tax:.2f} ({100 * ca_withholding.tax_rate:.2f}%)

taxable income: {ca_tax.taxable_income:.2f}
total tax: {ca_tax.total_tax:.2f} ({100 * ca_tax.total_tax_rate:.2f}%)
paid tax: {ca_tax.paid_tax:.2f} ({100 * ca_tax.paid_tax_rate:.2f}%)
error: {ca_tax.tax_error:.2f}
""".strip()
