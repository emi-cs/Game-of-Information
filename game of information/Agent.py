import random
import defs
import numpy as np
import math

class Agent():
    def __init__(self, id):
        self.secrecyIndex = 1 # 0 = not secretive; 1 = very secretive
        self.utilityOverSteps = []
        self.information = [False for i in range(defs.numOfInfo)]
        self.value = [0 for i in range(defs.numOfInfo)] #we will randomize this #how much everyone values this info
        self.id = id
        self.scoreKeeping = np.zeros(defs.numOfAgent)
        self.knowledgeBank = set([])
        self.totalNumberOfSharing = 0
        self.proportionOfSharedKnowledge = []

    def decide(self, agent, information): #matched with an Agent. the agent matched is the one self is potentially sharing info to
        saturation = []
        for i in range(len(information)):
            saturation.append(information[i].getSaturation())
    
        InfoIdToBeShared = -1
        maxSharingReward = 0
        for infoId in range(len(self.information)):
            if self.information[infoId] == True:
                gain = (1-agent.getPerceivedSecrecyIndex())*(np.mean(self.value))*agent.getPerceivedValue(infoId)
                risk = saturation[infoId] * (1-agent.getPerceivedSecrecyIndex())
                sharingReward = gain - risk
                t = math.log(defs.numOfAgent,2)
                sumFutureGains = self.sumFutureGains(self.value[infoId],0.9,t)
                hoardingReward = sumFutureGains - 0.1
                sharingReward += sumFutureGains
                if sharingReward + self.scoreKeeping[agent.id] - self.secrecyIndex > hoardingReward:
                    #any info coming down here, is already a potential info to be shared
                    if sharingReward > maxSharingReward:
                        InfoIdToBeShared = infoId 
                        maxSharingReward = sharingReward
        return InfoIdToBeShared
    
    
    def sumFutureGains(self,a,d,t)->int:
        sum = (a*(1-d**t))/(1-d)
        return sum

    #dont touch this if possible - for initializing the knowledge bank of agent
    def receive_info(self, infoId):
        if(self.information[infoId] == False):
            self.information[infoId] = True #activate piece of info

    
    #for updating the knowledge bank of an agent when a piece of information is given to her
    def receive_info_from_agent(self, agentId, infoId) -> bool: 
        if(self.information[infoId] == False):
            print(f"Agent {self.id} RECEIVED Information {infoId} from Agent {agentId}")
            self.information[infoId] = True #activate piece of info
            return True #info Exchanged happened
        else:
            print(f"Agent {self.id} already had Information {infoId}")
            return False
    

    
    def randomizeValue(self):
        for i in range(defs.numOfInfo):
            self.value[i] = random.uniform(0,1)
    


    def randomizeSecretiveness(self):
        self.secrecyIndex = random.uniform(0,1)

    def randomizeSecretivenessSecretiveCulture(self):
        self.secrecyIndex = random.uniform(0.5,1)

    def randomizeSecretivenessNonSecretiveCulture(self):
        self.secrecyIndex = random.uniform(0,0.5)

    



    def get_utility(self):
        utility = np.array(self.information).T @ np.array(self.value)
        return utility

    def getPerceivedSecrecyIndex(self) -> int:
        error = random.uniform(0,1)
        return self.secrecyIndex + error

    def getPerceivedValue(self, infoId) -> float:
        error = random.uniform(0,1)
        return self.value[infoId] + error


    def compileKB(self):
        for i in range(len(self.information)):
            if self.information[i] == True:
                self.knowledgeBank.add(i)

        
    def getNumberOfKnowledge(self) -> int:
        knowledgeCount = 0
        for i in range(len(self.information)):
            if self.information[i] == True:
                knowledgeCount+=1
        return knowledgeCount
    
   

