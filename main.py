import os
from PIL import Image

start: int = 10
end: int = 0
size: int = 100
diff: int = 0
new_width: int = 600
directory: str = '/mnt/c/Users/matya/Desktop/home/culture/'
files: str = os.listdir(directory)
histograms = []
files.remove("7e90b0b9b06044d57d4116a84502d95e.png")
files.remove("desktop.ini")


def create_histogram(file: str):
    hist: int = [0] * 256
    img = Image.open(os.path.join(directory, file)
                     ).convert('L').resize((size, size))
    for i in range(size * size):
        pixel = img.getpixel((int(i / size), i % size))
        hist[pixel] += 1
    return hist

if __name__ == "__main__":

    try:
        os.remove("pairs")
    except:
        print("file doesn't exist")

    ll = 0
    for file in files:
        histograms.append(create_histogram(file))
        print(ll)
        ll += 1

    with open("pairs", "x") as f:
        for i in range(start, len(histograms)):
            print(i)
            for j in range(i + 1, len(histograms)):
                diff = 0
                for k in range(255):
                    diff += abs(histograms[i][k] - histograms[j][k])
                # print(f"i: {i}\nj: {j}\ndiff: {diff}\n")
                if diff < 2000:
                    f.write(f"{files[i]},{files[j]};")
                    print("found one")
