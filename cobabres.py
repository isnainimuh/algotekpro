import matplotlib.pyplot as plt
plt.title("Algoritma Bresenham")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")


def bresenham(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    gradient = dy/float(dx)

    if gradient > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    p = 2 * dy - dx
    print(f'x = {x}, y = {y}')
    # inisialisasi titik ploting
    x_koordinat = [x]
    y_koordinat = [y]

    for k in range(dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        print(f'x = {x}, y = {y}')
        x_koordinat.append(x)
        y_koordinat.append(y)

    plt.plot(x_koordinat, y_koordinat)
    plt.show()


def main():
    x1 = int(input("Enter the starting point of x: "))
    y1 = int(input("Enter the starting point of y: "))
    x2 = int(input("Enter the end point of x: "))
    y2 = int(input("Enter the end point of y: "))

    bresenham(x1, y1, x2, y2)

main()

