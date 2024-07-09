from Model import Model
from Model2 import Model2
import defs
import matplotlib.pyplot as plt


model = Model(defs.numOfAgent,defs.numOfInfo)
model.initialize()
for i in range(defs.numOfSteps):
    model.step()
model.print(model.stepCount)


# vectors
agentsSecrecy = []
agentsTotalSharing = []
agentsTotalUtility = []
agentsProportionOfKnowledgeShared = [] #result_3

for i in range(defs.numOfAgent):
    agentsSecrecy.insert(i, model.agents[i].secrecyIndex)


for i in range(defs.numOfAgent):
    agentsTotalSharing.insert(i, model.agents[i].totalNumberOfSharing)


for i in range(defs.numOfAgent):
    agentsTotalUtility.insert(i, model.agents[i].get_utility())

  


# #result_0: total # of sharing vs secretiveness
# plt.scatter(agentsSecrecy,agentsTotalSharing)
# plt.title('Scatter plot of Total #of sharing against Secretiveness of Agents')
# plt.xlabel('Secretiveness')
# plt.ylabel('Total #of sharing')
# plt.show()


# #result_1: total utility of agent vs total number of sharing
# plt.scatter(agentsTotalSharing,agentsTotalUtility)
# plt.title('Total Utility of Agent Against Total #of sharing')
# plt.xlabel('Total #of Sharing')
# plt.ylabel('Total Utility of Agent')
# plt.show()


# result_2: total utility of agent vs total number of sharing for secretive agent
# plt.title('Utility Over Timesteps for Different types of Agents\n(#of Information=20)')
# plt.plot(range(model.stepCount),model.agents[1].utilityOverSteps, label='Secretive θ≈1')
# plt.plot(range(model.stepCount),model.agents[0].utilityOverSteps, label='Non-Secretive θ≈0')
# plt.plot(range(model.stepCount),model.averageUtilityPerStep, label='Average Agent')
# plt.plot(range(model.stepCount),model.agents[2].utilityOverSteps, label='θ=0.3')
# plt.plot(range(model.stepCount),model.agents[3].utilityOverSteps, label='θ=0.6')
# plt.xlabel('Timesteps')
# plt.ylabel('Utility of Agent')
# plt.legend()
# plt.show()

# plt.title('Utility Over Timesteps for Different types of Agents\n(#of Information=80)')
# plt.plot(range(model.stepCount),model.agents[1].utilityOverSteps, label='Secretive θ≈1')
# plt.plot(range(model.stepCount),model.agents[0].utilityOverSteps, label='Non-Secretive θ≈0')
# plt.plot(range(model.stepCount),model.averageUtilityPerStep, label='Average Agent')
# plt.plot(range(model.stepCount),model.agents[2].utilityOverSteps, label='θ=0.3')
# plt.plot(range(model.stepCount),model.agents[3].utilityOverSteps, label='θ=0.6')
# plt.xlabel('Timesteps')
# plt.ylabel('Utility of Agent')
# plt.legend()
# plt.show()


#result_3: Total Utility vs proportion of Info they share
# plt.title('Scatter Plot of Utility vs Proportion of Information Agent Shares')
# plt.scatter(model.agents[0].proportionOfSharedKnowledge, model.agents[0].utilityOverSteps, label='Non-Secretive θ≈0')
# plt.scatter(model.agents[1].proportionOfSharedKnowledge, model.agents[1].utilityOverSteps,label='Secretive θ≈1')
# plt.scatter(model.agents[2].proportionOfSharedKnowledge, model.agents[2].utilityOverSteps, label='θ=0.3')
# plt.scatter(model.agents[3].proportionOfSharedKnowledge, model.agents[3].utilityOverSteps, label='θ=0.6')
# plt.xlabel('Proportion of Info Agent Shares vs What Agent Knows (%)')
# plt.ylabel('Utility of Agent')
# plt.legend()
# plt.show()

#result_4.1: How well does a secretive agent do in an non-secretive culture?
# plt.title('How well does a Secretive Agent do in an Non-secretive culture?')
# plt.plot(range(model.stepCount),model.agents[1].utilityOverSteps, label='Secretive θ≈1')
# plt.plot(range(model.stepCount),model.agents[0].utilityOverSteps, label='Non-Secretive θ≈0')
# plt.xlabel('Timesteps')
# plt.ylabel('Utility of Agent')
# plt.legend()
# plt.show()


#result_4.2: How well does a open agent do in an secretive culture?
# plt.title('How well does a Non-secretive Agent do in an Secretive Culture?')
# plt.plot(range(model.stepCount),model.agents[1].utilityOverSteps, label='Secretive θ≈1')
# plt.plot(range(model.stepCount),model.agents[0].utilityOverSteps, label='Non-Secretive θ≈0')
# plt.xlabel('Timesteps')
# plt.ylabel('Utility of Agent')
# plt.legend()
# plt.show()



# result_5: Are agent's social utility higher in the secretive/ non-secretive culture?
# nonSecretiveCultureSocialUtilityPerStep = model.socialUtilityPerStep
# model2 = Model2(defs.numOfAgent,defs.numOfInfo)
# model2.initialize()
# for i in range(defs.numOfSteps):
#     model2.step()
# secretiveCultureSocialUtilityPerStep = model2.socialUtilityPerStep
# plt.title('Social Utility Under Different Cultures')
# plt.plot(range(model.stepCount),nonSecretiveCultureSocialUtilityPerStep, label='Non-Secretive culture')
# plt.plot(range(model.stepCount),secretiveCultureSocialUtilityPerStep, label='Secretive culture')
# plt.xlabel('Timesteps')
# plt.ylabel('Social Utility')
# plt.legend()
# plt.show()
    

#result_6: Social Utility vs #ofInfo
# plt.title('Social Utility Over Time (80 pieces of information circulating)')
# plt.plot(range(model.stepCount),model.socialUtilityPerStep)
# plt.xlabel('Timesteps')
# plt.ylabel('Social Utility')
# plt.legend()
# plt.show()



#result_7.1: Does the total number of exchanges correlate with #ofInfo
# plt.title('Rate of exchanging Information (#OfInfo=20)')
# plt.plot(range(model.stepCount),model.knowledgeExchangePerStep) 
# plt.xlabel('Time Step')
# plt.ylabel('Cumulative Number of Exchanges')
# plt.legend()
# plt.show()

#result_7.2: Does the total number of exchanges correlate with #ofInfo
# plt.title('Rate of exchanging Information (#OfInfo=40)')
# plt.plot(range(model.stepCount),model.knowledgeExchangePerStep) 
# plt.xlabel('Time Step')
# plt.ylabel('Cumulative Number of Exchanges')
# plt.legend()
# plt.show()

#result_7.3: Does the total number of exchanges correlate with #ofInfo
# plt.title('Rate of exchanging Information (#OfInfo=60)')
# plt.plot(range(model.stepCount),model.knowledgeExchangePerStep) 
# plt.xlabel('Time Step')
# plt.ylabel('Cumulative Number of Exchanges')
# plt.legend()
# plt.show()
    
#result_7.4: Does the total number of exchanges correlate with #ofInfo
# plt.title('Rate of exchanging Information (#OfInfo=80)')
# plt.plot(range(model.stepCount),model.knowledgeExchangePerStep) 
# plt.xlabel('Time Step')
# plt.ylabel('Cumulative Number of Exchanges')
# plt.legend()
# plt.show()


# #result_8: Does the capacity correlate with social utility?
# simulationsCapacityD2 = []
# capacityD2SocialUtility = []
# for s in range(10):
#     simulationsCapacityD2.insert(s,Model(defs.numOfAgent,defs.numOfInfo))
#     simulationsCapacityD2[s].initialize()
#     for i in range(defs.numOfSteps):
#         simulationsCapacityD2[s].step()
#     capacityD2SocialUtility.insert(s,simulationsCapacityD2[s].socialUtility)

# plt.title('Effect of Capacity on Social Utility')
# plt.boxplot(capacityD2SocialUtility)
# plt.xlabel('Higher Capacity')
# plt.ylabel('Social Utility')
# plt.legend()
# plt.show()


# simulationsCapacityD4 = []
# capacityD4SocialUtility = []
# for s in range(10):
#     simulationsCapacityD4.insert(s,Model(defs.numOfAgent,defs.numOfInfo))
#     simulationsCapacityD4[s].initialize()
#     for i in range(defs.numOfSteps):
#         simulationsCapacityD4[s].step()
#     capacityD4SocialUtility.insert(s,simulationsCapacityD4[s].socialUtility)

# plt.title('Effect of Capacity on Social Utility')
# plt.boxplot(capacityD4SocialUtility)
# plt.xlabel('Lower Capacity')
# plt.ylabel('Social Utility')
# plt.legend()
# plt.show()



#result_9: How does the capacity change how many info is being exchanged?
# simulationsCapacityD2 = []
# capacityD2KnowledgeExchange = []
# for s in range(10):
#     simulationsCapacityD2.insert(s,Model(defs.numOfAgent,defs.numOfInfo))
#     simulationsCapacityD2[s].initialize()
#     for i in range(defs.numOfSteps):
#         simulationsCapacityD2[s].step()
#     capacityD2KnowledgeExchange.insert(s,simulationsCapacityD2[s].knowledgeExchangeCount)

# plt.title('Effect of Capacity on #of Knowledge Exchanged')
# plt.boxplot(capacityD2KnowledgeExchange)
# plt.xlabel('Higher Capacity')
# plt.ylabel('#of Knowledge Exchanged')
# plt.legend()
# plt.show()


# simulationsCapacityD4 = []
# capacityD4KnowledgeExchange = []
# for s in range(10):
#     simulationsCapacityD4.insert(s,Model(defs.numOfAgent,defs.numOfInfo))
#     simulationsCapacityD4[s].initialize()
#     for i in range(defs.numOfSteps):
#         simulationsCapacityD4[s].step()
#     capacityD4KnowledgeExchange.insert(s,simulationsCapacityD4[s].knowledgeExchangeCount)

# plt.title('Effect of Capacity on #of Knowledge Exchanged')
# plt.boxplot(capacityD4KnowledgeExchange)
# plt.xlabel('Lower Capacity')
# plt.ylabel('#of Knowledge Exchanged')
# plt.legend()
# plt.show()
