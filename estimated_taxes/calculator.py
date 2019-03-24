from . import ca_constants
from . import fed_constants
from . import model


# See https://www.irs.gov/pub/irs-pdf/p15.pdf
def get_fed_withholding(data):
  allowance = data.fed_allowances * fed_constants.WITHHOLDING_ALLOWANCE[data.year]
  regular_taxable_wages = data.regular_wages + data.adjustments - allowance
  taxable_wages = regular_taxable_wages + data.supplemental_wages

  regular_tax = fed_constants.WITHHOLDING_BRACKETS[data.year].get_tax(regular_taxable_wages)
  supplemental_tax = (
      data.supplemental_wages * fed_constants.WITHHOLDING_SUPPLEMENTAL_RATE[data.year])
  tax = regular_tax + supplemental_tax

  return model.WithholdingSummary(taxable_wages, tax)


# See https://www.edd.ca.gov/pdf_pub_ctr/19methb.pdf
def get_ca_withholding(data):
  # The previous year's standard deduction
  deduction = ca_constants.STANDARD_DEDUCTION[data.year - 1]
  taxable_wages = data.regular_wages + data.supplemental_wages + data.adjustments - deduction

  allowance = data.ca_allowances * ca_constants.WITHHOLDING_ALLOWANCE[data.year]
  tax = ca_constants.WITHHOLDING_BRACKETS[data.year].get_tax(taxable_wages) - allowance

  return model.WithholdingSummary(taxable_wages, tax)


# See https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
def get_fed_tax(data, fed_withheld_tax, ca_withheld_tax):
  state_and_local_taxes = ca_withheld_tax + data.ca_estimated_tax + data.ca_other_payments
  state_and_local_taxes_limit = fed_constants.STATE_TAX_DEDUCTION_LIMIT[data.year]
  itemized_deduction = min(state_and_local_taxes, state_and_local_taxes_limit)
  standard_deduction = fed_constants.STANDARD_DEDUCTION[data.year]
  deduction = max(itemized_deduction, standard_deduction)
  exemption = fed_constants.PERSONAL_EXEMPTION[data.year]
  taxable_income = data.agi - deduction - exemption

  additional_medicare_tax = (
      fed_constants.ADDITIONAL_MEDICARE_TAX[data.year].get_tax(data.medicare_wages))
  net_investment_income_tax = fed_constants.NET_INVESTMENT_INCOME_TAX[data.year].get_tax(
      data.agi, at_most=max(data.investment_income, 0))
  credits = data.dividends_foreign_tax
  theoretical_tax = (
      fed_constants.BRACKETS[data.year].get_tax(taxable_income - data.qualified_dividends)
      + data.qualified_dividends * fed_constants.QUALIFIED_DIVIDENDS_RATE
      + additional_medicare_tax
      + net_investment_income_tax
      - credits)

  paid_tax = fed_withheld_tax + data.fed_estimated_tax + additional_medicare_tax

  return model.TaxSummary(taxable_income, theoretical_tax, paid_tax)


# See https://www.ftb.ca.gov/forms/2018/18_540bk.pdf
def get_ca_tax(data, ca_withheld_tax):
  deduction = ca_constants.STANDARD_DEDUCTION[data.year]
  adjustments = -data.state_tax_refund
  taxable_income = data.agi + adjustments - deduction

  theoretical_tax = ca_constants.BRACKETS[data.year].get_tax(taxable_income)

  paid_tax = ca_withheld_tax + data.ca_estimated_tax

  return model.TaxSummary(taxable_income, theoretical_tax, paid_tax)
