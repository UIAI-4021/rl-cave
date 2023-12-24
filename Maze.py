import gym
import gym_maze

env = gym.make("maze-random-10x10-plus-v0")
observation = env.reset()
NUM_EPISODES = 1000

for episode in range(NUM_EPISODES):
    action = env.action_space.sample()
    next_state, reward, done, truncated = env.step(action)
    if done or truncated:
        observation = env.reset()
env.close()