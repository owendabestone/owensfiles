
import maingame


mg = maingame
mg = mg.MainGame()
mg.restart()

while mg.quit == False:
    
        # if no result is made.
        if mg.result_string != 'win' and mg.result_string != 'lose':
            mg.print_board()
            mg.result()
            
            # bot wins or lose after its move
            
            if mg.result_string =='win' or mg.result_string == 'lose':
                break
                
            mg.play()
            mg.result()
            
            
            #user wins or loses after his move 
            
            if mg.result_string =='win' or mg.result_string == 'lose':
                mg.print_board()
                mg.quit = True
                
            # continue the process if no results yet 
            else: 
                mg.print_board()
                mg.bot()
                
        else:
            mg.quit = True
            