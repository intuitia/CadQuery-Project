import cadquery as cq

module_len = 8.0
plate_hgt = 3.2
towball_rad = 2.4
cylinder_rad = 1.6

my_part = (cq.Workplane("XY").box(16.0, 16.0, 3.2)
           .faces(">Y").workplane().cylinder(16.0, 1.6)
           .faces(">Z").workplane().sphere(2.4)
           )

# run through "front", "XY", and "YZ" for box and cylinder

# cylinder method used with radius measure

# sphere method used with radius measure

show_object(my_part)