"""Federal tax constants.

These numbers are from the following documents:

- Income tax withholding
  - https://www.irs.gov/pub/irs-prior/p15--2016.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2017.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2018.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2019.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2020.pdf
  - https://www.irs.gov/pub/irs-pdf/p15.pdf

- Income tax
  - https://www.irs.gov/pub/irs-prior/i1040gi--2016.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2017.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2018.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2019.pdf
  - https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
"""

from . import util
from .. import model

WITHHOLDING_ALLOWANCE = {
    2016: 4050,
    2017: 4050,
    2018: 4150,
    2019: 4200,
    2020: 4300,
    2021: 4300,
}

INCOME_TAX_WITHHOLDING = util.copy_single_to_married_separately({
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
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
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            3800: 0.10,
            13675: 0.12,
            43925: 0.22,
            89325: 0.24,
            167100: 0.32,
            211150: 0.35,
            522200: 0.37,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.00,
            11900: 0.10,
            31650: 0.12,
            92150: 0.22,
            182950: 0.24,
            338500: 0.32,
            426600: 0.35,
            633950: 0.37,
        }),
    },
    2021: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.00,
            3950: 0.10,
            13900: 0.12,
            44475: 0.22,
            90325: 0.24,
            168875: 0.32,
            213375: 0.35,
            527550: 0.37,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.00,
            12200: 0.10,
            32100: 0.12,
            93250: 0.22,
            184950: 0.24,
            342050: 0.32,
            431050: 0.35,
            640500: 0.37,
        }),
    },
})

WITHHOLDING_SUPPLEMENTAL_RATE = {
    2016: 0.25,
    2017: 0.25,
    2018: 0.22,
    2019: 0.22,
    2020: 0.22,
    2021: 0.22,
}

STATE_TAX_DEDUCTION_LIMIT = {
    2016: float('inf'),
    2017: float('inf'),
    2018: 10000,
    2019: 10000,
    2020: 10000,
    2021: 10000,
}

STANDARD_DEDUCTION = util.copy_single_to_married_separately({
    2016: {
        model.FilingStatus.SINGLE: 6300,
        model.FilingStatus.MARRIED_JOINTLY: 12600,
    },
    2017: {
        model.FilingStatus.SINGLE: 6350,
        model.FilingStatus.MARRIED_JOINTLY: 12700,
    },
    2018: {
        model.FilingStatus.SINGLE: 12000,
        model.FilingStatus.MARRIED_JOINTLY: 24000,
    },
    2019: {
        model.FilingStatus.SINGLE: 12200,
        model.FilingStatus.MARRIED_JOINTLY: 24400,
    },
    2020: {
        model.FilingStatus.SINGLE: 12400,
        model.FilingStatus.MARRIED_JOINTLY: 24800,
    },
    2021: {
        model.FilingStatus.SINGLE: 12550,
        model.FilingStatus.MARRIED_JOINTLY: 25100,
    },
})

PERSONAL_EXEMPTION = {
    2016: 4050,
    2017: 4050,
    2018: 0,
    2019: 0,
    2020: 0,
    2021: 0,
}

FOREIGN_TAX_CREDIT_LIMIT = 300

INCOME_TAX = {
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            18550: 0.15,
            75300: 0.25,
            151900: 0.28,
            231450: 0.33,
            413350: 0.35,
            466950: 0.396,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9275: 0.15,
            37650: 0.25,
            75950: 0.28,
            115725: 0.33,
            206675: 0.35,
            233475: 0.396,
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            18650: 0.15,
            75900: 0.25,
            153100: 0.28,
            233350: 0.33,
            416700: 0.35,
            470700: 0.396,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9325: 0.15,
            37950: 0.25,
            76550: 0.28,
            116675: 0.33,
            208350: 0.35,
            235350: 0.396,
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            19050: 0.12,
            77400: 0.22,
            165000: 0.24,
            315000: 0.32,
            400000: 0.35,
            600000: 0.37,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9525: 0.12,
            38700: 0.22,
            82500: 0.24,
            157500: 0.32,
            200000: 0.35,
            300000: 0.37,
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
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            19400: 0.12,
            78950: 0.22,
            168400: 0.24,
            321450: 0.32,
            408200: 0.35,
            612350: 0.37,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9700: 0.12,
            39475: 0.22,
            84200: 0.24,
            160725: 0.32,
            204100: 0.35,
            306175: 0.37,
        }),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9875: 0.12,
            40125: 0.22,
            85525: 0.24,
            163300: 0.32,
            207350: 0.35,
            518400: 0.37,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            19750: 0.12,
            80250: 0.22,
            171050: 0.24,
            326600: 0.32,
            414700: 0.35,
            622050: 0.37,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9875: 0.12,
            40125: 0.22,
            85525: 0.24,
            163300: 0.32,
            207350: 0.35,
            311025: 0.37,
        }),
    },
    2021: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.10,
            9950: 0.12,
            40525: 0.22,
            86375: 0.24,
            164925: 0.32,
            209425: 0.35,
            523600: 0.37,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.10,
            19900: 0.12,
            81050: 0.22,
            172750: 0.24,
            329850: 0.32,
            418850: 0.35,
            628300: 0.37,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.10,
            9950: 0.12,
            40525: 0.22,
            86375: 0.24,
            164925: 0.32,
            209425: 0.35,
            314150: 0.37,
        }),
    },
}

LONG_TERM_CAPITAL_GAINS_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            37650: 0.15,
            415050: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            75300: 0.15,
            466950: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            37650: 0.15,
            233475: 0.20,
        }),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            37950: 0.15,
            418400: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            75900: 0.15,
            470700: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            37950: 0.15,
            235350: 0.20,
        }),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            38600: 0.15,
            425800: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            77200: 0.15,
            479000: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            38600: 0.15,
            239500: 0.20,
        }),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            39375: 0.15,
            434550: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            78750: 0.15,
            488850: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            39375: 0.15,
            244425: 0.20,
        }),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            40000: 0.15,
            441450: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            80000: 0.15,
            496600: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            40000: 0.15,
            248300: 0.20,
        }),
    },
    2021: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.0,
            40400: 0.15,
            445850: 0.20,
        }),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict({
            0: 0.0,
            80800: 0.15,
            501600: 0.20,
        }),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict({
            0: 0.0,
            40400: 0.15,
            250800: 0.20,
        }),
    },
}

ADDITIONAL_MEDICARE_TAX = {
    model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.009),
    model.FilingStatus.MARRIED_JOINTLY: model.AdditionalTax(250000, 0.009),
    model.FilingStatus.MARRIED_SEPARATELY: model.AdditionalTax(125000, 0.009),
}

NET_INVESTMENT_INCOME_TAX = {
    model.FilingStatus.SINGLE: model.AdditionalTax(200000, 0.038),
    model.FilingStatus.MARRIED_JOINTLY: model.AdditionalTax(250000, 0.038),
    model.FilingStatus.MARRIED_SEPARATELY: model.AdditionalTax(125000, 0.038),
}
