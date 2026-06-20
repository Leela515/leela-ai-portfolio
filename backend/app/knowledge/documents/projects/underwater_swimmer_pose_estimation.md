# Underwater Swimmer Pose Estimation

# Project Overview

This project focused on building an AI-powered underwater swimmer pose estimation system for dolphin kick performance analysis in competitive swimming.

Traditional swimming analysis relies heavily on:

* manual video inspection,
* subjective biomechanical interpretation,
* and time-consuming frame-by-frame analysis performed by coaches.

The goal of this project was to develop a computer vision pipeline capable of:

* detecting swimmers underwater,
* estimating body joint positions,
* handling underwater visual distortion,
* and generating structured kinematic outputs for athlete performance analysis.

The project was developed in collaboration with Aquatics GB and focused specifically on analysing underwater dolphin/fly kick mechanics.

---

# Problem Statement

Underwater pose estimation is significantly more difficult than standard human pose estimation because underwater environments introduce:

* lighting distortion,
* bubbles,
* turbulence,
* reflections,
* motion blur,
* swimmer occlusion,
* and inconsistent visibility of body parts.

Traditional pose estimation datasets and models are not designed for underwater sports environments where:

* keypoints are frequently obscured,
* swimmer orientation changes rapidly,
* and water dynamics reduce feature clarity.

The project aimed to create a robust underwater pose estimation pipeline capable of operating reliably under these challenging real-world conditions.

---

# System Design

The system was designed as a two-stage computer vision pipeline consisting of:

* swimmer detection,
* underwater pose estimation,
* temporal refinement,
* and structured output generation.

The architecture separated:

* swimmer localisation,
* and keypoint estimation

to improve robustness under noisy underwater conditions.

---

# Technology Stack

This section describes the technologies, frameworks, libraries, tools, and models used in the underwater swimmer pose estimation project.

## Deep Learning & Computer Vision

* PyTorch
* OpenCV
* MMDetection
* MMPose

## Models

* RTMDet
* RTMPose

## Annotation & Dataset Tools

* CVAT
* Docker

## Data Processing & Visualisation

* NumPy
* Pandas
* Matplotlib

## Development Tools

* GitHub
* VS Code

---

# Pipeline Architecture

The overall workflow followed a multi-stage computer vision pipeline:

Underwater Video
↓
Frame Extraction
↓
Annotation using CVAT
↓
Swimmer Detection using RTMDet
↓
Bounding Box Expansion
↓
Pose Estimation using RTMPose
↓
Temporal Smoothing
↓
Structured Outputs

The system generated:

* annotated videos,
* JSON outputs,
* CSV coordinate exports,
* and confidence scores for detected keypoints.

---

# Detection Pipeline

## RTMDet

RTMDet handled swimmer detection and localisation.

The model was responsible for:

* detecting swimmers in underwater frames,
* generating bounding boxes,
* isolating swimmer regions,
* and reducing underwater background noise before pose estimation.

The model was:

* fine-tuned from COCO pretrained weights,
* adapted for a single swimmer class,
* and optimized for underwater environments.

Bounding boxes were expanded by 20% to improve downstream pose estimation stability.

### Detection Performance

* mAP = 0.611
* mAP@0.5 = 0.914
* mAP@0.75 = 0.703

---

# Pose Estimation Pipeline

## RTMPose

RTMPose handled underwater swimmer pose estimation.

The model predicted a custom unilateral underwater skeleton consisting of:

* fingertip,
* wrist,
* elbow,
* shoulder,
* head,
* pelvis,
* hip,
* knee,
* ankle,
* and toe keypoints.

The project used a unilateral skeleton because:

* dolphin kicks are largely symmetric,
* one side is frequently occluded underwater,
* and unilateral representation simplified training while improving robustness.

### Pose Estimation Performance

* coco/AP = 0.9979
* AR = 0.9983

---

# Temporal Refinement

The pipeline implemented EMA (Exponential Moving Average) smoothing to reduce skeleton instability across video frames.

This helped:

* reduce prediction jitter,
* stabilize keypoint trajectories,
* and improve motion consistency during fast underwater movement.

---

# Annotation & Dataset Preparation

The project involved custom underwater dataset preparation using CVAT.

The annotation pipeline included:

* underwater swimmer bounding boxes,
* custom keypoint annotation,
* and a custom 10-keypoint unilateral skeleton.

The dataset consisted of approximately:

* 2000 annotated underwater frames.

CVAT was deployed locally using Docker for annotation management and dataset preparation.

---

# Why A Two-Stage Pipeline Was Used

The project intentionally separated:

* swimmer detection,
* and pose estimation

instead of using direct end-to-end pose estimation.

The two-stage architecture improved:

* robustness,
* localisation quality,
* and underwater pose stability.

RTMDet first isolated swimmer regions and removed underwater background noise, allowing RTMPose to focus only on cropped swimmer areas.

This improved:

* small joint localisation,
* occlusion handling,
* and overall pose estimation quality under difficult aquatic conditions.

The design also aligned with production-style sports vision pipelines where detection and pose estimation are modular systems.

---

# Technical Challenges

One of the biggest challenges was handling underwater visual distortion while maintaining stable pose estimation.

Major challenges included:

* bubbles,
* turbulence,
* underwater lighting variation,
* motion blur,
* swimmer orientation changes,
* partial occlusion,
* and small-joint localisation difficulties.

Additional engineering challenges included:

* stabilising temporal predictions,
* reducing skeleton jitter,
* handling incomplete swimmer visibility,
* and improving robustness under noisy aquatic conditions.

---

# Model Improvements & Optimisations

Several techniques were introduced to improve performance under underwater conditions:

* domain-specific fine-tuning,
* bounding box expansion,
* temporal smoothing,
* data augmentation,
* and custom skeleton design.

The project also used:

* diversified underwater samples,
* custom annotations,
* and sports-specific pose adaptation strategies.

---

# Evaluation & Analysis

The project involved:

* detection evaluation,
* pose estimation benchmarking,
* PCK analysis,
* error analysis,
* and underwater domain adaptation evaluation.

The system was evaluated on:

* localisation accuracy,
* keypoint precision,
* temporal consistency,
* and robustness under underwater noise.

---

# What Makes This Different From Standard Computer Vision Projects

Unlike standard computer vision tutorial projects, this system addressed a real-world sports AI problem under difficult underwater conditions.

The project involved:

* a real client collaboration with Aquatics GB,
* custom underwater datasets,
* domain-specific skeleton design,
* multi-model pipeline engineering,
* temporal refinement,
* and deployable inference workflows.

The project focused on:

* underwater biomechanics,
* athlete performance analysis,
* and practical coaching applications

rather than generic human pose estimation benchmarks.

---

# Engineering & Research Skills Demonstrated

This project demonstrated:

* object detection,
* pose estimation,
* multi-stage computer vision pipeline design,
* sports AI engineering,
* PyTorch model fine-tuning,
* custom dataset preparation,
* temporal refinement techniques,
* domain adaptation,
* and deployable AI system design.

The project also demonstrated:

* real-world AI engineering,
* research-oriented computer vision,
* production-style pipeline development,
* and practical deployment considerations.

---

# Engineering Focus

The project combined:

* computer vision,
* sports biomechanics,
* underwater AI systems,
* pose estimation,
* detection pipelines,
* and applied machine learning engineering

within a real-world sports analytics environment.
