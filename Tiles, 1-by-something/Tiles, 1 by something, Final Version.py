import cadquery as cq

part_wid = 1 # fixed
Part_len = n = 3 # varies

module_len = L = 8.0
lego_unit = U = 1.6
horizontal_tolerance = t = 0.1
groove_wid = g = 0.4
    # that is, 0.3 measured from edge

base_part = (cq.Workplane("front")
        .rect((n * L) - (2 * t), (1 * L) - (2 * t))
        .extrude(3.1)
    .faces("<Z").workplane()
        .rect((n * L) - (2 * U), (1 * L) - (2 * U))
        .cutBlind(-2.0)
    .faces("<Z").workplane()
        .rect((n * L) - (2 * t), (1 * L) - (2 * t))
            .rect((n * L) - (2 * g), (1 * L) - (2 * g))
        .cutBlind(-0.4)
            .translate((((n * L) / 2) - 4.0, 0))
        )

antistud_squares = cq.Workplane("front")

for i in range((2 * n) - 1):
    each_square = (cq.Workplane("front")
        .rect(4.8, 4.8)
        .extrude(2.0)
        .rotateAboutCenter((0, 0, 1), 45)
        .translate((i * 4.0, 0, 0))
        )
    antistud_squares = antistud_squares.union(each_square)

antistud_pocket = (cq.Workplane("front")
        .rect((n * L) - (2 * U) - 4.8, (1 * L) - (2 * U))
        .extrude(2.0)
            .translate((((n * L) / 2) - 4.0, 0))
        )

stud_holders = antistud_pocket.cut(antistud_squares)

tile_result = base_part.union(stud_holders)

show_object(tile_result)