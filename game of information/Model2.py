from Agent import Agent
from Info import Info
import random
import defs
import numpy as np
import matplotlib.pyplot as plt

class Model2():
    def __init__(self, numOfAgent, numOfInfo):
        self.numOfAgent = numOfAgent
        self.numOfInfo = numOfInfo
        self.agents = [Agent(i) for i in range (numOfAgent)] #initializing agents
        self.information = [Info(i) for i in range(numOfInfo)] #initializing info
        self.initialInfoHolder = random.sample(self.agents, numOfInfo) #these are the agents that have info
        self.agentsUtility = [0 for i in range(defs.numOfAgent)] 
        self.infoUtility = [0 for i in range(defs.numOfInfo)] # i  ignore this for now
        self.socialUtility = 0
        self.socialUtilityPerStep = [0 for i in range(defs.numOfSteps)]
        self.averageUtilityPerStep = [0 for i in range(defs.numOfSteps)]
        self.stepCount = 0
        self.knowledgeExchangeCount = 0
        

    def initialize(self):
        i = 0
        for agent in self.agents:
            agent.randomizeValue()  
            # agent.randomizeSecretiveness() #result_4, result_5 deactivate
            # agent.randomizeSecretivenessNonSecretiveCulture() #result_4.1,5.1 activate 
            agent.randomizeSecretivenessSecretiveCulture() #result_4.2,5.2 activate
        
        #for result_1, result_2,result_3, result_4
        self.agents[0].secrecyIndex = 0.0001 #non-secretive
        self.agents[1].secrecyIndex = 0.9999 #secretive
        # self.agents[2].secrecyIndex = 0.3 #secretive
        # self.agents[3].secrecyIndex = 0.6 #secretive




        for info in self.information:
            info.randomizeCapacity()
 
        for info in self.information:
            agents = random.sample(self.agents, self.numOfAgent//2)
            for agent in agents:
                agent.receive_info(i)
            i+=1

        print("------------------------------------------------")
        print("At Initialization: ")
        for agent in self.agents:
            agent.compileKB()
            if(len(agent.knowledgeBank) == 0):
                print(f"Agent {agent.id} Knowledge:" + "{}")
            else:
                print(f"Agent {agent.id} Knowledge: {agent.knowledgeBank}")
        print("------------------------------------------------")
        for i in range(len(self.information)):
            print(f"Information {i} Capacity = {self.information[i].capacity}")
        print("------------------------------------------------")
        for agent in self.agents:
            print(f"Agent {agent.id} utility: {agent.get_utility()}")

        self.updateSocialUtility(0)

    #each step of the model
    #information propagation/ diffusion in action
    def step(self):
        a1Id, a2Id = self.match(self.stepCount)
        info2 = self.agents[a1Id].decide(self.agents[a2Id], self.information) #a1 giving info2 to a2 (a2 receiving info2)
        info1 = self.agents[a2Id].decide(self.agents[a1Id], self.information) #a2 giving info1 to a1 (a1 receiving info1)
        if(info2 != -1):
            infoExchangeHappened = self.agents[a2Id].receive_info_from_agent(a1Id,info2)
            self.agents[a2Id].scoreKeeping[a1Id] += 0.1 * self.agents[a2Id].value[info2]
            if(infoExchangeHappened == True):
                self.agents[a1Id].totalNumberOfSharing += 1
                self.knowledgeExchangeCount+=1
                self.information[info2].increaseCount()
        else:
            print(f"Agent {a2Id} did not receive any info from Agent {a1Id}")
            self.agents[a2Id].scoreKeeping[a1Id] -= 0.1


        if(info1 != -1):
            infoExchangeHappened = self.agents[a1Id].receive_info_from_agent(a2Id,info1)
            self.agents[a1Id].scoreKeeping[a2Id] += 0.1 * self.agents[a1Id].value[info1]
            if(infoExchangeHappened == True):
                self.agents[a2Id].totalNumberOfSharing += 1
                self.knowledgeExchangeCount+=1
                self.information[info1].increaseCount()
        else:
            print(f"Agent {a1Id} did not receive any info from Agent {a2Id}")
            self.agents[a1Id].scoreKeeping[a2Id] -= 0.1
        
        
        for i in range(defs.numOfAgent):
            self.agents[i].utilityOverSteps.insert(self.stepCount,self.agents[i].get_utility())
            self.agents[i].proportionOfSharedKnowledge.insert(self.stepCount,(self.agents[i].totalNumberOfSharing/self.agents[i].getNumberOfKnowledge())*100)

        #if capacity is reached
        #set value of info 0 for every agent
        for i in range(len(self.information)):
            if(self.information[i].capacityPassed() == True):
                if (self.information[i].firstTime == True):
                    print(f"Information {i} capacity reached")
                    for agent in self.agents:
                        agent.value[i] = 0
                    self.information[i].firstTime = False

        


        self.updateSocialUtility(self.stepCount)  
        self.stepCount += 1          



    def match(self,stepCount) -> int:
        selected = random.sample(self.agents,2)
        a1 = selected[0]
        a2 = selected[1]
        print(f"At Step {stepCount}:\nAgent {a1.id} matched with Agent {a2.id}")
        return a1.id, a2.id
        

    

    def updateAgentsUtility(self):
        i = 0
        for agent in self.agents:
            self.agentsUtility[i] = agent.get_utility()
            i += 1

    def updateSocialUtility(self, step): #called by main
        self.updateAgentsUtility()
        self.socialUtility = sum(self.agentsUtility)  + sum(self.infoUtility)
        self.socialUtilityPerStep[step] = self.socialUtility
        self.averageUtilityPerStep[step] = self.socialUtility/100


    def print(self, stepCount):
        if(stepCount == 0):
            print("------------------------------------------------")
        print()
        print("Agent Utility:")
        for i in range(len(self.agents)):
            print(f"Agent {self.agents[i].id} utility: {self.agents[i].get_utility()}")
        print()
        print("Agent Knowledge Bank:")
        for i in range(len(self.agents)):
            self.agents[i].compileKB()
            if(len(self.agents[i].knowledgeBank) == 0):
                print(f"Agent {self.agents[i].id} Knowledge:" + "{}")
            else:
                print(f"Agent {self.agents[i].id} Knowledge: {self.agents[i].knowledgeBank}")

        print()
        for info in self.information:
            print(f"Information {info.id}: {info.count}/{info.capacity} Capacity Reached")
        print()
        print(f"Social Utility: {self.socialUtility}")
        print("------------------------------------------------")
        if(stepCount == defs.numOfSteps):
            print("SIMULATION ENDED")
            print(f"# of exchanges : {self.knowledgeExchangeCount}")

