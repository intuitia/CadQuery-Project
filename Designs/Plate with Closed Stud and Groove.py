import cadquery as cq

my_part = (cq.Workplane("XY")
        .circle(3.9).extrude(3.2)
    .faces("<Z").sketch()
        .circle(2.45)
        .rect(4.8, 4.8, mode = "i")
        .finalize()
            .cutBlind(2.0)

    # the groove
    .faces("<Z").workplane()
        .circle(3.9).circle(3.6)
            .cutBlind(-0.4)

    # the stud
    .faces(">Z").workplane()
        .circle(2.45).extrude(1.8)
    .faces(">Z")
        .fillet(0.15)
    .faces(">Z[2]").workplane()
        .circle(1.65)
            .cutBlind(-1.2 - 0.6)
            )

show_object(my_part)