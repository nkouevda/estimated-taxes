from . import model

WITHHOLDING_ALLOWANCE = {
    2016: 4050,
    2017: 4050,
    2018: 4150,
    2019: 4200,
}

WITHHOLDING_BRACKETS = {
    2016: model.BracketGroup.from_dict({
        0: 0.00,
        2250: 0.10,
        11525: 0.15,
        39900: 0.25,
        93400: 0.28,
        192400: 0.33,
        415600: 0.35,
        417300: 0.396,
    }),
    2017: model.BracketGroup.from_dict({
        0: 0.00,
        2300: 0.10,
        11625: 0.15,
        40250: 0.25,
        94200: 0.28,
        193950: 0.33,
        419000: 0.35,
        420700: 0.396,
    }),
    2018: model.BracketGroup.from_dict({
        0: 0.00,
        3700: 0.10,
        13225: 0.12,
        42400: 0.22,
        86200: 0.24,
        161200: 0.32,
        203700: 0.35,
        503700: 0.37,
    }),
    2019: model.BracketGroup.from_dict({
        0: 0.00,
        3800: 0.10,
        13500: 0.12,
        43275: 0.22,
        88000: 0.24,
        164525: 0.32,
        207900: 0.35,
        514100: 0.37,
    }),
}

WITHHOLDING_SUPPLEMENTAL_RATE = {
    2016: 0.25,
    2017: 0.25,
    2018: 0.22,
    2019: 0.22,
}

STATE_TAX_DEDUCTION_LIMIT = {
    2016: float('inf'),
    2017: float('inf'),
    2018: 10000,
    2019: 10000,
}

STANDARD_DEDUCTION = {
    2016: 6300,
    2017: 6350,
    2018: 12000,
    2019: 12200,
}

PERSONAL_EXEMPTION = {
    2016: 4050,
    2017: 4050,
    2018: 0,
    2019: 0,
}

BRACKETS = {
    2016: model.BracketGroup.from_dict({
        0: 0.10,
        9275: 0.15,
        37650: 0.25,
        91150: 0.28,
        190150: 0.33,
        413350: 0.35,
        415050: 0.396,
    }),
    2017: model.BracketGroup.from_dict({
        0: 0.10,
        9325: 0.15,
        37950: 0.25,
        91900: 0.28,
        191650: 0.33,
        416700: 0.35,
        418400: 0.396,
    }),
    2018: model.BracketGroup.from_dict({
        0: 0.10,
        9525: 0.12,
        38700: 0.22,
        82500: 0.24,
        157500: 0.32,
        200000: 0.35,
        500000: 0.37,
    }),
    2019: model.BracketGroup.from_dict({
        0: 0.10,
        9700: 0.12,
        39475: 0.22,
        84200: 0.24,
        160725: 0.32,
        204100: 0.35,
        510300: 0.37,
    }),
}

QUALIFIED_DIVIDENDS_RATE = 0.15

ADDITIONAL_MEDICARE_TAX = {
    2016: model.AdditionalTax(200000, 0.009),
    2017: model.AdditionalTax(200000, 0.009),
    2018: model.AdditionalTax(200000, 0.009),
    2019: model.AdditionalTax(200000, 0.009),
}

NET_INVESTMENT_INCOME_TAX = {
    2016: model.AdditionalTax(200000, 0.038),
    2017: model.AdditionalTax(200000, 0.038),
    2018: model.AdditionalTax(200000, 0.038),
    2019: model.AdditionalTax(200000, 0.038),
}
