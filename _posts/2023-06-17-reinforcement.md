---
layout: post
title:  "Reinforcement Learning Practice"
summary: "Implementations of basic RL algorithms"
author: Junseo Park
contributors: "<span style='font-weight: bold; color: #ff5733;'>Junseo Park</span>"
date: '2023-06-17 14:35:23 +0530'
category: project
thumbnail: /assets/img/posts/rl_1_thumbnail.jpg
keywords: reinforcement learning
permalink: /proj/rl/
usemathjax: true
github_link: "https://github.com/qkrwnstj306/Reinforcement"
image: /assets/img/posts/rl_1_thumbnail.jpg
---


<div align="center" style="
  font-family: 'Times New Roman', Times, serif;
  font-size: 20px;
  font-weight: bold;
  color: #4a4a4a;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid #e0e0e0;
  border-radius: 10px;
  background: linear-gradient(120deg, #f0f8ff, #ffffff);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
  🚀 "Implementation of Basic RL Algorithms" 🌟
</div>

  
<p></p>

### Algorithm Test

- Basic RL algorithms were implemented and tested in the OpenAI Gym environment.
- The implemented algorithms are as follows:
  - ```DQN, DDQN, Dueling DQN, DDQN + Dueling, PPO, A2C, A3C```


### UAV with DDPG

$\textbf{Motivation}$

- A paper presented an experiment where a UAV uses the received signal strength as a reward and employs reinforcement learning (DDPG algorithm) to approach the user.
- The project was carried out with the idea of directly implementing the paper.

$\textbf{Environment}$

- The UAV must reach the user.
- The starting position of the UAV is fixed at ($20, 20, 200$).
- K users (default: $5$) are generated at random positions between [```rd.randint(150, 180), rd.randint(150, 180), 0```].
- The DDPG algorithm is used, and the reward is based on the received signal strength between the user and the UAV.
- The network is implemented using a simple DNN.
- The experiment ends after $60$ steps.

<div style="display: flex; justify-content: center; gap: 20px;">
  <div style="flex: 1; text-align: center;">
  <figure>
    <img src='/assets/img/posts/rl_3.png' alt="Image 1">
    <figcaption>Caption 1: Before training</figcaption>
    </figure>
  </div>
  <div style="flex: 1; text-align: center;">
  <figure>
    <img src='/assets/img/posts/rl_5.png' alt="Image 2">
    <figcaption>Caption 1: After training</figcaption>
    </figure>
  </div>
</div>

### Black Jack with TD vs MC

- TD/MC prediction/control 
- The results vary depending on the presence of ACE.
  - Areas marked with a star represent *"hit,"* while the unmarked areas represent *"stand."*

<div style="display: flex; justify-content: center; gap: 20px;">
  <div style="flex: 1; text-align: center;">
    <figure>
      <img src='/assets/img/posts/rl_6.png' alt="Image 1">
      <figcaption>Caption 1: Use ACE as 1</figcaption>
    </figure>
  </div>
  <div style="flex: 1; text-align: center;">
    <figure>
      <img src='/assets/img/posts/rl_7.png' alt="Image 2">
      <figcaption>Caption 2: Use ACE as 11</figcaption>
    </figure>
  </div>
</div>

### Unity with PPO

- Unity provides a service that allows various RL algorithms to be applied to environments created with Unity.
- A car racing environment was created, and the PPO algorithm was applied to test whether it could complete the race.
- The configuration is as follows:

```
behaviors:
  ArcadeDriver:
    trainer_type: ppo
    hyperparameters:
      batch_size: 1024
      buffer_size: 204800
      learning_rate: 0.0003
      beta: 0.005
      epsilon: 0.2
      lambd: 0.95
      num_epoch: 7
      learning_rate_schedule: linear
    network_settings:
      normalize: true
      hidden_units: 256
      num_layers: 2
      vis_encode_type: simple
    reward_signals:
      extrinsic:
        gamma: 0.995
        strength: 1.0
    keep_checkpoints: 200
    max_steps: 100000000
    time_horizon: 32
    summary_freq: 10000
    checkpoint_interval: 50000
```

<video width="100%" controls>
  <source src="/assets/img/posts/rl_1.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

### Dodge the poop game

$\textbf{Environment}$

- Action: Move left or right

- Termination: Terminated when hit by the ball

- Reward: $-0.01$ over time, $+1$ for small ball, $+10$ for large ball

- Base network: MLP

- Algorithms tested: ```DQN, A2C, DDPG, A3C, PPO, PPO + RNN, PPO + LSTM, DDQN```

- Main result: The task was easy, resulting in good performance from DNN, DDQN, and DQN.

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
  }

  table, th, td {
    border: 1px solid #ddd; /* 선 색깔을 연한 회색으로 설정 */
  }

  th, td {
    padding: 12px 15px; /* 셀 여백을 넉넉히 설정 */
    text-align: center; /* 텍스트 중앙 정렬 */
  }

  th {
    background-color: #f4f4f9; /* 헤더 배경을 연한 회색으로 설정 */
    font-weight: bold; /* 헤더 글씨 두껍게 */
  }

  tr:nth-child(even) {
    background-color: #f9f9f9; /* 짝수 번째 행에 배경색을 달리 설정 */
  }

  tr:hover {
    background-color: #f1f1f1; /* 마우스를 올렸을 때 행 배경색 변경 */
  }

  td {
    font-size: 14px; /* 표 내용 글자 크기 설정 */
  }

  strong {
    color: #2d9c2d; /* 강조된 텍스트 색깔을 초록색으로 설정 */
  }
</style>

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th># of layers</th>
      <th>Accelerated epi</th>
      <th>Best score</th>
      <th>Epi achieved best score</th>
      <th>Avg score ($\times 10^2$)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DQN</td>
      <td>4</td>
      <td>400</td>
      <td>1578</td>
      <td>178</td>
      <td>150</td>
    </tr>
    <tr>
      <td>DQN with CNN</td>
      <td>4</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
    </tr>
    <tr>
      <td>DDQN</td>
      <td>4</td>
      <td>400</td>
      <td><strong>1729</strong></td>
      <td>299</td>
      <td>160</td>
    </tr>
    <tr>
      <td>PPO</td>
      <td>5</td>
      <td>600</td>
      <td>173</td>
      <td>200</td>
      <td>11</td>
    </tr>
    <tr>
      <td>PPO with RNN</td>
      <td>5</td>
      <td>x</td>
      <td>45</td>
      <td>100</td>
      <td>11</td>
    </tr>
    <tr>
      <td>PPO with LSTM</td>
      <td>5</td>
      <td>5000</td>
      <td>140</td>
      <td>205</td>
      <td>24</td>
    </tr>
  </tbody>
</table>
