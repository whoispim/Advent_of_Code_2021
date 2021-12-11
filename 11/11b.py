import time
start_time = time.time()
import numpy as np

def energize(field):
    mask = np.zeros(field.shape, dtype=bool)
    count = 0
    field += 1
    while True:
        nmask = field >= 10
        # print()
        # print(nmask*1)
        if np.array_equal(mask, nmask): #exit process if no new flashes happened
            field[field >= 10] = 0
            return field, count
        count += np.sum(mask != nmask)
        
        pfield = np.pad(field, 1) #pad for processing
        pmask = np.pad(mask, 1)   #pad for processing
        pnmask = np.pad(nmask, 1)
        for i in range(pmask.shape[0]):
            for j in range(pmask.shape[1]):
                if pnmask[i,j] and not pmask[i,j]:
                    pfield[i-1:i+2,j-1:j+2] += 1 #add 1 to 3x3-grid
        field = pfield[1:-1,1:-1]
        mask = nmask
    

dumb = np.genfromtxt("input", dtype="int", delimiter=1)

flashnum = 0
stepnum = 0
while True:
    dumb, newflash = energize(dumb)
    flashnum += newflash
    stepnum += 1
    if np.all(dumb == dumb[0]):
        break

print(F"After {stepnum} steps, all dumbos are flashing in sync and you have been flashed exactly {flashnum} times.")

print()
print("--- %s seconds ---" % (time.time() - start_time))
