def path():
    p = ["right", "down", "down", "down", "down", "down", "down", ]
    for i in p:
        yield i
	#genius code


def script(check, x, y):
    if check("level") == 1:
        if check("gold", x, y) > 0:
            return "take"
        if check("wall", x + 2, y):
            return "down"
        return "right"
    
    if check("level") == 2:
        if check("gold", x, y) > 0:
            return "take"
        if check("gold", x, y - 1) > 0:
            return "up"
        if check("gold", x, y + 1) > 0:
            return "down"
        if check("gold", x + 1, y) > 0:
            return "right"
        if not check("wall", x + 2, y):
            return "right"
        if not check("wall", x, y - 1):
            return "up"
        return "down"

    if check("level") == 3:
        if check("gold", x, y) > 0:
            return "take"
        if (check("wall", x - 1, y) and not check("wall", x, y - 1)):
            return "up"
        if check("wall", x, y - 1) and not check("wall", x + 1, y):
            return "right"
        
        if check("wall", x + 1, y) and check("wall", x, y - 1):
            return "down"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1) and not check("wall", x + 1, y):
            return "right"
        if check("wall", x - 1, y + 1) or check("wall", x, y + 1):
            return "left"
        return "down"
    
    if check("level") == 4:
        if check("gold", x, y) > 0:
            return "take"
        
        if x == 11 and y == 19:
            return "down"
        if x == 12 and y == 20:
            return "up"
        if x == 4 and y == 10:
            return "right"
        
        
        if (check("wall", x - 1, y) and not check("wall", x, y - 1)):
            return "up"
        if check("wall", x, y - 1) and not check("wall", x + 1, y):
            return "right"
        
        if check("wall", x + 1, y) and check("wall", x, y - 1):
            return "down"
        if check("wall", x - 1, y - 1):
            return "up"
        if check("wall", x + 1, y - 1) and not check("wall", x + 1, y):
            return "right"
        if check("wall", x - 1, y + 1) or check("wall", x, y + 1):
            return "left"
        return "down"
    
    if check("level") == 5:
        if check("gold", x, y) > 0:
            return "take"

    return "pass"
