"""Clearance test: one peg and a strip of holes, each a little bigger than the peg.

Print this first (about 15 minutes, 0.4 nozzle, PLA). The tightest hole the peg
slides into is the clearance to use for every fit you design on this printer.

Run:  python clearance_test.py
Out:  clearance_test.stl and clearance_test.step in this folder.
All sizes are in millimeters.
"""
from pathlib import Path

from build123d import Box, Cylinder, Location, Pos, Text, export_step, export_stl, extrude

PEG_D = 8.0          # peg diameter
PEG_H = 12.0         # peg height
GAPS = [0.1, 0.2, 0.3, 0.4]   # extra room per side, in mm
STRIP_T = 5.0        # strip thickness
PITCH = 16.0         # distance between hole centers

# Strip with one hole per gap, holes go straight through.
width = PITCH * len(GAPS)
strip = Box(width, 24, STRIP_T)
strip = Pos(0, 0, STRIP_T / 2) * strip
for i, gap in enumerate(GAPS):
    x = -width / 2 + PITCH * (i + 0.5)
    hole = Cylinder(PEG_D / 2 + gap, STRIP_T * 3)
    strip -= Pos(x, 3, STRIP_T / 2) * hole
    # Engrave the gap value under each hole so you can read it after printing.
    label = extrude(Text(f"{gap:.1f}", font_size=7), amount=0.6)
    strip -= Location((x, -7, STRIP_T - 0.6)) * label

# Peg printed standing up, next to the strip.
peg = Pos(0, 22, PEG_H / 2) * Cylinder(PEG_D / 2, PEG_H)

part = strip + peg
out = Path(__file__).with_suffix("")
export_stl(part, f"{out}.stl")
export_step(part, f"{out}.step")
bb = part.bounding_box()
print(f"wrote {out}.stl  size {bb.size.X:.1f} x {bb.size.Y:.1f} x {bb.size.Z:.1f} mm")
