import cadquery as cq

part_wid = 1 # fixed
part_len = n = 3 # varies

module_len = L = 8.0
lego_unit = U = 1.6
horizontal_tolerance = t = 0.1
groove_wid = g = 0.4
    # that is, 0.3 when measured from edge

insert_base = (cq.Workplane("front")
        .rect((n * L) - (2 * t), (1 * L) - (2 * t))
        .extrude(-1.6)
    .faces(">Z").workplane()
        .rect((n * L) - (2 * t), (1 * L) - (2 * t))
            .rect((n * L) - (2 * g), (1 * L) - (2 * g))
        .cutBlind(-0.4)
        )

studs = (cq.Workplane("front")
    .rarray(8.0, 0, n, 1, True)
        .circle(2.45).extrude(1.8)
    .faces(">Z")
        .fillet(0.15)
    .faces(">Z")
        .circle(1.65).cutBlind(-1.8)
        )

ridges = (cq.Workplane("front")
    .rarray(8.0, 0, n, 1, True)
        .circle(1.65).extrude(1.8)
    .faces(">Z")
        .rect(3.1, 3.1).cutBlind(-1.8)
        )

final_result = insert_base.union(studs).union(ridges)

show_object(final_result)