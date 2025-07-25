"""California tax constants.

These numbers are from the following documents:

- Income tax withholding
  - (2016 is unavailable)
  - (2017 is unavailable)
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-18.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/de44-19.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/20methb.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/21methb.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/22methb.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/23methb.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/24methb.pdf
  - https://edd.ca.gov/siteassets/files/pdf_pub_ctr/25methb.pdf

- Income tax
  - (2016 is only available by request)
  - https://www.ftb.ca.gov/forms/2017/17-540-booklet.html
  - (2018 is only available by request)
  - https://www.ftb.ca.gov/forms/2019/2019-540-booklet.html
  - https://www.ftb.ca.gov/forms/2020/2020-540-booklet.html
  - https://www.ftb.ca.gov/forms/2021/2021-540-booklet.html
  - https://www.ftb.ca.gov/forms/2022/2022-540-booklet.html
  - https://www.ftb.ca.gov/forms/2023/2023-540-booklet.html
  - https://www.ftb.ca.gov/forms/2024/2024-540-booklet.html
"""

from .. import model
from . import util

WITHHOLDING_ALLOWANCE = {
    2016: 119.90,
    2017: 122.10,
    2018: 125.40,
    2019: 129.80,
    2020: 134.20,
    2021: 136.40,
    2022: 141.90,
    2023: 154.00,
    2024: 158.40,
    2025: 163.90,
}

INCOME_TAX_WITHHOLDING = util.copy_single_to_married_separately(
    {
        2016: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    7850: 0.022,
                    18610: 0.044,
                    29372: 0.066,
                    40773: 0.088,
                    51530: 0.1023,
                    263222: 0.1133,
                    315866: 0.1243,
                    526443: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    15700: 0.022,
                    37220: 0.044,
                    58744: 0.066,
                    81546: 0.088,
                    103060: 0.1023,
                    526444: 0.1133,
                    631732: 0.1243,
                    1000000: 0.1353,
                    1052886: 0.1463,
                }
            ),
        },
        2017: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    8015: 0.022,
                    19001: 0.044,
                    29989: 0.066,
                    41629: 0.088,
                    52612: 0.1023,
                    268750: 0.1133,
                    322499: 0.1243,
                    537498: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    16030: 0.022,
                    38002: 0.044,
                    59978: 0.066,
                    83258: 0.088,
                    105224: 0.1023,
                    537500: 0.1133,
                    644998: 0.1243,
                    1000000: 0.1353,
                    1074996: 0.1463,
                }
            ),
        },
        2018: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    8223: 0.022,
                    19495: 0.044,
                    30769: 0.066,
                    42711: 0.088,
                    53980: 0.1023,
                    275738: 0.1133,
                    330884: 0.1243,
                    551473: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    16446: 0.022,
                    38990: 0.044,
                    61538: 0.066,
                    85422: 0.088,
                    107960: 0.1023,
                    551476: 0.1133,
                    661768: 0.1243,
                    1000000: 0.1353,
                    1102946: 0.1463,
                }
            ),
        },
        2019: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    8544: 0.022,
                    20255: 0.044,
                    31969: 0.066,
                    44377: 0.088,
                    56085: 0.1023,
                    286492: 0.1133,
                    343788: 0.1243,
                    572980: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    17088: 0.022,
                    40510: 0.044,
                    63938: 0.066,
                    88754: 0.088,
                    112170: 0.1023,
                    572984: 0.1133,
                    687576: 0.1243,
                    1000000: 0.1353,
                    1145960: 0.1463,
                }
            ),
        },
        2020: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    8809: 0.022,
                    20883: 0.044,
                    32960: 0.066,
                    45753: 0.088,
                    57824: 0.1023,
                    295373: 0.1133,
                    354445: 0.1243,
                    590742: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    17618: 0.022,
                    41766: 0.044,
                    65920: 0.066,
                    91506: 0.088,
                    115648: 0.1023,
                    590746: 0.1133,
                    708890: 0.1243,
                    1000000: 0.1353,
                    1181484: 0.1463,
                }
            ),
        },
        2021: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    8932: 0.022,
                    21175: 0.044,
                    33421: 0.066,
                    46394: 0.088,
                    58634: 0.1023,
                    299508: 0.1133,
                    359407: 0.1243,
                    599012: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    17864: 0.022,
                    42350: 0.044,
                    66842: 0.066,
                    92788: 0.088,
                    117268: 0.1023,
                    599016: 0.1133,
                    718814: 0.1243,
                    1000000: 0.1353,
                    1198024: 0.1463,
                }
            ),
        },
        2022: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    9325: 0.022,
                    22107: 0.044,
                    34892: 0.066,
                    48435: 0.088,
                    61214: 0.1023,
                    312686: 0.1133,
                    375221: 0.1243,
                    625369: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    18650: 0.022,
                    44214: 0.044,
                    69784: 0.066,
                    96870: 0.088,
                    122428: 0.1023,
                    625372: 0.1133,
                    750442: 0.1243,
                    1000000: 0.1353,
                    1250738: 0.1463,
                }
            ),
        },
        2023: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    10099: 0.022,
                    23942: 0.044,
                    37788: 0.066,
                    52455: 0.088,
                    66295: 0.1023,
                    338639: 0.1133,
                    406364: 0.1243,
                    677275: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    20198: 0.022,
                    47884: 0.044,
                    75576: 0.066,
                    104910: 0.088,
                    132590: 0.1023,
                    677278: 0.1133,
                    812728: 0.1243,
                    1000000: 0.1353,
                    1354550: 0.1463,
                }
            ),
        },
        2024: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    10412: 0.022,
                    24684: 0.044,
                    38959: 0.066,
                    54081: 0.088,
                    68350: 0.1023,
                    349137: 0.1133,
                    418961: 0.1243,
                    698271: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    20824: 0.022,
                    49368: 0.044,
                    77918: 0.066,
                    108162: 0.088,
                    136700: 0.1023,
                    698274: 0.1133,
                    837922: 0.1243,
                    1000000: 0.1353,
                    1396542: 0.1463,
                }
            ),
        },
        2025: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.011,
                    10756: 0.022,
                    25499: 0.044,
                    40245: 0.066,
                    55866: 0.088,
                    70606: 0.1023,
                    360659: 0.1133,
                    432787: 0.1243,
                    721314: 0.1353,
                    1000000: 0.1463,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    21512: 0.022,
                    50998: 0.044,
                    80490: 0.066,
                    111732: 0.088,
                    141212: 0.1023,
                    721318: 0.1133,
                    865574: 0.1243,
                    1000000: 0.1353,
                    1442628: 0.1463,
                }
            ),
        },
    }
)

WITHHOLDING_SUPPLEMENTAL_RATE = {
    2016: 0.1023,
    2017: 0.1023,
    2018: 0.1023,
    2019: 0.1023,
    2020: 0.1023,
    2021: 0.1023,
    2022: 0.1023,
    2023: 0.1023,
    2024: 0.1023,
    2025: 0.1023,
}

STANDARD_DEDUCTION = util.copy_single_to_married_separately(
    {
        2015: {
            model.FilingStatus.SINGLE: 4044,
            model.FilingStatus.MARRIED_JOINTLY: 8088,
        },
        2016: {
            model.FilingStatus.SINGLE: 4129,
            model.FilingStatus.MARRIED_JOINTLY: 8258,
        },
        2017: {
            model.FilingStatus.SINGLE: 4236,
            model.FilingStatus.MARRIED_JOINTLY: 8472,
        },
        2018: {
            model.FilingStatus.SINGLE: 4401,
            model.FilingStatus.MARRIED_JOINTLY: 8802,
        },
        2019: {
            model.FilingStatus.SINGLE: 4537,
            model.FilingStatus.MARRIED_JOINTLY: 9074,
        },
        2020: {
            model.FilingStatus.SINGLE: 4601,
            model.FilingStatus.MARRIED_JOINTLY: 9202,
        },
        2021: {
            model.FilingStatus.SINGLE: 4803,
            model.FilingStatus.MARRIED_JOINTLY: 9606,
        },
        2022: {
            model.FilingStatus.SINGLE: 5202,
            model.FilingStatus.MARRIED_JOINTLY: 10404,
        },
        2023: {
            model.FilingStatus.SINGLE: 5363,
            model.FilingStatus.MARRIED_JOINTLY: 10726,
        },
        2024: {
            model.FilingStatus.SINGLE: 5540,
            model.FilingStatus.MARRIED_JOINTLY: 11080,
        },
        # TODO: copied from 2024
        2025: {
            model.FilingStatus.SINGLE: 5540,
            model.FilingStatus.MARRIED_JOINTLY: 11080,
        },
    }
)

INCOME_TAX = util.copy_single_to_married_separately(
    {
        2016: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    8015: 0.02,
                    19001: 0.04,
                    29989: 0.06,
                    41629: 0.08,
                    52612: 0.093,
                    268750: 0.103,
                    322499: 0.113,
                    537498: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    16030: 0.02,
                    38002: 0.04,
                    59978: 0.06,
                    83258: 0.08,
                    105224: 0.093,
                    537500: 0.103,
                    644998: 0.113,
                    1074996: 0.123,
                }
            ),
        },
        2017: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    8223: 0.02,
                    19495: 0.04,
                    30769: 0.06,
                    42711: 0.08,
                    53980: 0.093,
                    275738: 0.103,
                    330884: 0.113,
                    551473: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    16446: 0.02,
                    38990: 0.04,
                    61538: 0.06,
                    85422: 0.08,
                    107960: 0.093,
                    551476: 0.103,
                    661768: 0.113,
                    1102946: 0.123,
                }
            ),
        },
        2018: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    8544: 0.02,
                    20255: 0.04,
                    31969: 0.06,
                    44377: 0.08,
                    56085: 0.093,
                    286492: 0.103,
                    343788: 0.113,
                    572980: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    17088: 0.02,
                    40510: 0.04,
                    63938: 0.06,
                    88754: 0.08,
                    112170: 0.093,
                    572984: 0.103,
                    687576: 0.113,
                    1145960: 0.123,
                }
            ),
        },
        2019: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    8809: 0.02,
                    20883: 0.04,
                    32960: 0.06,
                    45753: 0.08,
                    57824: 0.093,
                    295373: 0.103,
                    354445: 0.113,
                    590742: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    17618: 0.02,
                    41766: 0.04,
                    65920: 0.06,
                    91506: 0.08,
                    115648: 0.093,
                    590746: 0.103,
                    708890: 0.113,
                    1181484: 0.123,
                }
            ),
        },
        2020: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    8932: 0.02,
                    21175: 0.04,
                    33421: 0.06,
                    46394: 0.08,
                    58634: 0.093,
                    299508: 0.103,
                    359407: 0.113,
                    599012: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    17864: 0.02,
                    42350: 0.04,
                    66842: 0.06,
                    92788: 0.08,
                    117268: 0.093,
                    599016: 0.103,
                    718814: 0.113,
                    1198024: 0.123,
                }
            ),
        },
        2021: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    9325: 0.02,
                    22107: 0.04,
                    34892: 0.06,
                    48435: 0.08,
                    61214: 0.093,
                    312686: 0.103,
                    375221: 0.113,
                    625369: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    18650: 0.02,
                    44214: 0.04,
                    69784: 0.06,
                    96870: 0.08,
                    122428: 0.093,
                    625372: 0.103,
                    750442: 0.113,
                    1250738: 0.123,
                }
            ),
        },
        2022: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    10099: 0.02,
                    23942: 0.04,
                    37788: 0.06,
                    52455: 0.08,
                    66295: 0.093,
                    338639: 0.103,
                    406364: 0.113,
                    677275: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    20198: 0.02,
                    47884: 0.04,
                    75576: 0.06,
                    104910: 0.08,
                    132590: 0.093,
                    677278: 0.103,
                    812728: 0.113,
                    1354550: 0.123,
                }
            ),
        },
        2023: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    10412: 0.02,
                    24684: 0.04,
                    38959: 0.06,
                    54081: 0.08,
                    68350: 0.093,
                    349137: 0.103,
                    418961: 0.113,
                    698271: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    20824: 0.02,
                    49368: 0.04,
                    77918: 0.06,
                    108162: 0.08,
                    136700: 0.093,
                    698274: 0.103,
                    837922: 0.113,
                    1396542: 0.123,
                }
            ),
        },
        2024: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    10756: 0.02,
                    25499: 0.04,
                    40245: 0.06,
                    55866: 0.08,
                    70606: 0.093,
                    360659: 0.103,
                    432787: 0.113,
                    721314: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    21512: 0.02,
                    50998: 0.04,
                    80490: 0.06,
                    111732: 0.08,
                    141212: 0.093,
                    721318: 0.103,
                    865574: 0.113,
                    1442628: 0.123,
                }
            ),
        },
        # TODO: copied from 2024
        2025: {
            model.FilingStatus.SINGLE: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    10756: 0.02,
                    25499: 0.04,
                    40245: 0.06,
                    55866: 0.08,
                    70606: 0.093,
                    360659: 0.103,
                    432787: 0.113,
                    721314: 0.123,
                }
            ),
            model.FilingStatus.MARRIED_JOINTLY: model.BracketGroup.from_dict(
                {
                    0: 0.01,
                    21512: 0.02,
                    50998: 0.04,
                    80490: 0.06,
                    111732: 0.08,
                    141212: 0.093,
                    721318: 0.103,
                    865574: 0.113,
                    1442628: 0.123,
                }
            ),
        },
    }
)
