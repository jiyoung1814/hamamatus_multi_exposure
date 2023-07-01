import CreateBlankDic


class Leveling_data:
    def __init__(self, remove_dark_current_data):
        # element_y_calibration = [0.001381225,0.001417199,0.001416147,0.001587136,0.001610727,0.001691344,0.001539675,0.001636889,0.001768295,0.001943046,0.001958185,0.002117683,0.001990439,0.002033006,0.002099217,0.002180267,0.002250056,0.002185939,0.002199452,0.002250799,0.002387721,0.002341965,0.00255673,0.002485368,0.002407009,0.002618931,0.00266956,0.002599741,0.002671936,0.002722114,0.002743777,0.002824308,0.002963851,0.003040711,0.003056343,0.003151717,0.003184089,0.003165674,0.003346077,0.003378064,0.003364261,0.003494938,0.003517246,0.003612315,0.003658635,0.00382717,0.003874581,0.003967611,0.003889706,0.003979686,0.004013074,0.004087114,0.004309676,0.004321145,0.004289023,0.004359658,0.004495881,0.004428665,0.004652322,0.004675667,0.004840632,0.004775628,0.00485423,0.004925422,0.004918855,0.005028392,0.005128265,0.005121228,0.005294134,0.005131875,0.005220854,0.005271921,0.005289081,0.005308658,0.005392636,0.005374659,0.005259583,0.005361047,0.005370455,0.005220647,0.00521936,0.005249335,0.005253975,0.005167325,0.005314942,0.00520372,0.005225195,0.005186756,0.005250826,0.005252471,0.005181649,0.005222737,0.005198041,0.00526765,0.005284805,0.005335093,0.005233672,0.005227175,0.005301985,0.005255929,0.005326828,0.005373278,0.005393389,0.005425747,0.005394692,0.005461573,0.005467285,0.005480147,0.005578871,0.0055743,0.00565789,0.005684148,0.005730111,0.005790116,0.005836031,0.005913598,0.005939424,0.006031231,0.006013674,0.006106944,0.006145203,0.006246712,0.006217193,0.006363979,0.006370196,0.006426597,0.006499234,0.006583673,0.006629823,0.006669647,0.006770185,0.006778729,0.006835938,0.006927677,0.006964774,0.007012442,0.007118269,0.007092482,0.007179608,0.007250789,0.007293615,0.007333845,0.007399244,0.007372506,0.007385123,0.007389725,0.00740028,0.007518055,0.007520831,0.00749249,0.007467423,0.00750399,0.007524167,0.00757608,0.007569427,0.00760904,0.007532331,0.0075979,0.007583795,0.007675286,0.007666074,0.007647489,0.007730276,0.007726069,0.007742332,0.007744688,0.007849213,0.007810336,0.007879829,0.007906829,0.0079462,0.007939468,0.008006282,0.008009261,0.008075907,0.008035324,0.008128742,0.008161715,0.008191018,0.008136006,0.008221799,0.008202018,0.008284333,0.00827593,0.008260544,0.008311146,0.00829857,0.008396544,0.00840339,0.008477994,0.008479466,0.00848388,0.008549369,0.008560912,0.00855973,0.00866277,0.008732785,0.008743115,0.008789387,0.008840153,0.008880645,0.008983244,0.009033324,0.00912962,0.009103894,0.00916878,0.009211449,0.009266053,0.009297481,0.009301335,0.009312662,0.009366484,0.009427711,0.009398524,0.009428465,0.009466738,0.009463805,0.009471875,0.009454227,0.009490412,0.009529266,0.009525018,0.009561746,0.009568301,0.009546353,0.009549453,0.009607952,0.009616766,0.009595485,0.009620233,0.009633863,0.009692057,0.009691951,0.009745129,0.009795776,0.009778092,0.009803621,0.00979258,0.009873755,0.009851966,0.00991141,0.00995185,0.010010961,0.009993247,0.010014301,0.010023925,0.01002676,0.009990047,0.009986438,0.0099675,0.010028024,0.009993588,0.010006886,0.010014685,0.01005104,0.010055361,0.010059602,0.010096758,0.010092546,0.010136537,0.010122279,0.010212829,0.010198288,0.010237713,0.010267946,0.010342704,0.010339681,0.010366044,0.01042551,0.010413889,0.010458208,0.010475302,0.010519528,0.010576214,0.010588758,0.010619916,0.010620861,0.010693091,0.010657852,0.010705855,0.010751856,0.010781901,0.010806731,0.010812316,0.010915811,0.010911308,0.010989527,0.01102182,0.011105807,0.011172722,0.011159577,0.011275087,0.011298525,0.011369003,0.011372122,0.011513862,0.011557977,0.011620549,0.011680758,0.011733773,0.01176784,0.011886664,0.011930965,0.012007608,0.01207777,0.01212543,0.012217724,0.012265316,0.012300047,0.012443481,0.012502628,0.012548766,0.01266998,0.012721978,0.012787826,0.012870792,0.012928487,0.012999329,0.012988444,0.013119571,0.013224696,0.013262633,0.013346607,0.013437672,0.013529955,0.013632451,0.013692834,0.013794489,0.013823454,0.013907587,0.014043098,0.014130974,0.014182183,0.014269894,0.014350358,0.014420204,0.014480866,0.014640891,0.014639046,0.014763464,0.014795022,0.01490571,0.014973506,0.015055669,0.015171654,0.015236225,0.015368845,0.015356137,0.015535376,0.015625874,0.015735148,0.015853378,0.01597272,0.015977472,0.016217982,0.016237225,0.016353899,0.016382718,0.016546423,0.016640449,0.016750482,0.016808295,0.016899069,0.016920707,0.016998149,0.017148521,0.017193229,0.017286529,0.017397163,0.017503496,0.017607563,0.01773221,0.017809004,0.017956026,0.018120204,0.018247579,0.018349332,0.018531143,0.018678494,0.018805947,0.019013489,0.01910767,0.019238641,0.019467762,0.019692156,0.019787087,0.01997499,0.020241105,0.020297351,0.020508389,0.020720843,0.020827849,0.021002765,0.021156145,0.021357597,0.021476544,0.021634559,0.0219339,0.022022703,0.022237578,0.022382062]

        self.leveling_data = CreateBlankDic.createBlankDic(range(0, 288))

        # print(merged_data)

        for pixel in range(0, len(remove_dark_current_data.keys())):
            Intg = remove_dark_current_data[pixel][1]

            leveling = remove_dark_current_data[pixel][0] / Intg

            self.leveling_data[pixel] = [leveling, Intg]