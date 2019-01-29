# initialize variables
name = []
chrn = []
pos = []
mat = []
ref = []
trio1 = {'PB1': [], 'PB2': [], 'egg': []}
trio2 = {'PB1': [], 'PB2': [], 'egg': []}
trio3 = {'PB1': [], 'PB2': [], 'egg': []}
trio4 = {'PB1': [], 'PB2': [], 'egg': []}
# read in the input file and store all variables
with open("F:\\input_data_trios.txt", 'r') as f:
    f.readline()
    for line in f:
        var = line.strip().split()
        name.append(var[0])
        chrn.append(var[1])
        pos.append(var[2])
        mat.append(var[3])
        ref.append(var[6])
        trio1['PB1'].append(var[4])
        trio1['PB2'].append(var[5])
        trio1['egg'].append(var[6])
        trio2['PB1'].append(var[7])
        trio2['PB2'].append(var[8])
        trio2['egg'].append(var[9])
        trio3['PB1'].append(var[10])
        trio3['PB2'].append(var[11])
        trio3['egg'].append(var[12])
        trio4['PB1'].append(var[13])
        trio4['PB2'].append(var[14])
        trio4['egg'].append(var[15])

trios = [trio1, trio2, trio3, trio4]
ctypes = ['PB1', 'PB2', 'egg']
# loop over all trios
for n in range(len(trios)):
    trio = trios[n]
    # loop over every cell in the trio
    for ctype in ctypes:
        # open the file for output
        url = "F:\\output_trio" + str(n + 1) + "_" + ctype + ".bed"
        f = open(url, 'w')

        # initialize variables
        start = end = pos[0]
        old = phase = None
        for i in range(len(pos)):
            # calculate the phase value
            # Only heterozygous maternal SNPs are informative for phasing
            if mat[i] != 'AB':
                phase = -2
            # SNPs that are not called or erroneous heterozygous calls in reference
            elif ref[i] == 'NC' or ref[i] == 'AB' or trio[ctype][i] == 'NC':
                phase = -1
            # SNPs that are in phase with the reference
            elif ref[i] == trio[ctype][i]:
                phase = 1
            # SNPs that are heterozygous
            elif trio[ctype][i] == 'AB':
                phase = 0.5
            # SNPs that are not in phase with the reference
            else:
                phase = 0

            # define the first region
            if old is None:
                if phase == -1:
                    pass
                else:
                    old = phase
            # merge regions with the same phase
            # extend the region if the phase remains or becomes noise
            if phase == old or phase == -1:
                end = pos[i]
            # update the region when phase changes
            else:
                # output phases for maternal hetSNPs
                if old >= 0:
                    f.write("chr1\t" + start + "\t" + end + "\t" + str(old) + "\n")
                start = end = pos[i]
                old = phase
            # output the last region
            if i == len(pos) - 1:
                if old >= 0:
                    f.write("chr1\t" + start + "\t" + end + "\t" + str(old) + "\n")

        f.close()



