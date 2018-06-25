import rotation
from rotation import vector, move, snapleft, snapright, getdir, dir_to_string, calculate_x_y_string


def test_get_dir():
 facing = 0
 assert getdir(facing) == rotation._north

def test_move():
 me = vector(1, 1, 0)
 test = vector(1, 0, 0)
 facing = 0
 me=move((me.x, me.y, me.z), rotation._south, facing) 
 me.x = round(me.x, 0)
 me.y = round(me.y, 0)
 me.z = round(me.z, 0)
 assert (me.x, me.y, me.z) == (test.x, test.y, test.z)

def test_dir():
 facing = 0
 facing = snapright(facing,  getdir(facing), 45)
 assert facing == 45

def test_string_dir():
 facing = 0
 facing = snapright(facing, getdir(facing), 90)
 string = dir_to_string(facing)
 assert string == 'east'

def test_calculate_x_Y_string():
 facing = 0
 string = calculate_x_y_string(facing)
 assert string == 'streight in front'