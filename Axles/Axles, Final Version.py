import cadquery as cq
from cadquery.selectors import BoxSelector

axle_module_len = L = 3

axle_wid = 4.7 # measured
ridge_wid = 1.8 # measured
module_len = 8.0

base_cylinder = (cq.Workplane("front")
        .circle(2.35).extrude(L * 8.0)
    .faces("<Z")
        .fillet(0.75)
    .faces(">Z")
        .fillet(0.75)
        )
#resulting inner circle 3.2 diameter (2.35 - 0.75)

axle_ridges = (cq.Workplane("front")
        .rect(4.7, 1.8).extrude(L * 8.0)
    .faces("<Z").workplane()
        .rect(1.8, 4.7).extrude(-L * 8.0)
    .edges("|Z")
    .edges(BoxSelector((1.8, 1.8, 0), (-1.8, -1.8, L * 8.0)))
        .fillet(0.65)
        )

my_part = base_cylinder.intersect(axle_ridges)

show_object(my_part)

from cadquery import exporters
exporters.export(my_part, 'Axle 3L, width 4.7, ridge 1.8.stl')