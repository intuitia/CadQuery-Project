import cadquery as cq

module_len = 8.0
plate_hgt = 3.2
wall_thickness = 1.5

my_part = (cq.Workplane("front")
                .hLine(16.0)
                .vLine(8.0)
                .hLine(-8.0)
                .vLine(8.0)
                .hLine(-8,0)
                .close().extrude(3.2)
                .faces("<Z")
                .shell(-1.5)
                 )

show_object(my_part)