import cadquery as cq

module_len = L = 8.0 # the nominal dimention
wall_thickness = LU = 1.6 # as in the LEGO Unit
plate_hgt = 3.2

outer_corners = [(0, 0),
                 (1.5 * L, 0),
                 (1.5 * L, 2 * L),
                 (0.5 * L, 2 * L),
                 (0.5 * L, L),
                 (0, L)]

# we have written the coordinates in terms of the model length 'L'           

first_solid = (cq.Workplane("front")
                .polyline(outer_corners)
                .mirrorY()
                .extrude(3.2)
                 )

                .faces("<Z")
                .shell(-2.0)

inner_corners = [(0, LU),
                 (1.5 * L - LU, LU),
                 (1.5 * L - LU, 2 * L - LU),
                 (0.5 * L + LU, 2 * L - LU),
                 (0.5 * L + LU, L - LU),
                 (0, L - LU)]

# we have written the coordinates including the wall thickness 'LU'

my_part = (first_solid.faces("<Z")
                .polyline(inner_corners)
                .mirrorY()
                .cutBlind(2.0)
                )

# demonstrate the difference with .shell(-1.5) method

show_object(my_part)