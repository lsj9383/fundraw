from skimage import data, filters,io, feature, morphology
import matplotlib.pyplot as plt
import findtraces
import drawtraces

def main(imgpath, sigma, speed):
    img = io.imread(imgpath, as_grey=True)
    img = feature.canny(img, sigma=sigma)
    print("关闭图像窗口后将会开始绘制")
    plt.imshow(img, cmap="gray")
    plt.show()
    traces = findtraces.do(img==False)
    drawtraces.do(traces, img.shape[0], img.shape[1])

if __name__ == '__main__':
    import sys
    if(len(sys.argv) < 2):
        print("缺少参数(fundraw.py <img-path> [<sigma>] [<speed>])")
    else:
        imgpath = sys.argv[1]
        sigma = float(sys.argv[2]) if len(sys.argv)>=3 else 2
        speed = int(sys.argv[3]) if len(sys.argv)>=4 else 10
        main(imgpath=imgpath, sigma=sigma, speed=speed)