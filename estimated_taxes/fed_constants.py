from . import model

WITHHOLDING_ALLOWANCE = {
    2016: 4050,
    2017: 4050,
    2018: 4150,
    2019: 4200,
}

WITHHOLDING_BRACKETS = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            2250: 0.10,
            11525: 0.15,
            39900: 0.25,
            93400: 0.28,
            192400: 0.33,
            415600: 0.35,
            417300: 0.396,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.00,
            8550: 0.10,
            27100: 0.15,
            83850: 0.25,
            160450: 0.28,
            240000: 0.33,
            421900: 0.35,
            475500: 0.396,
        }),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            2300: 0.10,
            11625: 0.15,
            40250: 0.25,
            94200: 0.28,
            193950: 0.33,
            419000: 0.35,
            420700: 0.396,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.00,
            8650: 0.10,
            27300: 0.15,
            84550: 0.25,
            161750: 0.28,
            242000: 0.33,
            425350: 0.35,
            479350: 0.396,
        }),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            3700: 0.10,
            13225: 0.12,
            42400: 0.22,
            86200: 0.24,
            161200: 0.32,
            203700: 0.35,
            503700: 0.37,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.00,
            11550: 0.10,
            30600: 0.12,
            88950: 0.22,
            176550: 0.24,
            326550: 0.32,
            411550: 0.35,
            611550: 0.37,
        }),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            3800: 0.10,
            13500: 0.12,
            43275: 0.22,
            88000: 0.24,
            164525: 0.32,
            207900: 0.35,
            514100: 0.37,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.00,
            11800: 0.10,
            31200: 0.12,
            90750: 0.22,
            180200: 0.24,
            333250: 0.32,
            420000: 0.35,
            624150: 0.37,
        }),
    },
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
    2016: {
        model.FilingStatus.SINGLE: 6300,
        model.FilingStatus.MARRIED: 12600,
    },
    2017: {
        model.FilingStatus.SINGLE: 6350,
        model.FilingStatus.MARRIED: 12700,
    },
    2018: {
        model.FilingStatus.SINGLE: 12000,
        model.FilingStatus.MARRIED: 24000,
    },
    2019: {
        model.FilingStatus.SINGLE: 12200,
        model.FilingStatus.MARRIED: 24400,
    },
}

PERSONAL_EXEMPTION = {
    2016: 4050,
    2017: 4050,
    2018: 0,
    2019: 0,
}

BRACKETS = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9275: 0.15,
            37650: 0.25,
            91150: 0.28,
            190150: 0.33,
            413350: 0.35,
            415050: 0.396,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.10,
            18550: 0.15,
            75300: 0.25,
            151900: 0.28,
            231450: 0.33,
            413350: 0.35,
            466950: 0.396,
        }),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9325: 0.15,
            37950: 0.25,
            91900: 0.28,
            191650: 0.33,
            416700: 0.35,
            418400: 0.396,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.10,
            18650: 0.15,
            75900: 0.25,
            153100: 0.28,
            233350: 0.33,
            416700: 0.35,
            470700: 0.396,
        }),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9525: 0.12,
            38700: 0.22,
            82500: 0.24,
            157500: 0.32,
            200000: 0.35,
            500000: 0.37,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.10,
            19050: 0.12,
            77400: 0.22,
            165000: 0.24,
            315000: 0.32,
            400000: 0.35,
            600000: 0.37,
        }),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9700: 0.12,
            39475: 0.22,
            84200: 0.24,
            160725: 0.32,
            204100: 0.35,
            510300: 0.37,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.10,
            19400: 0.12,
            78950: 0.22,
            168400: 0.24,
            321450: 0.32,
            408200: 0.35,
            612350: 0.37,
        }),
    },
}

QUALIFIED_DIVIDENDS_RATE = 0.15

ADDITIONAL_MEDICARE_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.009),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.009),
    },
    2017: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.009),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.009),
    },
    2018: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.009),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.009),
    },
    2019: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.009),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.009),
    },
}

NET_INVESTMENT_INCOME_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.038),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.038),
    },
    2017: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.038),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.038),
    },
    2018: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.038),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.038),
    },
    2019: {
        model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.038),
        model.FilingStatus.MARRIED: model.AdditionalTax(250000, 0.038),
    },
}
