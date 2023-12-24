import gym
import gym_maze

def toINT(L):
    return L[0] * 10 + L[1]

env = gym.make("maze-random-10x10-plus-v0")
observation = env.reset()
state = int(toINT(observation))
Q = np.zeros((100, 4))
NUM_EPISODES = 1000
alpha = 0.1
gamma = 0.9
epsilon = 0.1

for episode in range(NUM_EPISODES):
    action = env.action_space.sample()
    next_state, reward, done, truncated = env.step(action)
    if done or truncated:
        observation = env.reset()
env.close()