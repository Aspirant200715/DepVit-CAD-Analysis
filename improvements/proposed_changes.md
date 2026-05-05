# Proposed Improvements to DepViT-CAD

## Overview
While DepViT-CAD demonstrates strong performance in multi-class cancer classification, several design choices introduce limitations that affect robustness, interpretability, and generalization. This document outlines key areas of improvement along with proposed solutions.

---

## 1. Limitation: Hard Majority Voting

### Problem
- Uses binary decision (counts only labels)
- Ignores prediction confidence
- Unstable in borderline cases

### Example
Two tiles:
- Tile 1 → Class A (0.51)
- Tile 2 → Class B (0.52)

Majority voting:
- A = 1, B = 1 → ambiguous decision

---

## Proposed Solution: Soft Voting Aggregation

### ✔ Idea
Use softmax probabilities instead of hard labels.

### ✔ Method
- Aggregate probabilities across tiles
- Select class with highest total probability

### ✔ Formula
p(y) = (1/N) * Σ p_i(y)

### ✔ Pseudo-code

import numpy as np

def soft_voting(tile_probs):
    avg_prob = np.mean(tile_probs, axis=0)
    return np.argmax(avg_prob)

## Benefits
Uses confidence information
More stable predictions
Better handling of uncertainty

---

2. Limitation: Patch-Based Independence

### Problem
Each tile processed independently
No spatial relationship between tiles
Loss of global WSI structure

---

### Proposed Solution: Spatial-Aware Aggregation

### ✔ Idea
Incorporate spatial relationships between tiles.

### ✔ Approaches
Use positional embeddings
Graph-based modeling of tiles
Neighborhood-aware voting

### ✔ Benefits
Preserves tissue structure
Improves contextual reasoning

---

## 3. Limitation: Feature Alignment via Upsampling

Problem
DFS uses interpolation (upsampling)
Does not add real information
May distort features

--- 

Proposed Solution: Learnable Feature Alignment
✔ Idea

Replace fixed resizing with learnable alignment.

✔ Approaches
Deconvolution (transposed convolution)
Attention-based alignment
Adaptive feature scaling
✔ Benefits
More accurate feature representation
Better fusion quality


---

 4. Limitation: Difficulty in Subtype Classification
Problem

Confusion between similar classes (e.g., gliomas)
Fine-grained classification is challenging Proposed Solution: Hierarchical Classification

---

✔ Idea

Break classification into stages.

✔ Structure
Tumor vs Non-Tumor
Cancer Type
Subtype Classification
✔ Benefits
Reduces confusion
Improves interpretability
Mimics clinical workflow


---

## 5. Limitation: Lack of WSI-Level Context

### Problem
Transformer operates at patch level
No global slide-level reasoning
### Proposed Solution: WSI-Level Modeling


✔ Idea

Introduce global context modeling.

✔ Approaches

Graph Neural Networks (GNNs)
Slide-level transformer
Multiple Instance Learning (MIL)

✔ Benefits

Better global understanding
Improved decision consistency


---

## 6. Limitation: No Uncertainty Awareness

Problem
Model predictions may be overconfident
No estimation of uncertainty
Proposed Solution: Uncertainty Modeling
✔ Idea

## Quantify prediction reliability.

### ✔ Approaches

Monte Carlo Dropout
Bayesian Neural Networks
Confidence calibration

### ✔ Benefits
Safer clinical deployment
Better trust in predictions


| Limitation         | Proposed Solution           |
| ------------------ | --------------------------- |
| Hard Voting        | Soft Voting                 |
| Patch Independence | Spatial-Aware Modeling      |
| Feature Alignment  | Learnable Alignment         |
| Subtype Confusion  | Hierarchical Classification |
| No Global Context  | WSI-Level Modeling          |
| No Uncertainty     | Uncertainty Estimation      |
