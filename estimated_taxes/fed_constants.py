from . import model

WITHHOLDING_ALLOWANCE = {
    2016: 4050,
    2017: 4050,
    2018: 4150,
    2019: 4200,
}

WITHHOLDING_BRACKETS = {
    2016: model.BracketGroup([
        model.Bracket(0, 2250, 0.10, 0.00),
        model.Bracket(2250, 11525, 0.10, 0.00),
        model.Bracket(11525, 39900, 0.15, 927.50),
        model.Bracket(39900, 93400, 0.25, 5183.75),
        model.Bracket(93400, 192400, 0.28, 18558.75),
        model.Bracket(192400, 415600, 0.33, 46278.75),
        model.Bracket(415600, 417300, 0.35, 119934.75),
        model.Bracket(417300, float('inf'), 0.396, 120529.75),
    ]),
    2017: model.BracketGroup([
        model.Bracket(0, 2300, 0.10, 0.00),
        model.Bracket(2300, 11625, 0.10, 0.00),
        model.Bracket(11625, 40250, 0.15, 932.50),
        model.Bracket(40250, 94200, 0.25, 5226.25),
        model.Bracket(94200, 193950, 0.28, 18713.75),
        model.Bracket(193950, 419000, 0.33, 46643.75),
        model.Bracket(419000, 420700, 0.35, 120910.25),
        model.Bracket(420700, float('inf'), 0.396, 121505.25),
    ]),
    2018: model.BracketGroup([
        model.Bracket(0, 3700, 0.0, 0.00),
        model.Bracket(3700, 13225, 0.10, 0.00),
        model.Bracket(13225, 42400, 0.12, 952.50),
        model.Bracket(42400, 86200, 0.22, 4453.50),
        model.Bracket(86200, 161200, 0.24, 14089.50),
        model.Bracket(161200, 203700, 0.32, 32089.50),
        model.Bracket(203700, 503700, 0.35, 45689.50),
        model.Bracket(503700, float('inf'), 0.37, 150689.50),
    ]),
    2019: model.BracketGroup([
        model.Bracket(0, 3800, 0.0, 0.00),
        model.Bracket(3800, 13500, 0.10, 0.00),
        model.Bracket(13500, 43275, 0.12, 970.50),
        model.Bracket(43275, 88000, 0.22, 4543.00),
        model.Bracket(88000, 164525, 0.24, 14382.50),
        model.Bracket(164525, 207900, 0.32, 32748.50),
        model.Bracket(207900, 514100, 0.35, 46628.50),
        model.Bracket(514100, float('inf'), 0.37, 153798.50),
    ]),
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
    2016: model.BracketGroup([
        model.Bracket(0, 9275, 0.10, 0.00),
        model.Bracket(9275, 37650, 0.15, 927.50),
        model.Bracket(37650, 91150, 0.25, 5183.75),
        model.Bracket(91150, 190150, 0.28, 18558.75),
        model.Bracket(190150, 413350, 0.33, 46278.75),
        model.Bracket(413350, 415050, 0.35, 119934.75),
        model.Bracket(415050, float('inf'), 0.396, 120529.75),
    ]),
    2017: model.BracketGroup([
        model.Bracket(0, 9325, 0.10, 0.00),
        model.Bracket(9325, 37950, 0.15, 932.50),
        model.Bracket(37950, 91900, 0.25, 5226.25),
        model.Bracket(91900, 191650, 0.28, 18713.75),
        model.Bracket(191650, 416700, 0.33, 46643.75),
        model.Bracket(416700, 418400, 0.35, 120910.25),
        model.Bracket(418400, float('inf'), 0.396, 121505.25),
    ]),
    2018: model.BracketGroup([
        model.Bracket(0, 9525, 0.10, 0.00),
        model.Bracket(9525, 38700, 0.12, 952.50),
        model.Bracket(38700, 82500, 0.22, 4453.50),
        model.Bracket(82500, 157500, 0.24, 14089.50),
        model.Bracket(157500, 200000, 0.32, 32089.50),
        model.Bracket(200000, 500000, 0.35, 45689.50),
        model.Bracket(500000, float('inf'), 0.37, 150689.50),
    ]),
    2019: model.BracketGroup([
        model.Bracket(0, 9700, 0.10, 0.00),
        model.Bracket(9700, 39475, 0.12, 970.00),
        model.Bracket(39475, 84200, 0.22, 4543.00),
        model.Bracket(84200, 160725, 0.24, 14382.50),
        model.Bracket(160725, 204100, 0.32, 32748.50),
        model.Bracket(204100, 510300, 0.35, 46628.50),
        model.Bracket(510300, float('inf'), 0.37, 153798.50),
    ]),
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
