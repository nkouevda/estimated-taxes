from .. import model

"""
Reference documents

- Income tax withholding
  - https://www.edd.ca.gov/pdf_pub_ctr/de44-16.pdf
  - https://www.edd.ca.gov/pdf_pub_ctr/de44-17.pdf
  - https://www.edd.ca.gov/pdf_pub_ctr/de44-18.pdf
  - https://www.edd.ca.gov/pdf_pub_ctr/de44-19.pdf
  - https://www.edd.ca.gov/pdf_pub_ctr/20methb.pdf

- Income tax
  - https://www.ftb.ca.gov/forms/2016/16_540bk.pdf
  - https://www.ftb.ca.gov/forms/2017/17-540-booklet.html
  - (2018 is only available by request)
  - https://www.ftb.ca.gov/forms/2019/2019-540-booklet.pdf
"""

WITHHOLDING_ALLOWANCE = {
    2016: 119.90,
    2017: 122.10,
    2018: 125.40,
    2019: 129.80,
    2020: 134.20,
}

INCOME_TAX_WITHHOLDING = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
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
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
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
        }),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
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
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
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
        }),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
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
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
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
        }),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
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
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
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
        }),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
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
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
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
        }),
    },
}

STANDARD_DEDUCTION = {
    2015: {
        model.FilingStatus.SINGLE: 4044,
        model.FilingStatus.MARRIED: 8088,
    },
    2016: {
        model.FilingStatus.SINGLE: 4129,
        model.FilingStatus.MARRIED: 8258,
    },
    2017: {
        model.FilingStatus.SINGLE: 4236,
        model.FilingStatus.MARRIED: 8472,
    },
    2018: {
        model.FilingStatus.SINGLE: 4401,
        model.FilingStatus.MARRIED: 8802,
    },
    2019: {
        model.FilingStatus.SINGLE: 4537,
        model.FilingStatus.MARRIED: 9074,
    },
    2020: {
        model.FilingStatus.SINGLE: 4601,
        model.FilingStatus.MARRIED: 9202,
    },
}

INCOME_TAX = {
    2016: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.01,
            8015: 0.02,
            19001: 0.04,
            29989: 0.06,
            41629: 0.08,
            52612: 0.093,
            268750: 0.103,
            322499: 0.113,
            537498: 0.123,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.01,
            16030: 0.02,
            38002: 0.04,
            59978: 0.06,
            83258: 0.08,
            105224: 0.093,
            537500: 0.103,
            644998: 0.113,
            1074996: 0.123,
        }),
    },
    2017: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.01,
            8223: 0.02,
            19495: 0.04,
            30769: 0.06,
            42711: 0.08,
            53980: 0.093,
            275738: 0.103,
            330884: 0.113,
            551473: 0.123,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.01,
            16446: 0.02,
            38990: 0.04,
            61538: 0.06,
            85422: 0.08,
            107960: 0.093,
            551476: 0.103,
            661768: 0.113,
            1102946: 0.123,
        }),
    },
    2018: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.01,
            8544: 0.02,
            20255: 0.04,
            31969: 0.06,
            44377: 0.08,
            56085: 0.093,
            286492: 0.103,
            343788: 0.113,
            572980: 0.123,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.01,
            17088: 0.02,
            40510: 0.04,
            63938: 0.06,
            88754: 0.08,
            112170: 0.093,
            572984: 0.103,
            687576: 0.113,
            1145960: 0.123,
        }),
    },
    2019: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.01,
            8809: 0.02,
            20883: 0.04,
            32960: 0.06,
            45753: 0.08,
            57824: 0.093,
            295373: 0.103,
            354445: 0.113,
            590742: 0.123,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.01,
            17618: 0.02,
            41766: 0.04,
            65920: 0.06,
            91506: 0.08,
            115648: 0.093,
            590746: 0.103,
            708890: 0.113,
            1181484: 0.123,
        }),
    },
    2020: {
        model.FilingStatus.SINGLE: model.BracketGroup.from_dict({
            0: 0.01,
            8932: 0.02,
            21175: 0.04,
            33421: 0.06,
            46394: 0.08,
            58634: 0.093,
            299508: 0.103,
            359407: 0.113,
            599012: 0.123,
        }),
        model.FilingStatus.MARRIED: model.BracketGroup.from_dict({
            0: 0.01,
            17864: 0.02,
            42350: 0.04,
            66842: 0.06,
            92788: 0.08,
            117268: 0.093,
            599016: 0.103,
            718814: 0.113,
            1198024: 0.123,
        }),
    },
}
