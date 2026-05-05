# DepViT-CAD: Full Explanation

## Overview
DepViT-CAD is a hybrid deep learning framework designed for multi-class cancer classification using histopathology whole-slide images (WSIs). It combines convolutional neural networks (CNNs) and transformer-based architectures to capture both local cellular features and global contextual relationships.

The system operates in a patch-based manner, processes multi-scale features, and aggregates predictions to produce a final patient-level diagnosis.

---

## Problem Context
Histopathological analysis is the gold standard for cancer diagnosis, but it faces several challenges:

- WSIs are extremely large (gigapixel scale)
- Tissue regions are heterogeneous (tumor and non-tumor mixed)
- Some cancer subtypes appear visually similar
- Manual diagnosis is time-consuming and subjective

To address these issues, DepViT-CAD introduces a hybrid architecture combining CNNs and transformers.

---

## Step-by-Step Pipeline

### 1. Whole-Slide Image (WSI)
- Input is a high-resolution histopathology slide
- Cannot be processed directly due to size constraints

---

### 2. Patch Extraction (Tiling)
- The WSI is divided into smaller patches (e.g., 512×512)
- Only a subset of patches is sampled
- Each patch is processed independently

---

### 3. Feature Extraction (CNN Backbone)
- Uses EfficientNet-B3
- Extracts hierarchical features:
  - Low-level features (edges and textures)
  - Mid-level features (structures)
  - High-level features (semantic patterns)

---

### 4. Multi-Scale Feature Representation
Three levels of features are extracted:

- Shallow features: fine-grained details  
- Intermediate features: structural patterns  
- Deep features: semantic understanding  

Each level has different spatial dimensions.

---

### 5. Dual Fusion Strategy (DFS)

#### Purpose
To combine multi-scale features effectively.

#### Process

**Feature Alignment**
- Feature maps are resized to a common spatial size
- Uses convolution and bilinear upsampling

**Early Fusion**
- Combines shallow, intermediate, and deep features
- Produces a unified representation

#### Insight
DFS preserves both detailed and semantic information.

---

### 6. Vision Transformer Module (VTM)

#### Purpose
To capture global relationships across image regions.

#### Process
- Converts feature maps into tokens
- Applies self-attention mechanism

#### Attention Formula
Attention(Q, K, V) = Softmax(QKᵀ / √d) × V

#### Benefit
- Models long-range dependencies
- Overcomes locality limitations of CNNs

---

### 7. Late Fusion
- Combines CNN-based fused features with transformer output
- Produces the final feature representation

---

### 8. Prediction Layers
- Convolution layers refine features
- ReLU activation enhances important signals
- Fully connected layers generate class scores
- Softmax produces class probabilities

Each patch receives:
- A predicted class label
- A probability distribution over classes

---

### 9. Aggregation (Majority Voting)

#### Process
- Collect predictions from all patches
- Count occurrences of each class
- Select the most frequent class

#### Formula
y* = argmax_y (1/n) Σ δ(ŷᵢ, y)

#### Insight
Reduces noise from incorrect patch predictions

---

### 10. Output Generation
The system produces:
- Final patient-level diagnosis
- Label maps showing spatial predictions
- Probability heatmaps indicating confidence
- D-Graph for performance visualization

---

## Dataset and Evaluation

### Datasets
- TgCancer-ds (training and testing, surgical samples)
- CliniR-ds (external validation, biopsy and surgical samples)

### Patient-Level Split
- Ensures no data leakage
- All data from a single patient belongs to only one split

---

### Evaluation Metrics
- Sensitivity (recall)
- Specificity
- Accuracy
- F1-score

All metrics are computed using macro-averaging:
- Each class is treated equally regardless of frequency

---

## Performance Summary

- Tile-level Sensitivity: 88.60%  
- Tile-level F1-score: 89.54%  
- Patient-level Sensitivity: 94.11%  
- Patient-level F1-score: 94.37%  

Performance improves at the patient level due to aggregation.

---

## Model Strengths

- Combines local and global feature learning
- Effective multi-scale feature fusion through DFS
- Strong performance across multiple cancer types
- Good discrimination between tumor and non-tumor regions
- Reliable probability calibration

---

## Limitations

- Majority voting ignores prediction confidence
- Patch-based processing limits global context understanding
- Difficulty in distinguishing similar tumor subtypes
- Feature resizing may introduce distortions

---

## Key Insight
DepViT-CAD integrates:
- CNN for local feature extraction  
- DFS for multi-scale feature fusion  
- Transformer for global contextual modeling  

This combination enables effective classification of complex histopathological data.

---

## Conclusion
DepViT-CAD provides a strong hybrid approach for cancer classification in histopathology. While it achieves high accuracy and robustness, improvements in aggregation strategies, feature fusion, and global context modeling can further enhance its clinical applicability.