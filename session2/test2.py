def averg(point):
    result = sum(point)
    return result / len(point)

def grade(x):
    if x >= 8:
        return "hsg"
    elif x >= 6.5:
        return "hstt"
    else:
        return "hstb"


lloyd_point = input("enter lloyd's point: ")
sydney_point = input("enter sydney's point: ")
students = [int(lloyd_point), int(sydney_point)]
m = averg(students)
print("average point is %s" % (m))
y = grade(m)
print(y)