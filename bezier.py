import math
from PIL import Image
from PIL import ImageDraw

def binomial_coefficient(n, k):
    if k == 1: return n

    n_factorial = 1
    for x in range(1, n):
        n_factorial += n_factorial * x

    k_factorial = 1
    for x in range(1, k):
        k_factorial += k_factorial * x

    nk_factorial = 1
    for x in range(1, n - k):
        nk_factorial += nk_factorial * x

    return n_factorial/(k_factorial*nk_factorial)

def bernstein(n, i, t):
    return binomial_coefficient(n, i) * math.pow(t, i) * math.pow(1 - t, n - i)

def bezier_curve(points, steps):
    n = len(points) - 1
    result = []

    # calculate curve point for t
    def point(t):
        x = 0
        y = 0
        for i in range(0, n + 1):
            x += points[i][0] * bernstein(n,i,t)
            y += points[i][1] * bernstein(n,i,t)
        return (x, y)

    # steps for t from 0 to 1
    for x in range(0, steps+1):
        t = x * (1.0/steps)
        result.append( point(t) )
    
    return result

img_size = 500
img = Image.new("RGB", (img_size, img_size))
draw = ImageDraw.Draw(img)

draw.rectangle([0,0,img_size, img_size], fill="#fff")

D = [
    bezier_curve([(36, 100), (49, 303), (34,306)], 100),
    bezier_curve([(19, 309), (116, 295), (129,287)], 100),
    bezier_curve([(165, 266), (168, 234), (175,221)], 100),
    bezier_curve([(185, 203), (154, 122), (145,107)], 100),
    bezier_curve([(137, 94), (114, 85), (92, 87)], 100),
    bezier_curve([(77, 88), (30, 91), (15, 102)], 100),
]


for x in D:
    draw.line(x, fill="#000", width=2)

W = [
    bezier_curve([(244, 79), (282, 162),( 278, 154)], 100),
    bezier_curve([(271, 281), (378, 187),( 370, 175)], 100),
    bezier_curve([(362, 163), (420, 224),( 412, 237)], 100),
    bezier_curve([(404, 250), (532, 49),( 524, 62)], 100),


]



for x in W:
    draw.line(x, fill="#000", width=2)

img.show()