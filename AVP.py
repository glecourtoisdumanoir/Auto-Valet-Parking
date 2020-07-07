#Based on a Tulip template, here is a proposition of the systems dynamics for the AVP system
#states described in the AVP gridworld.ppt document

# Environment specification
env_vars = {}
env_vars['pedestrian'] = (32, 56)
# pedestrian in state 3 is equivalent to a pedestrian in state 39 on the AVP gridworld v2.pptx
# pedestrian in state 4 is equivalent to a pedestrian in state 32 on the AVP gridworld v2.pptx
sys_vars['statusCarA'] = (1, 4)
sys_vars['statusCarB'] = (1, 4)
env_init = {'pedestrian = 54', 'statusCarA = 1', 'statusCarB = 2'}
# statusCar = 1: request for parking & healthy
# statusCar = 2: request for pickup & healthy
# statusCar = 3: unhealthy
# statusCar = 4: picked up & healthy
env_prog = set() #[]<>
env_safe = {
            '(pedestrian = 54) -> X (pedestrian = 54 || pedestrian = 55)', 
            '(pedestrian = 55) -> X (pedestrian = 55 || pedestrian = 39)', 
            '(pedestrian = 39) -> X (pedestrian = 39 || pedestrian = 32)', 
            '(pedestrian = 32) -> X (pedestrian = 32 || pedestrian = 56)', 
            '(pedestrian = 56) -> X (pedestrian = 54)', # 56 is a final state, pedestrian then respawns in state 54
            'pedestrian != carA',
            'pedestrian != carB',

            '(statusCarA = 1) -> X (statusCarA = 1 || statusCarA = 3)',
            '(statusCarA = 1 && (carA = 48 || carA = 49 || carA = 50 || carA = 51 || carA = 52 || carA = 53)) -> X (statusCarA = 1 || statusCarA = 2 || statusCarA = 3)',
            '(statusCarA = 2) -> X (statusCarA = 2 || statusCarA = 3)',
            '(statusCarA = 2 && carA = 46) -> X (statusCarA = 2 || statusCarA = 3 || statusCarA = 4)',
            '(statusCarA = 3) -> X (statusCarA = 3)',
            '(statusCarA = 4) -> X (statusCarA = 4)',
            '(statusCarA = 4 && carA = 47) -> X (statusCarA = 1)',

            '(statusCarB = 1) -> X (statusCarB = 1 || statusCarB = 3)',
            '(statusCarB = 1 && (carA = 48 || carA = 49 || carA = 50 || carA = 51 || carA = 52 || carA = 53)) -> X (statusCarB = 1 || statusCarB = 2 || statusCarB = 3)',
            '(statusCarB = 2) -> X (statusCarB = 2 || statusCarB = 3)',
            '(statusCarB = 2 && carA = 46) -> X (statusCarB = 2 || statusCarB = 3 || statusCarB = 4)',
            '(statusCarB = 3) -> X (statusCarB = 3)',
            '(statusCarB = 4) -> X (statusCarB = 4)',
            '(statusCarB = 4 && carA = 47) -> X (statusCarB = 1)',
           } 

# System dynamics
sys_vars = {}
sys_vars['carA'] = (1, 53)
sys_vars['carB'] = (1, 53)
sys_init = {'carA = 1', 'carB = 15'}
sys_safe = {
            #dynamics for carA
            '(carA = 1 && statusCarA = 1) -> X (carA = 1 || carA = 2)',
            '(carA = 2 && statusCarA = 1) -> X (carA = 2 || carA = 3)',
            '(carA = 3 && statusCarA = 1) -> X (carA = 3 || carA = 4 || carA = 9)',
            
            '(carA = 4 && statusCarA = 1) -> X (carA = 4 || carA = 5 || carA = 10)',
            '(carA = 5 && statusCarA = 1) -> X (carA = 5 || carA = 6 || carA = 11)',
            '(carA = 6 && statusCarA = 1) -> X (carA = 6 || carA = 7 || carA = 12)',
            '(carA = 7 && statusCarA = 1) -> X (carA = 7 || carA = 8 || carA = 13)',
            '(carA = 8 && statusCarA = 1) -> X (carA = 8 || carA = 14)',
            '(carA = 9 && statusCarA = 1) -> X (carA = 9 || carA = 10 || carA = 5)',
            '(carA = 10 && statusCarA = 1) -> X (carA = 10 || carA = 11 || carA = 6)',
            '(carA = 11 && statusCarA = 1) -> X (carA = 11 || carA = 12 || carA = 7)',
            '(carA = 12 && statusCarA = 1) -> X (carA = 12 || carA = 13 || carA = 8)',
            '(carA = 13 && statusCarA = 1) -> X (carA = 13 || carA = 14)',

            '(carA = 14 && statusCarA = 1) -> X (carA = 14 || carA = 15 || carA = 48)',
            '(carA = 15 && statusCarA = 1) -> X (carA = 15 || carA = 16 || carA = 49)',
            '(carA = 16 && statusCarA = 1) -> X (carA = 16 || carA = 17 || carA = 22 || carA = 50)',
            '(carA = 14 && statusCarA = 2) -> X (carA = 14 || carA = 15)',
            '(carA = 15 && statusCarA = 2) -> X (carA = 15 || carA = 16)',
            '(carA = 16 && statusCarA = 2) -> X (carA = 16 || carA = 17 || carA = 22)',

            '(carA = 48) && statusCarA = 1 -> X (carA = 48)',
            '(carA = 48) && statusCarA = 2 -> X (carA = 48 || carA = 14)',
            '(carA = 49) && statusCarA = 1 -> X (carA = 49)',
            '(carA = 49) && statusCarA = 2 -> X (carA = 49 || carA = 15)',
            '(carA = 50) && statusCarA = 1 -> X (carA = 50)',
            '(carA = 50) && statusCarA = 2 -> X (carA = 50 || carA = 16)',

            '(carA = 17 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 17 || carA = 18 || carA = 23)',
            '(carA = 18 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 18 || carA = 19 || carA = 24)',
            '(carA = 19 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 19 || carA = 20 || carA = 25)',
            '(carA = 20 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 20 || carA = 21 || carA = 26)',
            '(carA = 21 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 21 || carA = 27)',
            '(carA = 22 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 22 || carA = 18 || carA = 23)',
            '(carA = 23 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 23 || carA = 19 || carA = 24)',
            '(carA = 24 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 24 || carA = 20 || carA = 25)',
            '(carA = 25 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 25 || carA = 21 || carA = 26)',
            '(carA = 26 && (statusCarA = 1 || statusCarA = 2)) -> X (carA = 26 || carA = 27)',
            
            '(carA = 27 && statusCarA = 1) -> X (carA = 27 || carA = 28 || carA = 51)',
            '(carA = 28 && statusCarA = 1) -> X (carA = 28 || carA = 291 || carA = 292 || carA = 52)',
            '(carA = 291 && statusCarA = 1 || statusCarA = 2) -> X (carA = 291 || carA = 292 || carA = 37 || carA = 30)',
            '(carA = 292 && statusCarA = 1) -> X (carA = 291 || carA = 292 || carA = 53 || carA = 37 || carA = 30)',

            '(carA = 27 && statusCarA = 2) -> X (carA = 27 || carA = 28)',
            '(carA = 28 && statusCarA = 2) -> X (carA = 28 || carA = 291 || carA = 292)',
            '(carA = 292 && statusCarA = 2) -> X (carA = 291 || carA = 292 || carA = 37 || carA = 30)',

            '(carA = 51) && statusCarA = 1 -> X (carA = 51)',
            '(carA = 51) && statusCarA = 2 -> X (carA = 51 || carA = 27)',
            '(carA = 52) && statusCarA = 1 -> X (carA = 52)',
            '(carA = 52) && statusCarA = 2 -> X (carA = 52 || carA = 28)',
            '(carA = 53) && statusCarA = 1 -> X (carA = 53)',
            '(carA = 53) && statusCarA = 2 -> X (carA = 53 || carA = 292)',

            '(carA = 30 && statusCarA = 2) -> X (carA = 30 || carA = 31 || carA = 38)',
            '(carA = 31 && statusCarA = 2) -> X (carA = 31 || carA = 32 || carA = 39)',
            '(carA = 32 && statusCarA = 2) -> X (carA = 32 || carA = 33 || carA = 40)',
            '(carA = 33 && statusCarA = 2) -> X (carA = 33 || carA = 34 || carA = 41)',
            '(carA = 34 && statusCarA = 2) -> X (carA = 34 || carA = 35 || carA = 42)',
            '(carA = 35 && statusCarA = 2) -> X (carA = 35 || carA = 36 || carA = 43)',
            '(carA = 36 && statusCarA = 2) -> X (carA = 36 || carA = 44)',
            '(carA = 37 && statusCarA = 2) -> X (carA = 37 || carA = 31 || carA = 38)',
           
            '(carA = 38 && statusCarA = 2) -> X (carA = 38)',
            '(carA = 38 && statusCarA = 2) -> X (carA = 38 || carA = 32 || carA = 39)',

            '(carA = 31 && statusCarA = 2) -> X (carA = 31)',
            '(carA = 39 && statusCarA = 2) -> X (carA = 39 || carA = 33 || carA = 40)',
           
            '(carA = 40 && statusCarA = 2) -> X (carA = 40 || carA = 34 || carA = 41)',
            '(carA = 41 && statusCarA = 2) -> X (carA = 41 || carA = 35 || carA = 42)',
            '(carA = 42 && statusCarA = 2) -> X (carA = 42 || carA = 36 || carA = 43)',
            '(carA = 43 && statusCarA = 2) -> X (carA = 43 || carA = 44)',

            '(carA = 44 && statusCarA = 2) -> X (carA = 44 || carA = 45)',
            '(carA = 45 && statusCarA = 2) -> X (carA = 45 || carA = 46)',
            '(carA = 46 && statusCarA = 2) -> X (carA = 46)',
            '(carA = 46 && statusCarA = 4) -> X (carA = 46 || carA = 47)',
            '(carA = 47) -> X (carA = 1)', # 47 is a final state, car then respawns in state 1

            'statusCarA = 3 -> X (carA) = carA',
            'carA != pedestrian',
            
            #same dynamics for carB
            '(carB = 1 && statusCarB = 1) -> X (carB = 1 || carB = 2)',
            '(carB = 2 && statusCarB = 1) -> X (carB = 2 || carB = 3)',
            '(carB = 3 && statusCarB = 1) -> X (carB = 3 || carB = 4 || carB = 9)',
            
            '(carB = 4 && statusCarB = 1) -> X (carB = 4 || carB = 5 || carB = 10)',
            '(carB = 5 && statusCarB = 1) -> X (carB = 5 || carB = 6 || carB = 11)',
            '(carB = 6 && statusCarB = 1) -> X (carB = 6 || carB = 7 || carB = 12)',
            '(carB = 7 && statusCarB = 1) -> X (carB = 7 || carB = 8 || carB = 13)',
            '(carB = 8 && statusCarB = 1) -> X (carB = 8 || carB = 14)',
            '(carB = 9 && statusCarB = 1) -> X (carB = 9 || carB = 10 || carB = 5)',
            '(carB = 10 && statusCarB = 1) -> X (carB = 10 || carB = 11 || carB = 6)',
            '(carB = 11 && statusCarB = 1) -> X (carB = 11 || carB = 12 || carB = 7)',
            '(carB = 12 && statusCarB = 1) -> X (carB = 12 || carB = 13 || carB = 8)',
            '(carB = 13 && statusCarB = 1) -> X (carB = 13 || carB = 14)',

            '(carB = 14 && statusCarB = 1) -> X (carB = 14 || carB = 15 || carB = 48)',
            '(carB = 15 && statusCarB = 1) -> X (carB = 15 || carB = 16 || carB = 49)',
            '(carB = 16 && statusCarB = 1) -> X (carB = 16 || carB = 17 || carB = 22 || carB = 50)',
            '(carB = 14 && statusCarB = 2) -> X (carB = 14 || carB = 15)',
            '(carB = 15 && statusCarB = 2) -> X (carB = 15 || carB = 16)',
            '(carB = 16 && statusCarB = 2) -> X (carB = 16 || carB = 17 || carB = 22)',

            '(carB = 48) && statusCarB = 1 -> X (carB = 48)',
            '(carB = 48) && statusCarB = 2 -> X (carB = 48 || carB = 14)',
            '(carB = 49) && statusCarB = 1 -> X (carB = 49)',
            '(carB = 49) && statusCarB = 2 -> X (carB = 49 || carB = 15)',
            '(carB = 50) && statusCarB = 1 -> X (carB = 50)',
            '(carB = 50) && statusCarB = 2 -> X (carB = 50 || carB = 16)',

            '(carB = 17 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 17 || carB = 18 || carB = 23)',
            '(carB = 18 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 18 || carB = 19 || carB = 24)',
            '(carB = 19 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 19 || carB = 20 || carB = 25)',
            '(carB = 20 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 20 || carB = 21 || carB = 26)',
            '(carB = 21 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 21 || carB = 27)',
            '(carB = 22 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 22 || carB = 18 || carB = 23)',
            '(carB = 23 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 23 || carB = 19 || carB = 24)',
            '(carB = 24 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 24 || carB = 20 || carB = 25)',
            '(carB = 25 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 25 || carB = 21 || carB = 26)',
            '(carB = 26 && (statusCarB = 1 || statusCarB = 2)) -> X (carB = 26 || carB = 27)',
            
            '(carB = 27 && statusCarB = 1) -> X (carB = 27 || carB = 28 || carB = 51)',
            '(carB = 28 && statusCarB = 1) -> X (carB = 28 || carB = 291 || carB = 292 || carB = 52)',
            '(carB = 291 && statusCarB = 1 || statusCarB = 2) -> X (carB = 291 || carB = 292 || carB = 37 || carB = 30)',
            '(carB = 292 && statusCarB = 1) -> X (carB = 291 || carB = 292 || carB = 53 || carB = 37 || carB = 30)',

            '(carB = 27 && statusCarB = 2) -> X (carB = 27 || carB = 28)',
            '(carB = 28 && statusCarB = 2) -> X (carB = 28 || carB = 291 || carB = 292)',
            '(carB = 292 && statusCarB = 2) -> X (carB = 291 || carB = 292 || carB = 37 || carB = 30)',

            '(carB = 51) && statusCarB = 1 -> X (carB = 51)',
            '(carB = 51) && statusCarB = 2 -> X (carB = 51 || carB = 27)',
            '(carB = 52) && statusCarB = 1 -> X (carB = 52)',
            '(carB = 52) && statusCarB = 2 -> X (carB = 52 || carB = 28)',
            '(carB = 53) && statusCarB = 1 -> X (carB = 53)',
            '(carB = 53) && statusCarB = 2 -> X (carB = 53 || carB = 292)',

            '(carB = 30 && statusCarB = 2) -> X (carB = 30 || carB = 31 || carB = 38)',
            '(carB = 31 && statusCarB = 2) -> X (carB = 31 || carB = 32 || carB = 39)',
            '(carB = 32 && statusCarB = 2) -> X (carB = 32 || carB = 33 || carB = 40)',
            '(carB = 33 && statusCarB = 2) -> X (carB = 33 || carB = 34 || carB = 41)',
            '(carB = 34 && statusCarB = 2) -> X (carB = 34 || carB = 35 || carB = 42)',
            '(carB = 35 && statusCarB = 2) -> X (carB = 35 || carB = 36 || carB = 43)',
            '(carB = 36 && statusCarB = 2) -> X (carB = 36 || carB = 44)',
            '(carB = 37 && statusCarB = 2) -> X (carB = 37 || carB = 31 || carB = 38)',
           
            '(carB = 38 && statusCarB = 2) -> X (carB = 38)',
            '(carB = 38 && statusCarB = 2) -> X (carB = 38 || carB = 32 || carB = 39)',

            '(carB = 31 && statusCarB = 2) -> X (carB = 31)',
            '(carB = 39 && statusCarB = 2) -> X (carB = 39 || carB = 33 || carB = 40)',
           
            '(carB = 40 && statusCarB = 2) -> X (carB = 40 || carB = 34 || carB = 41)',
            '(carB = 41 && statusCarB = 2) -> X (carB = 41 || carB = 35 || carB = 42)',
            '(carB = 42 && statusCarB = 2) -> X (carB = 42 || carB = 36 || carB = 43)',
            '(carB = 43 && statusCarB = 2) -> X (carB = 43 || carB = 44)',

            '(carB = 44 && statusCarB = 2) -> X (carB = 44 || carB = 45)',
            '(carB = 45 && statusCarB = 2) -> X (carB = 45 || carB = 46)',
            '(carB = 46 && statusCarB = 2) -> X (carB = 46)',
            '(carB = 46 && statusCarB = 4) -> X (carB = 46 || carB = 47)',
            '(carB = 47) -> X (carB = 1)', # 47 is a final state, car then respawns in state 1

            'statusCarB = 3 -> X (carB) = carB',
            'carB != pedestrian',
            
            #no collision with another car
            'carA != carB',          
           }
sys_prog = set()