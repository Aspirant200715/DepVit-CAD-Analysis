#  DepViT-CAD Analysis & Improvements

## Overview

This repository presents a detailed analysis of the DepViT-CAD framework, a hybrid deep learning model designed for multi-class cancer classification using histopathology whole-slide images (WSIs). The architecture combines convolutional neural networks (CNNs) and transformer-based modules to effectively capture both local tissue features and global contextual relationships. In addition to explaining the original methodology, this repository highlights key limitations and proposes potential improvements to enhance model robustness and clinical applicability.

---

## Problem Statement

Histopathological diagnosis is the gold standard for cancer detection, but it is time-intensive and subject to variability due to complex tissue morphology and inter-observer differences. Automated classification is challenging due to:

* Heterogeneous regions within WSIs
* Visual similarity between cancer subtypes
* Large image sizes requiring patch-based processing

---

## Pipeline Overview

```text
WSI → Patch Extraction → CNN (EfficientNet-B3)
     → Dual Fusion Strategy (DFS)
     → Vision Transformer Module (VTM)
     → Prediction Layers
     → Majority Voting → Final Diagnosis
```

---

## Key Components

### CNN Backbone (EfficientNet-B3)

* Extracts hierarchical multi-scale features
* Captures local textures and cellular patterns

### Dual Fusion Strategy (DFS)

* Combines shallow, intermediate, and deep features
* Uses spatial alignment (upsampling + resizing)
* Ensures consistent feature representation before fusion

###  Vision Transformer Module (VTM)

* Applies self-attention to model long-range dependencies
* Enhances global contextual understanding

### Prediction & Aggregation

* Tile-level predictions generated using softmax
* Final patient-level diagnosis obtained via majority voting

---

## Results Summary

* Tile-level Sensitivity: **88.60%**
* Tile-level F1-score: **89.54%**
* Patient-level Sensitivity: **94.11%**
* Patient-level F1-score: **94.37%**

Majority voting improves robustness by reducing noise from individual patch predictions.

---

## Limitations

### Hard Voting Strategy

* Ignores prediction confidence
* Can lead to instability in borderline cases

### Patch-Based Independence

* Tiles are processed independently
* Global WSI-level context is partially lost

### Subtype Confusion

* Difficulty distinguishing visually similar cancers (e.g., gliomas)

### Feature Alignment Issues

* Upsampling may distort feature representation

---

## Proposed Improvements

### 1. Soft Voting Aggregation

* Replace hard voting with probability-based aggregation
* Improves robustness in uncertain predictions

```python
import numpy as np

def soft_voting(tile_probs):
    return np.argmax(np.mean(tile_probs, axis=0))
```

---

### 2. Attention-Based Aggregation

* Assign importance weights to tiles
* Focus on diagnostically relevant regions

---

### 3. Enhanced Feature Fusion

* Replace simple concatenation with adaptive fusion
* Improve integration of multi-scale features

---

### 4. Global Context Modeling

* Incorporate WSI-level relationships beyond patch-level analysis

---

##  Evaluation Insights

* Macro-averaged metrics ensure equal importance across all classes
* Calibration curves and Brier loss indicate reliable probability estimates
* Performance improves significantly from tile-level to patient-level

---

##  References

* Original Paper: https://arxiv.org/pdf/2507.10250v1
* Original Implementation: https://github.com/AshkanShakarami/DepViT-CAD

---

## Author Note

This repository is created as part of a research analysis and re-thesis effort. It focuses on understanding the DepViT-CAD framework and proposing meaningful improvements rather than reproducing the full implementation.
