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
        )

show_object(my_part)

from cadquery import exporters
exporters.export(my_part, 'Round Tile with Groove.stl')