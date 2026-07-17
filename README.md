# auraLM

> A low-latency Large Language Model (LLM) inference engine built from first principles in C++.

---

## Vision

Modern LLM inference engines such as llama.cpp, vLLM, TensorRT-LLM and others are remarkable pieces of engineering. However, they are also extremely complex, making it difficult to understand how every component works under the hood.

**auraLM** is an educational and engineering-focused project whose goal is to build a modern LLM inference engine from scratch while understanding every major concept along the way.

Rather than treating machine learning and systems engineering as separate disciplines, auraLM combines both:

- Learning the mathematics behind transformer models
- Implementing every component from scratch
- Verifying correctness against reference implementations
- Profiling performance
- Optimizing for low latency

The objective is not merely to use LLMs, but to understand how they execute every token.

---

# Philosophy

Every feature follows the same development cycle.

```
Learn
   ↓
Build
   ↓
Verify
   ↓
Benchmark
   ↓
Optimize
   ↓
Repeat
```

Every optimization should be measurable.

Every abstraction should be understood.

Every line of code should teach something.

---

# Long-Term Goals

- Build an end-to-end decoder-only transformer inference engine
- Implement the runtime entirely in modern C++
- Support CPU inference first
- Add GPU acceleration using CUDA
- Implement KV Cache
- Implement quantized inference (FP16, INT8, INT4)
- Build a low-latency serving layer
- Support continuous batching
- Build profiling and benchmarking tools
- Understand every optimization instead of treating it as a black box

---

# Project Roadmap

## Phase 1 — Foundations

- [ ] Tokenization
- [ ] Vocabulary
- [ ] Embeddings
- [ ] Next-token prediction
- [ ] Softmax
- [ ] Sampling

---

## Phase 2 — Transformers

- [ ] Self-attention
- [ ] Multi-head attention
- [ ] Feed-forward networks
- [ ] Residual connections
- [ ] Layer normalization
- [ ] Decoder-only transformer

---

## Phase 3 — Modern LLM Architecture

- [ ] RMSNorm
- [ ] Rotary Position Embeddings (RoPE)
- [ ] SwiGLU
- [ ] KV Cache
- [ ] Autoregressive decoding

---

## Phase 4 — C++ Runtime

- [ ] Tensor class
- [ ] Memory management
- [ ] Matrix multiplication
- [ ] Transformer operators
- [ ] Model loader
- [ ] Token generation

---

## Phase 5 — Optimization

- [ ] SIMD (AVX2/AVX-512)
- [ ] Multithreading
- [ ] Cache-aware kernels
- [ ] FP16 inference
- [ ] INT8 quantization
- [ ] INT4 quantization

---

## Phase 6 — GPU Backend

- [ ] CUDA kernels
- [ ] Fused operators
- [ ] Optimized attention
- [ ] GPU memory management

---

## Phase 7 — Serving Infrastructure

- [ ] Low-latency inference server
- [ ] Streaming responses
- [ ] Request scheduling
- [ ] Continuous batching

---

# Repository Structure

```
auraLM/

├── docs/              # Engineering notes and design documents
├── learning/          # Concepts implemented while learning
├── reference/         # Python reference implementation
├── include/           # C++ headers
├── src/               # C++ source code
├── tests/             # Unit tests
├── benchmarks/        # Performance benchmarks
└── tools/             # Model conversion and utilities
```

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Reference Implementation | Python + PyTorch |
| Core Runtime | C++20 |
| Build System | CMake |
| Testing | GoogleTest |
| GPU Backend | CUDA *(planned)* |
| Serving Layer | Rust *(planned)* |

---

# Learning Objectives

This project aims to build a practical understanding of:

- Transformer architecture
- LLM inference
- Systems programming
- Memory management
- Parallel programming
- Performance engineering
- GPU programming
- Numerical computing

---

# Current Status

🚧 Project initialization.

Currently implementing the fundamental building blocks required for LLM inference.

---

## License

MIT License