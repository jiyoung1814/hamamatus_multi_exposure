import CreateBlankDic

class RemoveDarkCurrent:

    def __init__(self, merged_data):
        element_dark_current = [0.0000000000000001, -0.00000000003, 0.00003, 116.25]

        self.dark_current_removed_data = CreateBlankDic.createBlankDic(range(0,288))

        # print(merged_data)

        for pixel in range(0, len(merged_data.keys())):
            Intg = merged_data[pixel][1]

            remove_dark_current = merged_data[pixel][0] - (Intg**3 * element_dark_current[0] + Intg**2 * element_dark_current[1] + Intg * element_dark_current[2] + element_dark_current[3])
            self.dark_current_removed_data[pixel] = [remove_dark_current, Intg]
