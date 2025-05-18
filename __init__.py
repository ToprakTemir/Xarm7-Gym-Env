from gymnasium.envs.registration import register

register(
    id="XarmTable-v0",
    entry_point="xarm_env.XarmTableEnv:XarmTableEnv",  # adjust to actual import path
    kwargs={"control_option": "ee_pos"},
    max_episode_steps=1000,
)