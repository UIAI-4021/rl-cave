import gym
import gym_maze
import numpy as np

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

for episode in range(100000):
    if np.random.rand() < epsilon:
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])

    next_state, reward, done, truncated = env.step(action)
    next_state = int(toINT(next_state))
    Q[state, action] += alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])
    state = next_state

    if done or truncated:
        observation = env.reset()
state = int(toINT(env.reset()))
done = False
win = 0
for episode in range(NUM_EPISODES):
    action = np.argmax(Q[state, :])
    next_state, reward, done, truncated = env.step(action)
    if reward > 0:
        win += 1
    state = int(toINT(next_state))
    if done or truncated:
        observation = env.reset()
    env.render()
print(win)
env.close()