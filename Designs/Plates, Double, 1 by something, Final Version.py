import cadquery as cq

part_wid = 1
Part_len = n = 3

module_len = L = 8.0
lego_unit = U = 1.6
horizontal_tolerance = t = 0.1

tile_base = (cq.Workplane("front")
        .rect((n * L) - (2 * t), (1 * L) - (2 * t))
        .extrude(-3.2 * 2)
    .faces("<Z").workplane()
        .rect((n * L) - (2 * U), (1 * L) - (2 * U))
        .cutBlind(-3.2 - 2.0)
    .faces(">Z").workplane()
    .rarray(8.0, 0, n, 1, True)
        .circle(1.65)
        .cutBlind(-1.2)
            .translate((((n * L) / 2) - 4.0, 0))
        )

antistud_squares = cq.Workplane("front")

for i in range((2 * n) - 1):
    each_square = (cq.Workplane("front")
        .workplane(offset = -3.2 * 2)
            .rect(4.8, 4.8)
            .extrude(2.0 + 3.2)
            .rotateAboutCenter((0, 0, 1), 45)
                .translate((i * 4.0, 0))
        )
    antistud_squares = antistud_squares.union(each_square)

antistud_pocket = (cq.Workplane("front")
    .workplane(offset = -3.2 * 2)
        .rect((n * L) - (2 * U) - 4.8, (1 * L) - (2 * U))
        .extrude(2.0 + 3.2)
            .translate((((n * L) / 2) - 4.0, 0))
        )

stud_holders = antistud_pocket.cut(antistud_squares)

work_in_progress = tile_base.union(stud_holders)

studs = (cq.Workplane("front")
    .rarray(8.0, 0, n, 1, True)
        .circle(2.45).extrude(1.8)
    .faces(">Z")
        .fillet(0.15)
    .faces("<Z")
        .circle(1.65).cutBlind(0.6)
            .translate((((n * L) / 2) - 4.0, 0))
        )

my_part = work_in_progress.union(studs)

show_object(my_part)