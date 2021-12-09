def calc_abc_from_line_2d(x0, y0, x1, y1):
    a = y0 - y1
    b = x1 - x0
    c = x0*y1 - x1*y0
    return a, b, c


def get_line_cross_point(line1, line2):
    # x1y1x2y2
    a0, b0, c0 = calc_abc_from_line_2d(*line1)
    a1, b1, c1 = calc_abc_from_line_2d(*line2)
    D = a0 * b1 - a1 * b0
    if D == 0:
        return None
    x = (b0 * c1 - b1 * c0) / D
    y = (a1 * c0 - a0 * c1) / D
    # print(x, y)
    return x, y


if __name__ == '__main__':
    # x1y1x2y2
    line1 = [114.188770929583, 22.3215158249839, 114.188571504113, 22.3213608393456]
    line2 = [114.1885657624813, 22.32153808827565, 114.188630692262, 22.3214793112661]
    line3 = [114.1885657624813, 22.32153808827565, 114.188685497157, 22.321455610458]
    line4 = [114.1885657624813, 22.32153808827565, 114.188719073593, 22.3214684964372]
    line5 = [114.1885657624813, 22.32153808827565, 114.188740540472, 22.3215114648749]
    cross_pt1 = get_line_cross_point(line1, line2)
    cross_pt2 = get_line_cross_point(line1, line3)
    cross_pt3 = get_line_cross_point(line1, line4)
    cross_pt4 = get_line_cross_point(line1, line5)
import numpy as np
import math
pp1 = np.array([114.188571504113, 22.3213608393456])
pp2 = np.array([114.188770929583, 22.3215158249839])
p1 = np.array(cross_pt1)
p2 = np.array(cross_pt2)
p3 = np.array(cross_pt3)
p4 = np.array(cross_pt4)

diff = pp2-pp1
diff1 = p1-pp1
diff2 = p2-p1
diff3 = p3-p2
diff4 = p4-p3
diff5 = pp2-p4

bili1 = math.hypot(diff1[0], diff1[1])/math.hypot(diff[0], diff[1])
bili2 = math.hypot(diff2[0], diff2[1])/math.hypot(diff[0], diff[1])
bili3 = math.hypot(diff3[0], diff3[1])/math.hypot(diff[0], diff[1])
bili4 = math.hypot(diff4[0], diff4[1])/math.hypot(diff[0], diff[1])
bili5 = math.hypot(diff5[0], diff5[1])/math.hypot(diff[0], diff[1])

