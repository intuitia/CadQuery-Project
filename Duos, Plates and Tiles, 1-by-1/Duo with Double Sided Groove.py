import cadquery as cq

my_part = (cq.Workplane("front")
        .rect(7.8, 7.8).extrude(2 * 3.2)
    .faces("<Z").workplane()
        .rect(4.8, 4.8).cutBlind(-2 * 3.2)
    .faces("<Z").workplane()
        .rect(7.8, 7.8).rect(7.8 - 0.3, 7.8 - 0.3)
        .cutBlind(-0.4)
    .faces(">Z").workplane()
        .rect(7.8, 7.8).rect(7.8 - 0.3, 7.8 - 0.3)
        .cutBlind(-0.4)
        )

show_object(my_part)