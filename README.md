# XarmTable Gym Environment

A custom [Gymnasium](https://github.com/Farama-Foundation/Gymnasium) environment simulating the [xArm7](https://www.ufactory.cc/products/xarm-7) robot arm on a tabletop. Designed for reinforcement learning experiments in continuous or discrete control spaces using MuJoCo physics.

---

## 📦 Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/your-username/xarm-table-env.git
   cd xarm-table-env
   ```

2. **Install Python dependencies**:

   It's recommended to use a virtual environment. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **MuJoCo setup**:
   - You must install MuJoCo manually via [MuJoCo installation guide](https://mujoco.readthedocs.io/en/latest/installation.html).
   - Set the environment variable:
     ```
     export MUJOCO_GL=osmesa  # or egl/headless depending on your setup
     ```

---

## 🧠 Environment Summary

| Property           | Value                       |
|--------------------|-----------------------------|
| ID                 | `XarmTable-v0`              |
| Action Space       | Configurable, depends on control mode |
| Observation Space  | Configurable (6D or 14D)    |
| Render Modes       | `human`, `rgb_array`, `depth_array` |
| Control Modes      | `"ee_pos"`, `"discrete_ee_pos"`, `"joint_angles"` |

---

## 🕹️ Control Modes

- **`ee_pos`**: Control end-effector position (x, y, z) + gripper state using inverse kinematics.
- **`discrete_ee_pos`**: Discretized 2D control on the tabletop (left/right/up/down), plus open/close gripper.
- **`joint_angles`**: Direct control of all 7 joint angles and the gripper tendon.

---

## 🔍 Observation Space

The observation vector can be either:

- **14D**: `[cube_pos(3), joint_angles(7), gripper(1), ee_pos(3)]`
- **6D**: `[cube_pos(3), ee_pos(3)]`

This is configured by setting `env.observation_dim = 6` manually after creation if you want a smaller observation space.

---

## ✅ Quick Start Example

You can run the environment directly to see a random policy in action:

```
python XarmTableEnvironment.py
```

Or use it in your own code:

```
import gymnasium as gym
import XarmTableEnvironment  # triggers registration

env = gym.make("XarmTable-v0", render_mode="human", control_option="ee_pos")
obs = env.reset()

for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)
```

---

## 📁 File Structure

- `XarmTableEnvironment.py` – Main environment definition and logic
- `xarm7_tabletop.xml` – Table scene including the robot
- `xarm7_model.xml` – Definition of the xArm7 robot itself, used in xarm7_tabletop.xml
- `assets/` –  xArm7 robot description files, used in xarm7_model.xml (textures, etc.)

---

## 📌 Notes

- This project assumes the MuJoCo XML files (`xarm7_tabletop.xml` and `xarm7_model.xml`) are in the same directory as the XarmTableEnvironment.py file.
- The robot is placed at `(0, -1, 0)` on a 2x2 square table centered at `(0, 0)`.

---

Feel free to open issues or PRs if you want to extend this environment!
