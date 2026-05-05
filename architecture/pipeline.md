# DepViT-CAD Pipeline Explained

## Overview
The DepViT-CAD pipeline processes histopathology whole-slide images (WSIs) through multiple stages, combining CNN-based feature extraction, transformer-based contextual modeling, and aggregation to produce a final diagnosis.

---

## Step 1: Whole-Slide Image (WSI)
- Input is a high-resolution histopathology slide  
- WSIs are very large and cannot be processed directly  

---

## Step 2: Patch Extraction (Tiling)
WSI → multiple patches (e.g., 512×512)

- The WSI is divided into smaller tiles  
- Only selected patches are processed  
- Each patch is handled independently  

---

## Step 3: Feature Extraction (CNN Backbone)
Patch → EfficientNet-B3 → Feature maps

- Extracts:
  - Low-level features (edges, textures)  
  - Mid-level features (structures)  
  - High-level features (semantic patterns)  

---

## Step 4: Dual Fusion Strategy (DFS)

### Feature Alignment
- Feature maps have different sizes  
- Resized using convolution and upsampling  

### Early Fusion
Shallow + Intermediate + Deep → Combined feature map

- Combines multi-scale features  
- Preserves detailed and semantic information  

---

## Step 5: Vision Transformer Module (VTM)
Fused features → Transformer → Context-aware features

- Converts features into tokens  
- Applies self-attention  
- Captures long-range relationships  

---

## Step 6: Late Fusion
Early features + Transformer output → Final feature representation

- Combines CNN and transformer outputs  

---

## Step 7: Prediction Layers
Features → Conv → ReLU → Fully Connected → Softmax

- Produces probability distribution for each class  
- Each patch gets a predicted label  

---

## Step 8: Aggregation (Majority Voting)
Patch predictions → Voting → Final diagnosis

- Counts predicted labels across patches  
- Final output = most frequent class  

Formula:
y* = argmax_y (1/n) Σ δ(ŷ_i, y)

---

## Step 9: Output Generation
- Final diagnosis at patient level  
- Visualization outputs:
  - Label maps  
  - Probability heatmaps  
  - D-Graph  

---

## Key Idea
- CNN → local features  
- DFS → multi-scale fusion  
- Transformer → global context  
- Voting → robust decision  

---

## Limitations
- Patch-based processing loses global structure  
- Majority voting ignores confidence  
- Feature resizing may distort information  

---

## Possible Improvements
- Use soft voting instead of hard voting  
- Add attention-based aggregation  
- Improve feature fusion  
- Include WSI-level context modeling  

---

## Pipeline flow
WSI → Patch Extraction → CNN (EfficientNet-B3) → DFS (Feature Fusion) → VTM (Transformer) → Prediction Layers → Majority Voting → Final Diagnosis