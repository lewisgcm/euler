-- Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
-- there are exactly 6 routes to the bottom right corner.
-- How many such routes are there through a 20×20 grid?

routes' :: (Integer, Integer) -> Integer
routes' (0, 0) = 1
routes' (0, a) = routes' (0, a-1)
routes' (a, 0) = routes' (a-1, 0)
routes' (a, b) = routes' (a-1, b) + routes' (a, b-1)

main = print (routes' (20,20))