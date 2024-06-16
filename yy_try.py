import gymnasium as gym
import mani_skill.envs

env = gym.make(
    "PickCube-v1",
    obs_mode="state",
    control_mode="pd_joint_delta_pos",
    num_envs=16,
)
print(env.observation_space) # will now have shape (16, ...)
print(env.action_space) # will now have shape (16, ...)

obs, _ = env.reset(seed=0) # reset with a seed for determinism
for i in range(200):
    action = env.action_space.sample() # this is batched now
    obs, reward, terminated, truncated, info = env.step(action)
    done = terminated | truncated
    print(f"Obs shape: {obs.shape}, Reward shape {reward.shape}, Done shape {done.shape}")
    # note at the moment we do not support showing all parallel sub-scenes
    # at once on a GUI, only during observation generation/video recording
env.close()