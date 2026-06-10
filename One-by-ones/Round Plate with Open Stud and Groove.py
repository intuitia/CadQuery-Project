import cadquery as cq

my_part = (cq.Workplane("XY")
        .circle(3.9).extrude(3.2)
    .faces("<Z").workplane()
        .rect(4.8, 4.8).cutBlind(-2.0)
    .faces("<Z").workplane()
        .circle(3.9).circle(2.5).extrude(-2.0) # antistud 5.0 dia.
        # resulting wall thickness 1.4 (3.9 - 2.5)

    # the groove
    .faces("<Z").workplane()
        .circle(3.9).circle(3.6).cutBlind(-0.4)
        # groove wid. 0.3 (3.9 - 3.6)

    # the stud
    .faces(">Z").workplane()
        .circle(2.45).extrude(1.8) # stud 4.9 dia.
    .faces(">Z")
        .fillet(0.15)

    .faces(">Z").workplane().tag("studtop")
        .rect(3.1, 3.1).cutBlind(-3.0) # 1.8 + 1.2 in total
    .workplaneFromTagged("studtop")
        .circle(2.3).circle(1.65).extrude(-3.0) # 2.3 [radius - fillet]; 3.2 + 0.1 for bar holder
        # resulting stud wall thickness : 0.8 (2.45 - 1.65)
        )

show_object(my_part)

from cadquery import exporters
exporters.export(my_part, 'Round Plate with Open Stud and Groove.stl')