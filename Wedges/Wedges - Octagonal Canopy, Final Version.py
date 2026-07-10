import cadquery as cq

# preliminaries

c1 = 7.9 # 1L - t
c2 = 23.9 # 3L - t

p1 = (c1, c2)
p2 = (c2, c1)

def rotate_quad(point):
	x, y = point
	return (y, -x)

p3 = rotate_quad(p1)
p4 = rotate_quad(p2)
p5 = rotate_quad(p3)
p6 = rotate_quad(p4)
p7 = rotate_quad(p5)
p8 = rotate_quad(p6)

base_points = [p1, p2, p3, p4, p5, p6, p7, p8]

# beginning of solid design

octagonal_base = (cq.Workplane("front")
        .polyline(base_points)
        .close()
        .extrude(9.6)
        )

c3 = 4.0 # L / 2, or half module

d1 = (c3, c1)
d2 = (c1, c3)

d3 = rotate_quad(d1)
d4 = rotate_quad(d2)
d5 = rotate_quad(d3)
d6 = rotate_quad(d4)
d7 = rotate_quad(d5)
d8 = rotate_quad(d6)

upper_points = [d1, d2, d3, d4, d5, d6, d7, d8]

lofted_base = (octagonal_base.faces(">Z")
    .wires().toPending()
    .workplane(offset = 9.6)
        .polyline(upper_points)
        .close()
        .loft(combine = True)
        )

shelled_base = (lofted_base.faces("<Z")
        .shell(-1.2) # alternatively -1.5 for tighter fit
        )

s1 = (c3, c3) # first stud center

s2 = rotate_quad(s1)
s3 = rotate_quad(s2)
s4 = rotate_quad(s3)

stud_centers = [s1, s2, s3, s4]

studs_added = (shelled_base.faces(">Z").workplane().tag("basetop")
    .pushPoints(stud_centers)
        .circle(2.45).extrude(1.8)
    .faces(">Z")
        .fillet(0.15)

    .workplaneFromTagged("basetop")
    .pushPoints(stud_centers)
        .circle(1.25).cutBlind(-1.2)

    .workplaneFromTagged("basetop")
    .pushPoints(stud_centers)
        .circle(1.25).cutBlind(0.6)
        )

# custom elements added

stud_connector = (cq.Workplane("front")
        .moveTo(c1, c2)
        .lineTo(c1, c2 - 3.9)
        .radiusArc((c1 - 3.9, c2 - 7.8), 3.9)
        .lineTo(-c1 + 3.9, c2 - 7.8)
        .radiusArc((-c1, c2 - 3.9), 3.9)
        .lineTo(-c1, c2)
        .close()
        .extrude(1.8)

    .faces(">Z").workplane()
    .pushPoints([(4.0, 20.0), (-4.0, 20.0)])
        .circle(2.45)
        .cutBlind(-1.8)
        )

stud_holders = (cq.Workplane("front")
    .pushPoints([(4, 20), (-4, 20)])
        .circle(2.45)
        .extrude(1.8)

    .faces(">Z").workplane()
    .pushPoints([(4, 20), (-4, 20)])
        .rect(4.8, 4.8)
        .cutBlind(-1.8)
        )

work_in_progress = studs_added.union(stud_connector).union(stud_holders)

final_result = (work_in_progress.faces("<Z").workplane()
    .moveTo(0, -20)
        .rect(1.6, 7.8)
        .extrude(until = "next")
        )

show_object(final_result)