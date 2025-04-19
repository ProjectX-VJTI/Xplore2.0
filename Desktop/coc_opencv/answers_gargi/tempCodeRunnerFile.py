def count_nonw(image):
    nonw = []
    count = 0
    for y in range(thresh.shape[0]):
        for x in range(thresh.shape[1]):
            if thresh[y,x]!=255:
                count+=1
                nonw.append((x,y))
    print(f"Number of non white pixels are {count}")
    return nonw