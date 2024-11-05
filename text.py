# В этом файле содержаться текста программы, для оптимизации кода.
from termcolor import colored, cprint
#----------------------- BANNER -----------------------
banner = """                                                                                                         
      # ###         ##### /##        ##### /    ##         #######            #####  #       #######    
    /  /###  /   ######  / ##     ######  /  #####       /       ###       ######  /       /       ###  
   /  /  ###/   /#   /  /  ##    /#   /  /     #####    /         ##      /#   /  /       /         ##  
  /  ##   ##   /    /  /   ##   /    /  ##     # ##     ##        #      /    /  /        ##        #   
 /  ###            /  /    /        /  ###     #         ###                 /  /          ###          
##   ##           ## ##   /        ##   ##     #        ## ###              ## ##         ## ###        
##   ##           ## ##  /         ##   ##     #         ### ###            ## ##          ### ###      
##   ##           ## ###/          ##   ##     #           ### ###        /### ##            ### ###    
##   ##           ## ##  ###       ##   ##     #             ### /##     / ### ##              ### /##  
##   ##           ## ##    ##      ##   ##     #               #/ /##       ## ##                #/ /## 
 ##  ##           #  ##    ##       ##  ##     #                #/ ##  ##   ## ##                 #/ ## 
  ## #      /        /     ##        ## #      #                 # /  ###   #  /                   # /  
   ###     /     /##/      ###        ###      #       /##        /    ###    /          /##        /   
    ######/     /  ####    ##          #########      /  ########/      #####/          /  ########/    
      ###      /    ##     #             #### ###    /     #####          ###          /     #####      
               #                               ###   |                                 |                
                ##                 ########     ###   \)                                \)              
                                 /############  /#                                                      
                                /           ###/                                                        """
banner_colored = colored(banner,"red")
# ----------------------- BANNER -----------------------
credits = """
                                                                                                         
@@@  @@@  @@@  @@@@@@@@  @@@@@@@               @@@@@@@   @@@@@@   @@@@@@@   @@@@@@@  @@@@@@@@  @@@       
@@@  @@@  @@@  @@@@@@@@  @@@@@@@@             @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@       
@@!  @@!  @@!  @@!       @@!  @@@             !@@       @@!  @@@  @@!  @@@    @@!    @@!       @@!       
!@!  !@!  !@!  !@!       !@   @!@             !@!       !@!  @!@  !@!  @!@    !@!    !@!       !@!       
@!!  !!@  @!@  @!!!:!    @!@!@!@   @!@!@!@!@  !@!       @!@!@!@!  @!@!!@!     @!!    @!!!:!    @!!       
!@!  !!!  !@!  !!!!!:    !!!@!!!!  !!!@!@!!!  !!!       !!!@!!!!  !!@!@!      !!!    !!!!!:    !!!       
!!:  !!:  !!:  !!:       !!:  !!!             :!!       !!:  !!!  !!: :!!     !!:    !!:       !!:       
:!:  :!:  :!:  :!:       :!:  !:!             :!:       :!:  !:!  :!:  !:!    :!:    :!:        :!:      
 :::: :: :::    :: ::::   :: ::::              ::: :::  ::   :::  ::   :::     ::     :: ::::   :: ::::  
  :: :  : :    : :: ::   :: : ::               :: :: :   :   : :   :   : :     :     : :: ::   : :: : :  
                                                                                                         """
credits_text = """github: https://github.com/webcartel-https \n"""
colored_credits = colored(credits,"red")