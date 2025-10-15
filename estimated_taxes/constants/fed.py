"""Federal tax constants.

These numbers are from the following documents:

- Income tax withholding
  - https://www.irs.gov/pub/irs-prior/p15--2016.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2017.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2018.pdf
  - https://www.irs.gov/pub/irs-prior/p15--2019.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2020.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2021.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2022.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2023.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2024.pdf
  - https://www.irs.gov/pub/irs-prior/p15t--2025.pdf
  - https://www.irs.gov/pub/irs-pdf/p15t.pdf

- Income tax
  - https://www.irs.gov/pub/irs-prior/i1040gi--2016.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2017.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2018.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2019.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2020.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2021.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2022.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2023.pdf
  - https://www.irs.gov/pub/irs-prior/i1040gi--2024.pdf
  - https://www.irs.gov/pub/irs-pdf/i1040gi.pdf
"""

from .. import model
from . import util

WITHHOLDING_ALLOWANCE = {
    2016: 4050,
    2017: 4050,
    2018: 4150,
    2019: 4200,
    2020: 4300,
    2021: 4300,
    2022: 4300,
    2023: 4300,
    2024: 4300,
    2025: 4300,
}

INCOME_TAX_WITHHOLDING = util.copy_single_to_married_separately(
    {
        2016: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    2250: 0.10,
                    11525: 0.15,
                    39900: 0.25,
                    93400: 0.28,
                    192400: 0.33,
                    415600: 0.35,
                    417300: 0.396,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    8550: 0.10,
                    27100: 0.15,
                    83850: 0.25,
                    160450: 0.28,
                    240000: 0.33,
                    421900: 0.35,
                    475500: 0.396,
                }
            ),
        },
        2017: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    2300: 0.10,
                    11625: 0.15,
                    40250: 0.25,
                    94200: 0.28,
                    193950: 0.33,
                    419000: 0.35,
                    420700: 0.396,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    8650: 0.10,
                    27300: 0.15,
                    84550: 0.25,
                    161750: 0.28,
                    242000: 0.33,
                    425350: 0.35,
                    479350: 0.396,
                }
            ),
        },
        2018: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    3700: 0.10,
                    13225: 0.12,
                    42400: 0.22,
                    86200: 0.24,
                    161200: 0.32,
                    203700: 0.35,
                    503700: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    11550: 0.10,
                    30600: 0.12,
                    88950: 0.22,
                    176550: 0.24,
                    326550: 0.32,
                    411550: 0.35,
                    611550: 0.37,
                }
            ),
        },
        2019: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    3800: 0.10,
                    13500: 0.12,
                    43275: 0.22,
                    88000: 0.24,
                    164525: 0.32,
                    207900: 0.35,
                    514100: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    11800: 0.10,
                    31200: 0.12,
                    90750: 0.22,
                    180200: 0.24,
                    333250: 0.32,
                    420000: 0.35,
                    624150: 0.37,
                }
            ),
        },
        2020: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    3800: 0.10,
                    13675: 0.12,
                    43925: 0.22,
                    89325: 0.24,
                    167100: 0.32,
                    211150: 0.35,
                    522200: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    11900: 0.10,
                    31650: 0.12,
                    92150: 0.22,
                    182950: 0.24,
                    338500: 0.32,
                    426600: 0.35,
                    633950: 0.37,
                }
            ),
        },
        2021: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    3950: 0.10,
                    13900: 0.12,
                    44475: 0.22,
                    90325: 0.24,
                    168875: 0.32,
                    213375: 0.35,
                    527550: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    12200: 0.10,
                    32100: 0.12,
                    93250: 0.22,
                    184950: 0.24,
                    342050: 0.32,
                    431050: 0.35,
                    640500: 0.37,
                }
            ),
        },
        2022: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    4350: 0.10,
                    14625: 0.12,
                    46125: 0.22,
                    93425: 0.24,
                    174400: 0.32,
                    220300: 0.35,
                    544250: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    13000: 0.10,
                    33550: 0.12,
                    96550: 0.22,
                    191150: 0.24,
                    353100: 0.32,
                    444900: 0.35,
                    660850: 0.37,
                }
            ),
        },
        2023: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    5250: 0.10,
                    16250: 0.12,
                    49975: 0.22,
                    100625: 0.24,
                    187350: 0.32,
                    236500: 0.35,
                    583375: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    14800: 0.10,
                    36800: 0.12,
                    104250: 0.22,
                    205550: 0.24,
                    379000: 0.32,
                    477300: 0.35,
                    708550: 0.37,
                }
            ),
        },
        2024: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    6000: 0.10,
                    17600: 0.12,
                    53150: 0.22,
                    106525: 0.24,
                    197950: 0.32,
                    249725: 0.35,
                    615350: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    16300: 0.10,
                    39500: 0.12,
                    110600: 0.22,
                    217350: 0.24,
                    400200: 0.32,
                    503750: 0.35,
                    747500: 0.37,
                }
            ),
        },
        2025: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    6400: 0.10,
                    18325: 0.12,
                    54875: 0.22,
                    109750: 0.24,
                    203700: 0.32,
                    256925: 0.35,
                    632750: 0.37,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.00,
                    17100: 0.10,
                    40950: 0.12,
                    114050: 0.22,
                    223800: 0.24,
                    411700: 0.32,
                    518150: 0.35,
                    768700: 0.37,
                }
            ),
        },
    }
)

WITHHOLDING_SUPPLEMENTAL_RATE = {
    2016: 0.25,
    2017: 0.25,
    2018: 0.22,
    2019: 0.22,
    2020: 0.22,
    2021: 0.22,
    2022: 0.22,
    2023: 0.22,
    2024: 0.22,
    2025: 0.22,
}

STATE_TAX_DEDUCTION_LIMIT = {
    2016: float("inf"),
    2017: float("inf"),
    2018: 10000,
    2019: 10000,
    2020: 10000,
    2021: 10000,
    2022: 10000,
    2023: 10000,
    2024: 10000,
    2025: 40000,
}

STANDARD_DEDUCTION = util.copy_single_to_married_separately(
    {
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
        2022: {
            model.FilingStatus.SINGLE: 12950,
            model.FilingStatus.MARRIED_JOINTLY: 25900,
        },
        2023: {
            model.FilingStatus.SINGLE: 13850,
            model.FilingStatus.MARRIED_JOINTLY: 27700,
        },
        2024: {
            model.FilingStatus.SINGLE: 14600,
            model.FilingStatus.MARRIED_JOINTLY: 29200,
        },
        2025: {
            model.FilingStatus.SINGLE: 15000,
            model.FilingStatus.MARRIED_JOINTLY: 30000,
        },
    }
)

PERSONAL_EXEMPTION = {
    2016: 4050,
    2017: 4050,
    2018: 0,
    2019: 0,
    2020: 0,
    2021: 0,
    2022: 0,
    2023: 0,
    2024: 0,
    2025: 0,
}

FOREIGN_TAX_CREDIT_LIMIT = 300

INCOME_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9275: 0.15,
                37650: 0.25,
                91150: 0.28,
                190150: 0.33,
                413350: 0.35,
                415050: 0.396,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                18550: 0.15,
                75300: 0.25,
                151900: 0.28,
                231450: 0.33,
                413350: 0.35,
                466950: 0.396,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9275: 0.15,
                37650: 0.25,
                75950: 0.28,
                115725: 0.33,
                206675: 0.35,
                233475: 0.396,
            }
        ),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9325: 0.15,
                37950: 0.25,
                91900: 0.28,
                191650: 0.33,
                416700: 0.35,
                418400: 0.396,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                18650: 0.15,
                75900: 0.25,
                153100: 0.28,
                233350: 0.33,
                416700: 0.35,
                470700: 0.396,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9325: 0.15,
                37950: 0.25,
                76550: 0.28,
                116675: 0.33,
                208350: 0.35,
                235350: 0.396,
            }
        ),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9525: 0.12,
                38700: 0.22,
                82500: 0.24,
                157500: 0.32,
                200000: 0.35,
                500000: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                19050: 0.12,
                77400: 0.22,
                165000: 0.24,
                315000: 0.32,
                400000: 0.35,
                600000: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9525: 0.12,
                38700: 0.22,
                82500: 0.24,
                157500: 0.32,
                200000: 0.35,
                300000: 0.37,
            }
        ),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9700: 0.12,
                39475: 0.22,
                84200: 0.24,
                160725: 0.32,
                204100: 0.35,
                510300: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                19400: 0.12,
                78950: 0.22,
                168400: 0.24,
                321450: 0.32,
                408200: 0.35,
                612350: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9700: 0.12,
                39475: 0.22,
                84200: 0.24,
                160725: 0.32,
                204100: 0.35,
                306175: 0.37,
            }
        ),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9875: 0.12,
                40125: 0.22,
                85525: 0.24,
                163300: 0.32,
                207350: 0.35,
                518400: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                19750: 0.12,
                80250: 0.22,
                171050: 0.24,
                326600: 0.32,
                414700: 0.35,
                622050: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9875: 0.12,
                40125: 0.22,
                85525: 0.24,
                163300: 0.32,
                207350: 0.35,
                311025: 0.37,
            }
        ),
    },
    2021: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9950: 0.12,
                40525: 0.22,
                86375: 0.24,
                164925: 0.32,
                209425: 0.35,
                523600: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                19900: 0.12,
                81050: 0.22,
                172750: 0.24,
                329850: 0.32,
                418850: 0.35,
                628300: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                9950: 0.12,
                40525: 0.22,
                86375: 0.24,
                164925: 0.32,
                209425: 0.35,
                314150: 0.37,
            }
        ),
    },
    2022: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                10275: 0.12,
                41775: 0.22,
                89075: 0.24,
                170050: 0.32,
                215950: 0.35,
                539900: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                20550: 0.12,
                83550: 0.22,
                178150: 0.24,
                340100: 0.32,
                431900: 0.35,
                647850: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                10275: 0.12,
                41775: 0.22,
                89075: 0.24,
                170050: 0.32,
                215950: 0.35,
                323925: 0.37,
            }
        ),
    },
    2023: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11000: 0.12,
                44725: 0.22,
                95375: 0.24,
                182100: 0.32,
                231250: 0.35,
                578125: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                22000: 0.12,
                89450: 0.22,
                190750: 0.24,
                364200: 0.32,
                462500: 0.35,
                693750: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11000: 0.12,
                44725: 0.22,
                95375: 0.24,
                182100: 0.32,
                231250: 0.35,
                346875: 0.37,
            }
        ),
    },
    2024: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11600: 0.12,
                47150: 0.22,
                100525: 0.24,
                191950: 0.32,
                243725: 0.35,
                609350: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                23200: 0.12,
                94300: 0.22,
                201050: 0.24,
                383900: 0.32,
                487450: 0.35,
                731200: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11600: 0.12,
                47150: 0.22,
                100525: 0.24,
                191950: 0.32,
                243725: 0.35,
                365600: 0.37,
            }
        ),
    },
    2025: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11925: 0.12,
                48475: 0.22,
                103350: 0.24,
                197300: 0.32,
                250525: 0.35,
                626350: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                23850: 0.12,
                96950: 0.22,
                206700: 0.24,
                394600: 0.32,
                501050: 0.35,
                751600: 0.37,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.10,
                11925: 0.12,
                48475: 0.22,
                103350: 0.24,
                197300: 0.32,
                250525: 0.35,
                375800: 0.37,
            }
        ),
    },
}

LONG_TERM_CAPITAL_GAINS_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                37650: 0.15,
                415050: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                75300: 0.15,
                466950: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                37650: 0.15,
                233475: 0.20,
            }
        ),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                37950: 0.15,
                418400: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                75900: 0.15,
                470700: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                37950: 0.15,
                235350: 0.20,
            }
        ),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                38600: 0.15,
                425800: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                77200: 0.15,
                479000: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                38600: 0.15,
                239500: 0.20,
            }
        ),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                39375: 0.15,
                434550: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                78750: 0.15,
                488850: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                39375: 0.15,
                244425: 0.20,
            }
        ),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                40000: 0.15,
                441450: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                80000: 0.15,
                496600: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                40000: 0.15,
                248300: 0.20,
            }
        ),
    },
    2021: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                40400: 0.15,
                445850: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                80800: 0.15,
                501600: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                40400: 0.15,
                250800: 0.20,
            }
        ),
    },
    2022: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                41675: 0.15,
                459750: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                83350: 0.15,
                517200: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                41675: 0.15,
                258600: 0.20,
            }
        ),
    },
    2023: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                44625: 0.15,
                492300: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                89250: 0.15,
                553850: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                44625: 0.15,
                276900: 0.20,
            }
        ),
    },
    2024: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                47025: 0.15,
                518900: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                94050: 0.15,
                583750: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                47025: 0.15,
                291850: 0.20,
            }
        ),
    },
    2025: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
            {
                0: 0.0,
                48350: 0.15,
                533400: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                96700: 0.15,
                600050: 0.20,
            }
        ),
        model.FilingStatus.MARRIED_SEPARATELY: model.BracketGroup.from_dict(
            {
                0: 0.0,
                48350: 0.15,
                300000: 0.20,
            }
        ),
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
