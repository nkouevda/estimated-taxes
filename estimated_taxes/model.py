from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Bracket(object):
  min: float
  max: float
  rate: float
  constant: float

  def get_tax(self, taxable_amount):
    return (taxable_amount - self.min) * self.rate + self.constant


@dataclass(frozen=True)
class BracketGroup(object):
  brackets: List[Bracket]

  def get_tax(self, taxable_amount):
    for bracket in self.brackets:
      if bracket.min <= taxable_amount <= bracket.max:
        return bracket.get_tax(taxable_amount)

    raise ValueError(f'Amount out of range: {taxable_amount}')


@dataclass(frozen=True)
class AdditionalTax(object):
  threshold: float
  rate: float

  def get_tax(self, taxable_amount, at_most=None):
    base = max(taxable_amount - self.threshold, 0)

    if at_most is not None and base > at_most:
      base = at_most

    return base * self.rate


@dataclass(frozen=True)
class InputData(object):
  year: int
  fed_allowances: int
  ca_allowances: int
  regular_wages: float = 0
  supplemental_wages: float = 0
  untaxed_wages: float = 0
  k401: float = 0
  other_adjustments: float = 0
  interest: float = 0
  dividends: float = 0
  qualified_dividends: float = 0
  dividends_foreign_tax: float = 0
  long_term_capital_gains: float = 0
  short_term_capital_gains: float = 0
  state_tax_refund: float = 0
  other_income: float = 0
  fed_estimated_tax: float = 0
  ca_estimated_tax: float = 0
  ca_other_payments: float = 0

  def __post_init__(self):
    if self.k401 < 0:
      raise ValueError(f'401(k) value must be nonnegative: {self.k401}')

  @property
  def adjustments(self):
    return self.other_adjustments - self.k401

  @property
  def capital_gains(self):
    return self.long_term_capital_gains + self.short_term_capital_gains

  @property
  def w2_wages(self):
    return self.regular_wages + self.supplemental_wages + self.untaxed_wages + self.adjustments

  @property
  def medicare_wages(self):
    return self.regular_wages + self.supplemental_wages + self.other_adjustments

  @property
  def investment_income(self):
    return self.interest + self.dividends + self.capital_gains

  @property
  def agi(self):
    return self.w2_wages + self.investment_income + self.state_tax_refund + self.other_income


@dataclass(frozen=True)
class WithholdingSummary(object):
  taxable_wages: float
  tax: float

  @property
  def tax_rate(self):
    return self.tax / self.taxable_wages


@dataclass(frozen=True)
class TaxSummary(object):
  taxable_income: float
  theoretical_tax: float
  paid_tax: float

  @property
  def theoretical_tax_rate(self):
    return self.theoretical_tax / self.taxable_income

  @property
  def paid_tax_rate(self):
    return self.paid_tax / self.taxable_income

  @property
  def tax_error(self):
    return self.paid_tax - self.theoretical_tax
