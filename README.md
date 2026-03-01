# AI_SKILL_MAXING

A structured, self-paced roadmap to become a top-tier Applied AI Engineer — able to design and build AI-driven products end-to-end without vibecoding.

**Goal:** 1 hour/day, Mon–Fri. Every week ships something real.

---

## What This Is

This repository tracks weekly progress through a foundation-first learning roadmap covering the core systems, frameworks, and tools used in production AI engineering.

Each week focuses on one topic, ends with a shipped artifact, and builds on the previous week.

---

## Roadmap Structure

| Phase | Topics |
|---|---|
| Phase 1 — Foundation | Redis, AWS, PyTorch, LLM Evaluation, RAG, Vector DBs |
| Phase 2 — Portfolio Project | Full end-to-end AI system built from scratch |
| Phase 3 — Multimodal + Open Source | VLMs, fine-tuning, open source contributions |
| Phase 4 — Job Ready | Interview prep, system design, negotiation |

---

## Progress

### Phase 1 — Foundation

| Week | Topic | Status | Folder |
|---|---|---|---|
| Week 1 | Redis — Data Structures & Patterns | ✅ Done | `redis-fundamentals/` |
| Week 2 | Redis — Task Queues & Celery Internals | 🔜 Up next | — |
| Week 3 | AWS — IAM, S3, Mental Model | — | — |
| Week 4 | AWS — ECS, ECR, Docker | — | — |
| Week 5 | PyTorch Fundamentals | — | — |
| Week 6 | LLM Evaluation — RAGAS | — | — |

---

## Setup

This project uses Python 3.13 and [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run any file
uv run python <path-to-file>
```

**Redis on Windows:** This project uses [Memurai](https://www.memurai.com/get-memurai) — a Redis-compatible server that runs natively on Windows. Install it, then verify with:

```bash
memurai-cli ping   # should return PONG
```

---

## Repository Structure

```
AI_SKILL_MAXING/
│
├── redis-fundamentals/     # Week 1 — Redis data structures & patterns
│   ├── pub/
│   │   └── publisher.py
│   ├── sub/
│   │   └── subscriber.py
│   ├── priority_queue.py
│   └── README.md
│
└── ...                     # More weeks added as roadmap progresses
```
