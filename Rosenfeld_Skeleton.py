import copy
import numpy as np


class RosenfeldSkeleton(object):

    def __init__(self, binary_img):
        self.img = binary_img

    def skeleton(self):
        img = np.pad(self.img, (5, 5), mode='edge')
        heigh, width = img.shape
        img_temp = copy.deepcopy(img)
        # 4邻域 北南东西
        D4_y = [-1, 1, 0, 0]
        D4_x = [0, 0, 1, -1]
        step = 0
        while 1:
            ifEnd = False
            for i in range(4):
                # print('step...')
                step += 1
                img = copy.deepcopy(img_temp)
                img_temp = copy.deepcopy(img)
                for y in range(1, heigh - 1):
                    for x in range(1, width - 1):
                        if img[y][x] == 0 or img[y + D4_y[i]][x + D4_x[i]] > 0:
                            continue
                        is8simple, adjsum = self.distinguish(img, y, x)
                        if adjsum != 1 and adjsum != 0 and is8simple == 1:
                            img_temp[y][x] = 0
                            ifEnd = True
                # cv2.imwrite('sss'+str(step)+'.tif', img_temp*255)
            if not ifEnd:
                break
        return img[5:-5, 5:-5]*255

    @staticmethod
    def distinguish(img, y, x):
        p2 = img[y - 1][x]
        p3 = img[y - 1][x + 1]
        p4 = img[y][x + 1]
        p5 = img[y + 1][x + 1]
        p6 = img[y + 1][x]
        p7 = img[y + 1][x - 1]
        p8 = img[y][x - 1]
        p9 = img[y - 1][x - 1]

        is8simple = 1
        if p2 == 0 and p6 == 0:
            if (p9 == 1 or p8 == 1 or p7 == 1) and (p3 == 1 or p4 == 1 or p5 == 1):
                is8simple = 0
        if p4 == 0 and p8 == 0:
            if (p9 == 1 or p2 == 1 or p3 == 1) and (p7 == 1 or p6 == 1 or p5 == 1):
                is8simple = 0
        if p2 == 0 and p4 == 0:
            if (p3 == 1) and (p5 == 1 or p6 == 1 or p7 == 1 or p8 == 1 or p9 == 1):
                is8simple = 0
        if p4 == 0 and p6 == 0:
            if (p5 == 1) and (p7 == 1 or p8 == 1 or p9 == 1 or p2 == 1 or p3 == 1):
                is8simple = 0
        if p6 == 0 and p8 == 0:
            if (p7 == 1) and (p9 == 1 or p2 == 1 or p3 == 1 or p4 == 1 or p5 == 1):
                is8simple = 0
        if p8 == 0 and p2 == 0:
            if (p9 == 1) and (p3 == 1 or p4 == 1 or p5 == 1 or p6 == 1 or p7 == 1):
                is8simple = 0

        adjsum = sum([p2, p3, p4, p5, p6, p7, p8, p9])

        return is8simple, adjsum


if __name__ == '__main__':
    # 调用方法
    # img_skeleton = RosenfeldSkeleton(binary_img=img).skeleton()
    pass