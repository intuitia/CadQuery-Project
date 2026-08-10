import cadquery as cq

my_duo = (cq.Workplane("XY")
        .circle(3.9).extrude(1.6)
    .faces("<Z")
        .circle(2.45)
            .cutBlind(1.0)
    .faces(">Z").workplane()
        .circle(2.45)
            .extrude(1.8)
    .faces(">Z")
        .fillet(0.15)
    .faces(">Z").workplane().sketch()
        .circle(1.65)
        .rect(3.1, 3.1, mode = "i")
        .finalize()
            .cutThruAll()
            )

my_duo_mirrored = (my_duo
    .mirror(my_duo.faces("<Z"), union = "True")
    )

show_object(my_duo_mirrored)