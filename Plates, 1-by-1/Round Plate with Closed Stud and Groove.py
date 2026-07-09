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
    .faces(">Z").workplane().tag("basetop")
        .circle(2.45).extrude(1.8) # stud 4.9 dia.
    .faces(">Z")
        .fillet(0.15)

    .workplaneFromTagged("basetop")
        .circle(1.65).cutBlind(-1.2)
    .workplaneFromTagged("basetop")
        .circle(1.65).cutBlind(0.6)
        # resulting stud wall thickness : 0.8 (2.45 - 1.65)
        )

show_object(my_part)

from cadquery import exporters
exporters.export(my_part, 'Round Plate with Closed Stud and Groove.stl')