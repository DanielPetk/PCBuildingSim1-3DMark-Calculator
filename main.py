import csv

while True:
    try:
        min = int(input("What is the minimum score you need? "))
        break
    except:
        print("Invalid score, try again")

cpufilter = input("Enter CPU Keyword to Filter By (Enter to skip)").strip("\n").strip()
gpufilter = input("Enter GPU Keyword to Filter By (Enter to skip)").strip("\n").strip()


with open("CPUReal.csv", "r") as cpufile, open("GPUReal.csv", "r") as gpufile, open("Results.txt", "w") as newfile:

    cpu_reader = csv.reader(cpufile)
    gpu_reader = csv.reader(gpufile)

    for i in cpu_reader:

        if cpufilter and cpufilter.lower() not in i[0].lower():
            continue

        cpuscore = int(i[2])

        for j in gpu_reader:

            if gpufilter and gpufilter.lower() not in j[0].lower():
                continue

            gpu_score = int(j[2])

            totalscore = (1/((.85/gpu_score) + (.15/cpuscore)))

            if totalscore >= min:
                newfile.write(f"{i[0]}, {j[0]}, {totalscore}\n")

        gpufile.seek(0)
