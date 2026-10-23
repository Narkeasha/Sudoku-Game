#grid class 
#game logic

#better outside class.
def create_line_coordinates(cell_size: int) -> list[list[tuple]]: #creates the x, y coordinates for drawing grid lines
    points = []
    for y in range(1, 9):
        #horizontal lines
        temp = []
        temp.append((0, y * cell_size)) #[((0, 100), (0, 200), (0,300...))] horizontal #tuples
        temp.append((900, y * cell_size)) #[((900, 100), (900, 200), (900,300...))] 
        points.append(temp) #append temp likst - cretaes y cooordinates

    for x in range(1, 10): 
        #vertical lines up to 10 to close grid on right side
        temp = []
        temp.append((x * cell_size, 0)) #[((100, 0), (200, 0), (300,0...))] horizontal #tuples
        temp.append((x * cell_size, 900)) #[((100, 900), (200, 900), (300,900...))] 
        points.append(temp) #append temp likst - cretaes x cooordinates
    print(points)
    return points


class  Grid: 
    def __init__(self):
        #creat 1 propetry
        self.cell_size = 100 #size of each cell is 100x100
        self.line_coordinates = create_line_coordinates(self.cell_size)#line coordinates


    #draw lines method
    def draw_lines(self, pg, surface) -> None:
        for index, line in enumerate(self.line_coordinates):
            pg.draw.line(surface, (0, 50, 0), line[0], line[1]) 
        