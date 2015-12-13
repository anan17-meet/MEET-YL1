import meet
import random 
import turtle








cells=[]
user_cell={"radius":20,"x":0,"y":0,"dy":1,"dx":1,"color":"black"}
user_cell=meet.create_cell(user_cell)
cells.append(user_cell)

for i in range(30):
	ball1={"radius": random.randint(1,50), "x": random.randint (-400,250), "y": random.randint (-100,250),"dy":random.randint (-4,1),"dx":random.randint(0,1),"color":"blue"}

	circle1=meet.create_cell(ball1)
	cells.append(circle1)


def borders(cells):

	for i in cells:
		sw=meet.get_screen_width()
		sh=get_screen_height()
		x=i.xcor()
		y=i.ycor()
		if(x > sw or x< -sw):
			i.set_dx(-i.get_dx())
		if(y > sh or y< -sh):
			i.set_dy(-i.get_dy())

i=0
while(True):
	x,y = meet.get_user_direction(user_cell)
	user_cell.set_dx(x)
	user_cell.set_dy(y)
	meet.move_cells(cells)

	borders(cells)

while(True)
	move_cells(cells)
	borders(cells)
	dx,dy =get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	for i in cells:
		r=i.get_radius()
		x=i.xcor()
		y=i.cor()
		for g in cells: 	
			r2=g.get_radius()
			x2=g.xcor()
			y2=g.ycor()
			if((x-x2)**2+ (y-y2)**2)0.5<(r-r2)
				if (g==user_cell):
					g.bye()
			
	






meet.mainloop()	
