# CH4rch Market Terminal

> **A next-generation event-driven cryptocurrency market terminal built with modern Python.**

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Architecture](https://img.shields.io/badge/Architecture-Event--Driven-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Pre--Alpha-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

</div>

---

## Table of Contents

* [Overview](#overview)
* [Vision](#vision)
* [Core Principles](#core-principles)
* [Key Features](#key-features)
* [Current Development Status](#current-development-status)
* [Architecture at a Glance](#architecture-at-a-glance)
* [Technology Stack](#technology-stack)

---

# Overview

**CH4rch Market Terminal** is a modern cryptocurrency market terminal designed around an **event-driven architecture**, strong modularity, and long-term maintainability.

Unlike traditional trading dashboards that tightly couple data sources, analysis engines, storage, and user interfaces, this project treats every subsystem as an independent component communicating through a centralized event bus.

The project is intended to become a flexible platform for:

* cryptocurrency market monitoring;
* real-time analytics;
* technical indicators;
* multiple market providers;
* extensible plugins;
* desktop terminal interfaces;
* automated strategies;
* historical market storage.

The architecture prioritizes scalability over short-term convenience, allowing new providers, indicators, storage backends, and user interfaces to be integrated with minimal changes to the existing codebase.

---

# Vision

The long-term objective is to build a professional desktop platform capable of aggregating market data from multiple cryptocurrency exchanges and on-chain sources into a unified, normalized runtime.

Every subsystem should remain independent and replaceable.

Instead of building "one application", CH4rch Market Terminal is designed as an extensible runtime where additional functionality can be introduced as isolated modules.

Future releases are planned to include:

* multi-provider aggregation;
* technical analysis engine;
* plugin ecosystem;
* asynchronous runtime;
* desktop interface built with Qt6;
* historical database;
* websocket streaming;
* scripting capabilities;
* alerting system;
* portfolio monitoring.

---

# Core Principles

The project follows several architectural principles that define every implementation decision.

## Event-Driven Communication

Modules never communicate directly.

Instead, they exchange immutable events through the Event Bus.

This dramatically reduces coupling between components and allows the runtime to evolve without breaking existing modules.

---

## Loose Coupling

Every major subsystem is designed as an independent layer.

Examples include:

* Providers
* Storage
* Analysis
* Runtime
* UI
* Plugins

Each component should only expose a clearly defined public interface.

---

## Dependency Inversion

High-level modules must never depend on concrete implementations.

Instead, they communicate through abstract interfaces and service registration.

This enables:

* easier testing;
* runtime replacement;
* future dependency injection;
* plugin support.

---

## Single Responsibility

Each package is responsible for one concern only.

For example:

* providers collect data;
* analysis processes data;
* storage persists data;
* UI visualizes data;
* runtime coordinates components.

---

## Explicit Runtime Lifecycle

The application lifecycle is deterministic.

Every runtime component follows the same sequence:

```
Created
    ↓
Initializing
    ↓
Starting
    ↓
Running
    ↓
Stopping
    ↓
Stopped
```

This makes startup, shutdown, debugging, and recovery predictable.

---

# Key Features

## Runtime

* asynchronous application runtime
* lifecycle management
* centralized configuration
* structured logging
* service registry
* module management

---

## Event System

* asynchronous Event Bus
* immutable event objects
* publish / subscribe model
* strongly separated communication
* extensible event hierarchy

---

## Providers

Designed around a unified abstraction layer.

Planned providers include:

* DexScreener
* Binance
* Bybit
* OKX
* Coinbase
* Kraken
* Hyperliquid
* Pump.fun

All providers normalize incoming market data before exposing it to the runtime.

---

## Storage

Designed for multiple interchangeable backends.

Current roadmap includes:

* SQLite
* PostgreSQL
* TimescaleDB

Storage is isolated from providers through repositories.

---

## Analysis

The analysis engine will operate entirely on normalized market events.

Planned indicators include:

* RSI
* EMA
* SMA
* MACD
* VWAP
* ATR
* Bollinger Bands
* Volume Profile

---

## Desktop UI

The graphical interface is planned to be built with **Qt6**.

The UI layer will never communicate directly with providers.

Instead, it subscribes to runtime events generated by the analysis engine.

---

# Current Development Status

Current project phase:

**Architectural Foundation**

Completed:

* modern src-layout
* Python package architecture
* application runtime
* module manager
* lifecycle management
* service registry
* centralized configuration
* structured logging
* asynchronous event bus
* provider abstraction
* storage foundation

In progress:

* provider runtime
* provider registry
* DexScreener integration

Planned:

* analysis engine
* realtime websocket layer
* database migrations
* plugin runtime
* Qt6 interface

---

# Architecture at a Glance

```
                   +----------------------+
                   |     Application      |
                   +----------+-----------+
                              |
                              v
                   +----------------------+
                   |       Runtime        |
                   +----------+-----------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
     ModuleManager      ServiceRegistry      EventBus
          |                                       |
          |                                       |
          +-------------------+-------------------+
                              |
        +---------------------+----------------------+
        |                     |                      |
        v                     v                      v
    Providers            Analysis Engine         Storage
        |                     |                      |
        +---------------------+----------------------+
                              |
                              v
                          Desktop UI
```

The runtime acts as the central coordinator while every subsystem remains isolated through well-defined interfaces and asynchronous event exchange.

---

# Technology Stack

| Component             | Technology                         |
| --------------------- | ---------------------------------- |
| Language              | Python 3.14+                       |
| Configuration         | Pydantic Settings                  |
| Logging               | Structlog                          |
| HTTP Client           | HTTPX                              |
| Database              | SQLite (initial)                   |
| Async Runtime         | asyncio                            |
| Event System          | Custom Event Bus                   |
| Packaging             | src-layout                         |
| GUI                   | Qt6 (planned)                      |
| Architecture          | Event-Driven                       |
| Dependency Management | Virtual Environment / uv (planned) |
