---
layout: post
title:  "Consistent Web Novel Illustration Generation Project"
summary: "capston design"
author: Junseo Park
contributors: "Junseo Park, Beomseok Ko, Jaehyun Jeong, and Jinseob Han"
date: '2023-03-01 14:35:23 +0530'
category: project
thumbnail: /assets/img/posts/webnovel_1.png
keywords: diffusion model, image generation, dreambooth, subject fine-tuning
permalink: /blog/consistent-web-novel/
usemathjax: true
github_link: "https://github.com/qkrwnstj306/capston_design"
image: "/assets/img/posts/webnovel_1.png"
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
  🚀 "Provides Consistent Text-to-Image Synthesis for Characters in Web Novel" 🌟
</div>

  
<p></p>


### Context

- Web novels often include illustrations of characters, either on the cover or within the text. These illustrations are typically outsourced to artists to ensure consistent character designs.
- However, communication issues between the author and the illustrator can lead to several challenges:
  - Time and cost inefficiencies
  - Failure to capture the character as envisioned by the author
  - Lack of immediate reflection of the author's feedback
  - Limited to the illustrator's particular drawing style
- To address these issues, this project aims to build an AI service that provides consistent character illustrations for web novel platforms, establishing a stable system to solve the above problems.
  - The image generation model used is the **Latent Diffusion Model (LDM)**.
  - In this project, *the author (Junseo Park)* focused on developing the AI model and server infrastructure.

### Problem

- LDM generates entirely different characters even with minor text changes, despite having a fixed seed value.
- A personalization methodology is required to create characters that remain consistent despite variations in text input.
- Assigning a separate model for each character is cost-inefficient. A single model must be capable of generating all characters within the same style.

### Proposed Method

- The generation process is as follows:
  1. First, the author selects a model (RevAnimate, DreamShaper, Pastelboys, Counterfeit) that can generate images in two styles (mid-journey or anime) to match the story's characters.
  2. After selecting tags corresponding to the character, the author generates an image.
  3. Once the desired character is generated, the author selects the character.
  4. Since a single image is insufficient for training, $20$ images with various backgrounds, expressions, and angles are generated based on a prompt template.
    - To maintain character consistency, the original prompt is preserved with slight modifications:
      - E.g., ```{original prompt}, ((upper body)), in the mountain, looking at viewer```
  5. The $20$ images are used to train the model using DreamBooth, a process that takes about $30$ minutes.
  6. The author can then generate consistent character illustrations as needed.


<p align="center">
<img src='/assets/img/posts/webnovel2.png'>
</p>

- To provide consistent and personalized characters, [DreamBooth](https://arxiv.org/abs/2208.12242) is utilized:
  - **DreamBooth** is a personalization methodology that binds a pseudo word to a subject. Each character is mapped to a unique pseudo word (e.g., ```zxw```), allowing multiple characters to be bound to a single model.

- The proposed service offers the following benefits:
  - Resolves time and cost inefficiencies
  - Generates characters as envisioned by the author
  - Simplifies the process with convenient tag-based generation
  - Immediately reflects the author's feedback
  - Enables image generation within ~$30$ seconds
  - Offers diverse image styles
  - Provides consistent character illustrations


### Result

- By integrating a stable AI service into the web novel platform, authors can now generate illustrations more flexibly and conveniently.

<p align="center">
<img src='/assets/img/posts/webnovel3.png'>
</p>

<p align="center">
<img src='/assets/img/posts/webnovel4.png'>
</p>