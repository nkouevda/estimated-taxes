from . import constants
from . import model


# See https://www.irs.gov/pub/irs-pdf/p15.pdf
def get_fed_withholding(data):
  allowance = data.fed_allowances * constants.fed.WITHHOLDING_ALLOWANCE[data.year]
  regular_taxable_wages = data.regular_wages + data.adjustments - allowance
  taxable_wages = regular_taxable_wages + data.supplemental_wages

  regular_tax = constants.fed.INCOME_TAX_WITHHOLDING[data.year][data.filing_status].get_tax(
      regular_taxable_wages)
  supplemental_tax = (
      data.supplemental_wages * constants.fed.WITHHOLDING_SUPPLEMENTAL_RATE[data.year])
  tax = regular_tax + supplemental_tax

  return model.WithholdingSummary(taxable_wages, tax)


# See https://www.edd.ca.gov/pdf_pub_ctr/21methb.pdf
def get_ca_withholding(data):
  # The previous year's standard deduction
  deduction = constants.ca.STANDARD_DEDUCTION[data.year - 1][data.filing_status]
  regular_taxable_wages = data.regular_wages + data.adjustments - deduction
  taxable_wages = regular_taxable_wages + data.supplemental_wages

  allowance = data.ca_allowances * constants.ca.WITHHOLDING_ALLOWANCE[data.year]
  regular_tax = constants.ca.INCOME_TAX_WITHHOLDING[data.year][data.filing_status].get_tax(
      regular_taxable_wages) - allowance
  supplemental_tax = data.supplemental_wages * constants.ca.WITHHOLDING_SUPPLEMENTAL_RATE[data.year]
  tax = regular_tax + supplemental_tax

  return model.WithholdingSummary(taxable_wages, tax)


# See https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
def get_fed_tax(data, fed_withheld_tax, ca_withheld_tax):
  state_and_local_taxes = ca_withheld_tax + data.ca_estimated_tax + data.ca_other_payments
  state_and_local_taxes_limit = constants.fed.STATE_TAX_DEDUCTION_LIMIT[data.year]
  itemized_deduction = min(state_and_local_taxes, state_and_local_taxes_limit)
  standard_deduction = constants.fed.STANDARD_DEDUCTION[data.year][data.filing_status]
  deduction = max(itemized_deduction, standard_deduction)
  exemption = constants.fed.PERSONAL_EXEMPTION[data.year]
  taxable_income = data.agi - deduction - exemption

  long_term_taxable_income = max(data.long_term_capital_gains, 0) + data.qualified_dividends
  ltcg_bracket_group = constants.fed.LONG_TERM_CAPITAL_GAINS_TAX[data.year][data.filing_status]
  long_term_tax = ltcg_bracket_group.get_tax(taxable_income) - ltcg_bracket_group.get_tax(
      taxable_income - long_term_taxable_income)

  additional_medicare_tax = constants.fed.ADDITIONAL_MEDICARE_TAX[data.filing_status].get_tax(
      data.medicare_wages)
  net_investment_income_tax = constants.fed.NET_INVESTMENT_INCOME_TAX[data.filing_status].get_tax(
      data.agi, limit=max(data.investment_income, 0))

  # See https://www.irs.gov/pub/irs-pdf/i1116.pdf
  credits = (
      data.dividends_foreign_tax
      if data.dividends_foreign_tax <= constants.fed.FOREIGN_TAX_CREDIT_LIMIT
      else 0)

  total_tax = (
      constants.fed.INCOME_TAX[data.year][data.filing_status].get_tax(
          taxable_income - long_term_taxable_income)
      + long_term_tax
      + additional_medicare_tax
      + net_investment_income_tax
      - credits)

  paid_tax = fed_withheld_tax + data.fed_estimated_tax + additional_medicare_tax

  return model.TaxSummary(taxable_income, total_tax, paid_tax)


# See https://www.ftb.ca.gov/forms/2019/2019-540-booklet.pdf
def get_ca_tax(data, ca_withheld_tax):
  deduction = constants.ca.STANDARD_DEDUCTION[data.year][data.filing_status]
  adjustments = -data.state_tax_refund if data.year <= 2018 else 0
  taxable_income = data.agi + adjustments - deduction

  total_tax = constants.ca.INCOME_TAX[data.year][data.filing_status].get_tax(taxable_income)

  paid_tax = ca_withheld_tax + data.ca_estimated_tax

  return model.TaxSummary(taxable_income, total_tax, paid_tax)
