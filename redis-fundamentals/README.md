# Redis Fundamentals

## Introduction

This repository documents my revision of Redis fundamentals. It is also useful for anyone who wants to remind themselves of the basic concepts of Redis.

This is part of a personal roadmap to become a top-tier Applied AI Engineer — able to write and design AI-driven products end-to-end without vibecoding.

This week I revised the absolute basics of Redis including:
- Setting up Redis on Windows using **Memurai** (skipping Docker — will tackle it in a later part of the roadmap)
- Core data structures: Strings, List, Set, Sorted Set, Hash
- The Pub/Sub messaging model, implemented in Python using redis-py

---

## Redis Data Structures

### String
A Redis String is a binary-safe value that can hold text, numbers, or binary data. It is the simplest Redis data type and is used for caching, counters, session tokens, and more.

### List
A Redis List is a linked list of strings. It is used to implement queues by pushing to one end and popping from the other.

### Sorted Set
A Redis Sorted Set is a set where each member is assigned a numeric score. Redis keeps members automatically sorted by score. This makes it useful for priority queues, leaderboards, rate limiters, and anything that needs ranked ordering.

### Hash
A Redis Hash is a collection of field-value pairs stored under a single key. It is used to represent objects — for example, storing all attributes of a user (name, email, age) under one key like `user:123`.

### Pub/Sub
Redis Pub/Sub is a messaging model where a publisher sends data to a channel and Redis instantly forwards it to all active subscribers. Unlike a LIST-based queue, there is no persistence — if a subscriber is offline when a message is published, that message is permanently lost.

---

## Why SORTED SET over LIST for a Priority Queue?

A LIST has no concept of priority — to find the highest priority task you would have to scan the entire list, which is O(n).

A SORTED SET assigns a numeric score to each member and Redis maintains sorted order internally using a skip list. Retrieving the highest priority task with `ZPOPMAX` is O(log n), regardless of queue size.

---

## Files

| File | Description |
|---|---|
| `priority_queue.py` | Priority queue implementation using a Redis SORTED SET |
| `pub/publisher.py` | Pub/Sub publisher — sends messages to a Redis channel |
| `pub/subscriber.py` | Pub/Sub subscriber — listens to a Redis channel |

---

## Setup (Windows)

Redis does not have an official Windows build. Use **Memurai** — a Redis-compatible server that runs natively as a Windows service.

1. Download from https://www.memurai.com/get-memurai
2. Run the installer — it registers as a Windows service and auto-starts on boot
3. Use `memurai-cli` in your terminal — identical to `redis-cli`
4. Verify: `memurai-cli ping` → should return `PONG`

Install dependencies:
```bash
uv sync
```

Run any file:
```bash
uv run python redis-fundamentals/priority_queue.py
```
