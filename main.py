from Game_Mechanics.Menu import *
from Players.HumanPlayer import HumanPlayer
from Players.SmartPlayer import SmartPlayer
from Players.IpPlayer import IpPlayer
from Players.BetaAi import BetaAi
from Players.SigmaPlayer import SigmaPlayer
from Players.AlphaPlayer import AlphaPlayer
from Players.DeltaPlayer import DeltaPlayer
from Players.IamArobot import IamArobot
from Players.Winner import Winner

# run_game(BetaAi(), AlphaPlayer())
# run_game(SigmaPlayer(), BetaAi())
# run_game(BetaAi(), SmartPlayer())
#run_game(IpPlayer("172.19.7.64"), BetaAi())
# run_game(AlphaPlayer(), AlphaPlayer())
run_game(Winner(), HumanPlayer())
# run_game(AlphaPlayer(), AlphaPlayer())
# for now AlphaPlayer is the best
