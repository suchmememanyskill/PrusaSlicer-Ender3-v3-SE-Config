import sys
import datetime

filename = sys.argv[1]

with open(filename, 'r') as fp:
    data = fp.readlines()

filament_used_mm = 0
time_s = 0
layer_height = 0
bottom_lines_analyzed_amount = 400

for line in data[-bottom_lines_analyzed_amount:]:
    if line.startswith("; filament used [mm] = "):
        filament_used_mm = float(line[23:])
    if line.startswith("; estimated printing time (normal mode) = "):
        line_times = [x.strip() for x in line[42:].split(" ")]
        for time in line_times:
            if time.endswith("d"):
                time_s += int(time[:-1]) * 3600 * 24
            if time.endswith("h"):
                time_s += int(time[:-1]) * 3600
            elif time.endswith("m"):
                time_s += int(time[:-1]) * 60
            elif time.endswith("s"):
                time_s += int(time[:-1])

    if line.startswith("; layer_height = "):
        layer_height = float(line[17:])

print("Filament used: " + str(filament_used_mm) + "mm")
print("Time: " + str(time_s) + "s")
print("Layer height: " + str(layer_height) + "mm")

extra_data = [
    ";FLAVOR:Marlin",
    f";TIME:{time_s:.2f}",
    f";Filament used:{filament_used_mm/1000:.5f}m",
    f";Layer height:{layer_height}",
    ";generated by https://github.com/suchmememanyskill/PrusaSlicer-Ender3-v3-SE-Config on " + datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d at %H:%M:%S UTC"),
    ";",
    ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
]

with open(filename, 'w') as fp:
    fp.writelines([x + "\n" for x in extra_data])
    fp.writelines(data)
