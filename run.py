#EVOLab2022

DIRECTION_TO_DEGREE = {'N': 0, 'NE': 45, 'E': 90, 'SE': 135, 'S': 180, 'SW': 225, 'W': 270, 'NW': 315}
DEGREE_TO_DIRECTION = {v: k for k, v in DIRECTION_TO_DEGREE.items()}
#DEGREE_TO_DIRECTION  = {0: 'N', 45: 'NE', 90: 'E', 135: 'SE', 180: 'S', 225: 'SW', 270: 'W', 315: 'NW'}


def direction(facing, turn):
    if -1080 > turn or turn > 1080:
        raise ValueError('The parameter should be beetwen -1080 and 1080')

    facing_new = (DIRECTION_TO_DEGREE[facing] + turn) % 360

    return DEGREE_TO_DIRECTION[facing_new]


assert direction('S', 180) == 'N'
assert direction('N', -90) == 'W'
assert direction('W', 225) == 'SE'
assert direction('N', 0) == 'N'
assert direction('NE', -360) == 'NE'
assert direction('E', 720) == 'E'
