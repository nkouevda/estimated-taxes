from . import model

WITHHOLDING_ALLOWANCE = {
    2016: 119.90,
    2017: 122.10,
    2018: 125.40,
    2019: 129.80,
}

WITHHOLDING_BRACKETS = {
    2016: model.BracketGroup([
        model.Bracket(0, 7850, 0.011, 0.00),
        model.Bracket(7850, 18610, 0.022, 86.35),
        model.Bracket(18610, 29372, 0.044, 323.07),
        model.Bracket(29372, 40773, 0.066, 796.60),
        model.Bracket(40773, 51530, 0.088, 1549.07),
        model.Bracket(51530, 263222, 0.1023, 2495.69),
        model.Bracket(263222, 315866, 0.1133, 24151.78),
        model.Bracket(315866, 526443, 0.1243, 30116.35),
        model.Bracket(526443, 1000000, 0.1353, 56291.07),
        model.Bracket(1000000, float('inf'), 0.1463, 120363.33),
    ]),
    2017: model.BracketGroup([
        model.Bracket(0, 8015, 0.011, 0.00),
        model.Bracket(8015, 19001, 0.022, 88.17),
        model.Bracket(19001, 29989, 0.044, 329.86),
        model.Bracket(29989, 41629, 0.066, 813.33),
        model.Bracket(41629, 52612, 0.088, 1581.57),
        model.Bracket(52612, 268750, 0.1023, 2548.07),
        model.Bracket(268750, 322499, 0.1133, 24658.99),
        model.Bracket(322499, 537498, 0.1243, 30748.75),
        model.Bracket(537498, 1000000, 0.1353, 57473.13),
        model.Bracket(1000000, float('inf'), 0.1463, 120049.65),
    ]),
    2018: model.BracketGroup([
        model.Bracket(0, 8223, 0.011, 0.00),
        model.Bracket(8223, 19495, 0.022, 90.45),
        model.Bracket(19495, 30769, 0.044, 338.43),
        model.Bracket(30769, 42711, 0.066, 834.49),
        model.Bracket(42711, 53980, 0.088, 1622.66),
        model.Bracket(53980, 275738, 0.1023, 2614.33),
        model.Bracket(275738, 330884, 0.1133, 25300.17),
        model.Bracket(330884, 551473, 0.1243, 31548.21),
        model.Bracket(551473, 1000000, 0.1353, 58967.42),
        model.Bracket(1000000, float('inf'), 0.1463, 119653.12),
    ]),
    2019: model.BracketGroup([
        model.Bracket(0, 8544, 0.011, 0.00),
        model.Bracket(8544, 20255, 0.022, 93.98),
        model.Bracket(20255, 31969, 0.044, 351.62),
        model.Bracket(31969, 44377, 0.066, 867.04),
        model.Bracket(44377, 56085, 0.088, 1685.97),
        model.Bracket(56085, 286492, 0.1023, 2716.27),
        model.Bracket(286492, 343788, 0.1133, 26286.91),
        model.Bracket(343788, 572980, 0.1243, 32778.55),
        model.Bracket(572980, 1000000, 0.1353, 61267.12),
        model.Bracket(1000000, float('inf'), 0.1463, 119042.93),
    ]),
}

STANDARD_DEDUCTION = {
    2015: 4044,
    2016: 4129,
    2017: 4236,
    2018: 4401,
    # TODO(nkouevda): Update
    2019: 4401,
}

BRACKETS = {
    2016: model.BracketGroup([
        model.Bracket(0, 8015, 0.01, 0.00),
        model.Bracket(8015, 19001, 0.02, 80.15),
        model.Bracket(19001, 29989, 0.04, 299.87),
        model.Bracket(29989, 41629, 0.06, 739.39),
        model.Bracket(41629, 52612, 0.08, 1437.79),
        model.Bracket(52612, 268750, 0.093, 2316.43),
        model.Bracket(268750, 322499, 0.103, 22417.26),
        model.Bracket(322499, 537498, 0.113, 27953.41),
        model.Bracket(537498, float('inf'), 0.123, 52248.30),
    ]),
    2017: model.BracketGroup([
        model.Bracket(0, 8223, 0.01, 0.00),
        model.Bracket(8223, 19495, 0.02, 82.23),
        model.Bracket(19495, 30769, 0.04, 307.67),
        model.Bracket(30769, 42711, 0.06, 758.63),
        model.Bracket(42711, 53980, 0.08, 1475.15),
        model.Bracket(53980, 275738, 0.093, 2376.67),
        model.Bracket(275738, 330884, 0.103, 23000.16),
        model.Bracket(330884, 551473, 0.113, 28680.20),
        model.Bracket(551473, float('inf'), 0.123, 53606.76),
    ]),
    2018: model.BracketGroup([
        model.Bracket(0, 8544, 0.01, 0.00),
        model.Bracket(8544, 20255, 0.02, 85.44),
        model.Bracket(20255, 31969, 0.04, 319.66),
        model.Bracket(31969, 44377, 0.06, 788.22),
        model.Bracket(44377, 56085, 0.08, 1532.70),
        model.Bracket(56085, 286492, 0.093, 2469.34),
        model.Bracket(286492, 343788, 0.103, 23897.19),
        model.Bracket(343788, 572980, 0.113, 29798.68),
        model.Bracket(572980, float('inf'), 0.123, 55697.38),
    ]),
    # TODO(nkouevda): Update
    2019: model.BracketGroup([
        model.Bracket(0, 8544, 0.01, 0.00),
        model.Bracket(8544, 20255, 0.02, 85.44),
        model.Bracket(20255, 31969, 0.04, 319.66),
        model.Bracket(31969, 44377, 0.06, 788.22),
        model.Bracket(44377, 56085, 0.08, 1532.70),
        model.Bracket(56085, 286492, 0.093, 2469.34),
        model.Bracket(286492, 343788, 0.103, 23897.19),
        model.Bracket(343788, 572980, 0.113, 29798.68),
        model.Bracket(572980, float('inf'), 0.123, 55697.38),
    ]),
}
