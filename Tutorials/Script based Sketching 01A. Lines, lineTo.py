import cadquery as cq

module_len = 8.0
plate_hgt = 3.2
wall_thickness = 1.5

my_part = (cq.Workplane("front")
                .lineTo(16.0, 0)
                .lineTo(16.0, 8.0)
                .lineTo(8.0, 8.0)
                .lineTo(8.0, 16.0)
                .lineTo(0, 16.0)
                .close().extrude(3.2)
                 )

show_object(my_part)