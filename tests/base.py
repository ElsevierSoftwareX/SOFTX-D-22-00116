# encoding: utf-8

# ------------------------------------------------------------------------
# Copyright 2022 All Histolab Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------

import numpy as np

# ============== IMAGES ==============
IMAGE1_GRAY = np.array(
    [
        [152, 100, 162, 160, 23],
        [160, 113, 31, 126, 36],
        [181, 234, 4, 9, 58],
        [159, 59, 82, 114, 167],
        [125, 176, 150, 191, 44],
    ]
)

IMAGE2_GRAY = np.array(
    [
        [89.04472016, 70.10608259, 233.5658837, 165.17043321, 2.37055166],
        [73.56836436, 222.25117531, 73.54528918, 246.26874863, 201.15243113],
        [55.80077125, 200.49377651, 156.47616081, 28.80584561, 5.66855687],
        [122.93254896, 21.71657872, 49.94170459, 163.93079849, 209.12053187],
        [239.75677754, 171.85187822, 80.00714111, 34.50513061, 11.70897055],
    ]
).astype("float64")

IMAGE3_GRAY_BLACK = np.array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
)

IMAGE4_GRAY_WHITE = np.array(
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
)


IMAGE1_RGB = np.array(
    [
        [[248, 241, 240], [201, 145, 55], [91, 187, 88], [113, 93, 199], [8, 123, 186]],
        [
            [11, 201, 202],
            [130, 216, 185],
            [116, 183, 54],
            [174, 204, 239],
            [106, 48, 246],
        ],
        [[176, 147, 56], [34, 233, 60], [62, 150, 226], [251, 8, 25], [89, 41, 145]],
        [[71, 192, 99], [29, 183, 66], [77, 254, 229], [188, 105, 76], [123, 6, 197]],
        [[220, 196, 145], [59, 245, 92], [91, 19, 131], [95, 7, 24], [116, 149, 50]],
    ]
)


IMAGE2_RGB = np.array(
    [
        [
            [250.46667994, 207.53490467, 214.50399479],
            [21.04824152, 137.53266106, 29.80915812],
            [174.13565183, 156.58288797, 176.23601052],
            [181.26113426, 249.33345871, 36.39709525],
            [170.7239498, 137.48820526, 254.03940111],
        ],
        [
            [180.22111014, 95.89742953, 247.15601891],
            [120.82353667, 100.99475051, 82.14598146],
            [70.24057994, 201.62735452, 104.44351811],
            [191.74630995, 192.5243764, 5.14987911],
            [191.4529353, 64.84790175, 47.05901394],
        ],
        [
            [24.88919567, 160.53598296, 154.92184106],
            [163.71520824, 224.76971613, 148.21094717],
            [38.12550987, 219.02342954, 169.24793629],
            [231.65973804, 38.71138012, 130.88308092],
            [86.67265687, 213.09897821, 78.36342844],
        ],
        [
            [211.56562323, 165.20554453, 35.20783482],
            [16.90764974, 39.77079838, 173.60132559],
            [202.24538944, 90.88829655, 182.74225827],
            [187.79736065, 187.73249091, 24.59227461],
            [192.78231484, 17.2252114, 190.00451876],
        ],
        [
            [87.83519087, 159.23347006, 61.72965162],
            [163.64333465, 71.39544476, 229.84139059],
            [182.36976346, 28.23078029, 107.43467956],
            [147.54101008, 10.90833493, 127.25950459],
            [53.58874852, 183.05132864, 247.22483264],
        ],
    ]
).astype("float64")

IMAGE3_RGB_BLACK = np.array(
    [
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    ]
)

IMAGE4_RGB_WHITE = np.array(
    [
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
    ]
)

IMAGE1_RGBA = np.array(
    [
        [
            [62, 27, 234, 242],
            [139, 243, 82, 177],
            [14, 236, 204, 251],
            [90, 10, 243, 24],
            [216, 168, 218, 172],
        ],
        [
            [216, 99, 169, 80],
            [134, 128, 229, 113],
            [225, 83, 99, 138],
            [42, 101, 254, 111],
            [73, 252, 0, 60],
        ],
        [
            [136, 47, 244, 199],
            [154, 101, 41, 116],
            [158, 249, 118, 7],
            [8, 159, 219, 212],
            [185, 148, 250, 64],
        ],
        [
            [184, 21, 164, 216],
            [179, 184, 216, 176],
            [41, 249, 212, 231],
            [188, 119, 209, 187],
            [121, 64, 0, 138],
        ],
        [
            [166, 117, 188, 211],
            [147, 206, 36, 13],
            [232, 151, 59, 194],
            [215, 119, 145, 93],
            [159, 67, 135, 209],
        ],
    ]
)

IMAGE2_RGBA = np.array(
    [
        [
            [164.38632133, 110.08443323, 116.35063696, 63.13852983],
            [115.10591273, 160.12649525, 90.14258916, 237.29189205],
            [161.06553204, 44.98752726, 134.36657355, 189.63594562],
            [78.09141122, 231.64647257, 225.9347354, 98.98274009],
            [138.75975675, 169.91618712, 152.2341757, 169.89830933],
        ],
        [
            [29.18828919, 170.40268151, 231.91205921, 193.47071228],
            [243.00554155, 237.28344558, 66.19293197, 61.21496589],
            [28.4563456, 135.48313095, 18.23409728, 182.84827665],
            [171.15590649, 73.61945972, 201.51987306, 214.18017119],
            [156.92042535, 240.08793481, 30.20462495, 150.50225248],
        ],
        [
            [77.64230315, 118.27897499, 117.02932548, 238.48101162],
            [71.95878526, 124.26487545, 79.83131311, 67.52016196],
            [179.78590382, 72.91859704, 197.43630509, 54.85463794],
            [27.83210743, 97.01851134, 180.86021085, 162.50834919],
            [173.59266351, 82.92299402, 124.51014511, 34.19710161],
        ],
        [
            [79.70710595, 81.58539001, 162.90909666, 49.13898631],
            [189.36224801, 93.21488083, 182.1533083, 203.34095574],
            [133.54459668, 152.65385565, 2.06067074, 102.33510191],
            [234.45354218, 238.07646876, 213.60772367, 192.68581696],
            [200.36314852, 237.08527865, 163.63627569, 51.89662212],
        ],
        [
            [94.47070123, 249.22406972, 212.39398804, 142.9429469],
            [148.68661296, 52.8758938, 101.6367555, 253.57368287],
            [174.89285059, 175.05038036, 243.40691237, 180.98586835],
            [180.74850939, 239.55713876, 45.9097807, 93.81222997],
            [132.37246546, 47.14983759, 81.30343076, 164.60078272],
        ],
    ]
).astype("float64")

IMAGE3_RGBA_BLACK = np.array(
    [
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    ]
)
IMAGE4_RGBA_WHITE = np.array(
    [
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
        [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
    ]
)

# ============== MASKS ==============

BASE_MASK = np.array([[True, True, False, False], [False, True, False, False]])
BASE_MASK2 = np.array([[True, False, False, False], [True, True, False, False]])
BASE_MASK3 = np.array([True, True, False, False])
BASE_MASK4 = np.array([False, True, True, False])
COMPLEX_MASK = np.array(
    [
        [False, True, True, True, True, True, False, False, True, False],
        [True, True, False, False, True, False, False, False, True, False],
        [True, True, False, False, True, True, False, False, True, True],
        [True, True, True, True, False, True, False, True, True, False],
        [True, False, False, True, False, True, False, True, True, False],
        [False, True, True, False, True, True, True, True, True, True],
        [True, False, True, False, False, True, True, False, True, True],
        [True, True, False, True, True, False, True, True, True, True],
        [False, True, True, True, True, False, True, True, False, False],
        [True, True, False, False, False, True, True, False, True, False],
    ]
)
COMPLEX_MASK2 = np.array(
    [
        [False, True, True, True, True, True, False, False, True, False],
        [True, True, False, False, True, False, False, False, True, False],
        [True, True, False, False, True, True, False, False, True, True],
        [True, True, True, True, False, True, False, False, True, False],
        [True, False, False, True, False, True, False, True, True, False],
        [False, True, True, False, True, True, True, True, True, True],
        [True, False, True, False, False, True, True, False, True, True],
        [True, True, False, True, True, False, True, True, True, True],
        [False, True, True, True, True, False, True, True, False, False],
        [True, True, False, False, False, True, True, False, True, True],
    ]
)
COMPLEX_MASK3 = np.array(
    [
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, True, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
    ]
)
COMPLEX_MASK4 = np.array(
    [
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
        [False, False, False, False, False, True, False, False, False, False],
        [False, False, False, True, True, True, True, False, False, False],
        [False, False, False, True, True, True, True, False, False, False],
        [False, False, True, True, True, True, True, False, False, False],
        [False, False, False, True, True, True, True, False, False, False],
        [False, False, False, False, False, True, False, False, False, False],
        [False, False, False, False, False, True, False, False, False, False],
        [False, False, False, False, False, False, False, False, False, False],
    ]
)
