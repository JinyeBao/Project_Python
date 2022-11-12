import random
class Player:
    '''
    Player() represents a "naive" player playing a stick-picking game from 100 sticks,in which thelast onw to pick the stick lose.
    The rule is if there are 5-100 sticks left, he/ she will choose randomly between 1, 2, or 3 
    if 2-4 sticks left, he/she will choose in a way so that 1 stick is left. 
    if 1 stick left, there is no choice but pick the last stick
    '''

    def __init__(self):
        self._result = []
        
    
    def play(self, num_stick_left, t=0):
        '''
        A method being called when it is the player's turn to play
        ------
        num_stick_left : the number of sticks left 
        ------ 
        Returns : the number of stick chosen in this round, int > 0
        '''
        if num_stick_left in range(5, 101):
            stick_choose = random.choice((1, 2, 3))
            return stick_choose
        if num_stick_left in range(2, 5):
            stick_choose = num_stick_left - 1
            return stick_choose
        if num_stick_left == 1:
            return 1
    
    def outcome(self, result):
        '''
        Put the result (true/false) of the game into the list,  a method being called when the game is over to notify the player if s/he has won the game
        '''
        self._result.append(result)
        
    def winning_percentage(self, n = None):
        '''
        Calculate the player's winning percentage for the last n games

        ----------
        n : int, optional
        the number of last n games used to calculate the winning percentage. If the argument is not given, then calculate the winning percentage based on all rounds it has played
        -------
        Returns: the winning percentage, float, in the range of [0,1]

        '''
        num_winning_round = 0
        if n == None:
            n = len(self._result)
        for i in range(len(self._result)-n, len(self._result)):
            if self._result[i] == True:
                num_winning_round += 1
        return num_winning_round/n
    

            
            

class SmartPlayer(Player):
    '''
    SmartPlayer(Player) represents a smart player that could deduce the losing and winning positions. He/She knows about the "winning positions" and the corresponding winning strategy.
    
    '''

    
    def play(self, num_stick_left, t=0):
        '''
        A method being called when it is the smart player's turn to play
        ------
        num_stick_left : the number of sticks left 
        ------ 
        Returns : the number of stick chosen in this round, int > 0

        '''
        if num_stick_left == 1:
            return 1
        if num_stick_left % 4 != 1:
            return (num_stick_left+3)%4
        else:
            return random.choice([1,2,3])



                    
            
class LearningPlayer(Player):
    '''
    LearningPlayer represents a player who will 'reward' the winning choices and "punish" the losing choices.
    '''
    def __init__(self):
        '''
        self._net_wins is dict that can be used to select the number of sticks and how to update it after a around
        self._records is dict to remember every move of the player in one round

        '''
        super().__init__()
        self._net_wins = {i:{1:0, 2:0, 3:0} for i in range(5, 101)}
        self._records = {}
        self._count = 1
    
    def check(self):
        
        '''
        To check whether the self._net_wins is reasonable
    
        Returns: dict, self._net_wins
    
        
    
        '''
        return self._net_wins
    
    def play(self, num_stick_left, t=0):
        '''
        A method being called when it is the learning player's turn to play

        ----------
        num_stick_left : the number of sticks left 
        t : int, optional
        -------
        Returns : the number of stick chosen in this round, int > 0
 

        '''
        # first time play means no figures in self._net_wins
        if len(self._result) == 0:
            if num_stick_left in range(5, 101):
                choice = random.choice([1, 2, 3])
                self._records[num_stick_left] = choice
                return choice
            elif num_stick_left < 5:
                return super(LearningPlayer, self).play(num_stick_left)
        else:
            # first record the outcome of the last game, and to make it call only once in one round, we use _count and t
            if self._count != t:
                for i, j in self._records.items():
                    if self._result[-1] == True: 
                        self._net_wins[i][j] += 1
                    else:
                        self._net_wins[i][j] -= 1
                    self._records = {}
                    self._count += 1


            if num_stick_left in range(5, 101):
                _r = {1:self._net_wins[num_stick_left][1], 2:self._net_wins[num_stick_left][2], 3:self._net_wins[num_stick_left][3]}
                for x in _r:
                    while x<=0:
                        _r[x] == 1 # make the ones whose marks is 0 or negative into 1
                choice = max(_r, key = _r.get)
                self._records[num_stick_left] = choice
                return choice
            if num_stick_left < 5: # when smaller than 5 sticks left, we don't have to count it into the _records
                return super(LearningPlayer, self).play(num_stick_left)
            
     
    



     
class LearningPlayer_Plus(Player):
    '''
    LearninPlayer_Plus represents a player who can record his/her and the other player's choices. And if he/she win, he/she reward his/her move one point, and punish the other player's move one point, v.v.
    '''
    
    def __init__(self):
        '''
        self._net_wins is dict that can be used to select the number of sticks and how to update it after a around
        self._records_1 is dict to remember every move of the player in one round
        self._records_2 is dict to remember every move of the other player in one round

        '''
        super().__init__()
        self._net_wins = {i:{1:0, 2:0, 3:0} for i in range(5, 101)}
        self._records_1 = {}
        self._records_2 = {}
        self._count = 1
        
    def check(self):
        
        '''
        To check whether the self._net_wins is reasonable
    
        Returns: dict, self._net_wins
    
        
    
        '''
        return self._net_wins
        
    def play(self, num_stick_left, t=0):
        '''
        A method being called when it is the learning player_plus's turn to play

        ----------
        num_stick_left : the number of sticks left 
        t : int, optional
        -------
        Returns : the number of stick chosen in this round, int > 0
 

        '''
        #similar explanation as LearningPlayer
        if len(self._result) == 0:    
            if num_stick_left in range(5, 101):
                choice = random.choice([1, 2, 3])
                self._records_1[num_stick_left] = choice
                return choice
            elif num_stick_left < 5:
                x = list(self._records_1.keys())
                if num_stick_left == 1:
                    return 1
                else:
                    return num_stick_left - 1
                        
            
        else:
            if self._count != t:
                #here is different as i use a loop to record the other person's move by calculations
                r1_keys_list = list(self._records_1.keys())
                for i in range (len(r1_keys_list)):
                    if self._records_1[r1_keys_list[i]] < 5:
                        break
                    if self._records_1[r1_keys_list[i]] != 100:
                        self._records_2[100] = 100 - self._records_1[r1_keys_list[i]]
                    else:
                        self._records_2[r1_keys_list[i] - self._records_1[r1_keys_list[i]]] = r1_keys_list[i] - self._records_1[r1_keys_list[i]] - r1_keys_list[i + 1]

                for i, j in self._records_1.items():
                    if self._result[-1] == True:
                        self._net_wins[i][j] += 1
                    else:
                        self._net_wins[i][j] -= 1
                    self._records_1 = {}
                    self._count += 1
                for m, n in self._records_2.items():#here i put the other person's move into the self_net_wins as well
                    if self._result[-1] == True:
                        self._net_wins[m][n] -= 1
                    else:
                        self._net_wins[m][n] += 1
                    self._records_2 = {}
                    
            if num_stick_left in range(5, 101):
                choice = max(self._net_wins[num_stick_left], key = self._net_wins[num_stick_left].get) # here i consider to choose the biggest number in each key in dict.                 
                self._records_1[num_stick_left] = choice
                return choice
            
            elif num_stick_left < 5:
                if num_stick_left == 1:
                    return 1
                else:
                    return num_stick_left - 1
            


    


    

        
        
       


class NimGame:
    '''
    this class represents a Nim game
    '''
    def __init__(self, player_1, player_2):
        '''
        player_1 : Player, one of the player of the nim game
        player_2 : Player, another player of the nim game
        '''
        self._players = [player_1, player_2]



    def play(self, t=0):
        '''
        A game first random choose the one to play, and ask the two player to play in turn until no sticks left.
        return : None
        '''
        sticks = 100
        loser_idx = None
        player = random.sample([0,1], 2) # randomly decide the order of players
        while loser_idx is None:
            for m in player:
                num_stick = self._players[m].play(sticks, t)
                sticks -= num_stick
                assert sticks >= 0, "number of sticks remaining cannot be negative"
                if sticks == 0: # someone has lost the game
                    loser_idx = m
                    break
        # notify the player the game outcome
        for i in player:
            self._players[i].outcome(i != loser_idx) 
 
    
 
    
 
    
 
    
                        
                        

                    
                
                    
    
                
    
                        
                        
                        
                        
                        

                        
                    
                    
                    
                    
    
