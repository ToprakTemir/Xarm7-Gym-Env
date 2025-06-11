from gymnasium.envs.registration import register

try:
    register(
        id="XarmTableEnv-v0",
        entry_point="xarm7_gym_env.XarmTableEnvironment:XarmTableEnv",
        kwargs={"control_option": "ee_pos"},
        max_episode_steps=1000,
    )
    print("registration successful")
except Exception as e:
    print(f"Error: Xarm Environment registration failed: {e}")