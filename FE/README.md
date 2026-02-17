# CODESTACKER 2026 - Frontend Development Challenge

## Visit Oman: Discover & Plan

---

## 📋 Table of Contents

- [Problem Statement](#-problem-statement)
- [Project Structure](#-project-structure)
- [Part 1: Marketing Experience (SSR)](#-part-1-marketing-experience-server-side-rendering)
- [Part 2: Intelligent Itinerary Generator (CSR)](#-part-2-intelligent-itinerary-generator-client-side-rendering)
- [Technical Constraints](#-technical-constraints)
- [Submission Requirements](#-submission-requirements)
- [Dataset Schema](#-dataset-schema)

---

## 🎯 Problem Statement

Oman Vision 2040 identifies tourism as a primary pillar for economic diversification beyond oil. Increasing visitor numbers alone is not enough—the country must improve digital accessibility, trip planning efficiency, and visitor confidence.

### Current Challenges

Today, most tourism websites act as **brochures**: they show places but don't help visitors decide how to travel inside the country.

**Poor planning leads to:**

- ❌ Unrealistic travel routes
- ❌ Missed seasonal attractions (Khareef, turtle nesting, mountain climate)
- ❌ Overcrowding in specific areas
- ❌ Lost revenue for smaller regions
- ❌ Short average tourist stay

### Solution Impact

**A smart digital planning platform can:**

- ✅ Distribute tourists across regions
- ✅ Increase average stay duration
- ✅ Improve local business exposure
- ✅ Reduce travel friction
- ✅ Strengthen Oman's global tourism competitiveness

### Your Task

Build a **two-phase frontend platform**:

1. A modern marketing discovery website that promotes Oman
2. An intelligent client-side trip planner that converts interest into a concrete itinerary

> **⚠️ Important:** No backend services will exist—the entire experience must run purely in the browser.

---

## 🏗 Project Structure

You will implement a single unified frontend application using a **hybrid rendering architecture (SSR + CSR)**.

### Part 1: Marketing Experience (Discover Oman) - Server-Side Rendering (SSR)

**Objective:** Present an engaging discovery experience that introduces destinations and motivates the visitor to begin planning.

### Part 2: Intelligent Itinerary Generator (Plan Trip) - Client-Side Rendering (CSR)

**Objective:** Convert user preferences into a realistic, constraint-aware travel itinerary computed entirely in the browser.

> Both parts must operate as one singular product, sharing state seamlessly and maintaining a consistent user experience across rendering boundaries.

---

## 🌐 Part 1: Marketing Experience (Server-Side Rendering)

The first portion of the application focuses on destination discovery. Its purpose is to inspire interest while preparing structured user preferences that will later be consumed by the itinerary planner.

> **All displayed destinations must originate exclusively from the provided dataset.** Hardcoded locations are not permitted.

### 1. Landing Page

The landing page must be server-side rendered and include:

- ✅ A hero section introducing the platform
- ✅ Category exploration sections (mountain, desert, sea, culture)
- ✅ A featured destinations section populated dynamically from the dataset
- ✅ A clear call-to-action directing the user to "Plan Your Trip"
- ✅ Support for both Arabic and English layouts

**Note:** Content must be derived programmatically from the dataset and not manually written per destination.

### 2. Destination Browsing

Provide a browsable catalogue of all destinations with interactive filtering and sorting.

**Users must be able to:**

- Filter by category
- Filter by region
- Filter by recommended season
- Sort by popularity (crowd level) or estimated cost

**Requirements:**

- Filtering state must be reflected in URL query parameters to support sharable and reloadable views

### 3. Destination Details Page

Each destination must have a statically renderable details page displaying:

- Generated placeholder description text
- Recommended months indicator
- Crowd level visualization
- Estimated visit duration
- Map preview of the location

**The page must be pre-renderable without client-only data dependencies.**

### 4. Save Interest (Preference Collection)

Users must be able to save destinations of interest. These saved selections will serve as input to the itinerary generator in Part 2.

**Requirements:**

- Persist selections locally using `LocalStorage` or `IndexedDB`
- Persist across refresh and navigation
- Be accessible to the planner without additional user input

---

## 🧠 Part 2: Intelligent Itinerary Generator (Client-Side Rendering)

This section is the core engineering component. You will build a constraint-driven itinerary optimizer that produces a realistic multi-day route from the dataset and user preferences. **The entire computation must run in the browser.**

### 1. User Inputs

Collect and validate:

- **Trip duration:** 1–7 days
- **Budget tier:** `low` | `medium` | `luxury`
- **Travel month:** 1–12
- **Travel intensity:** `relaxed` | `balanced` | `packed`
- **Preferred categories:** pre-populated from saved interests

### 2. Multi-Objective Scoring Model

Implement a deterministic, multi-factor scoring model with explicit normalization.

For each location `i`, compute:

```
score(i) =
  w_interest  * Jaccard(categories_user, categories_i)
+ w_season    * SeasonFit(month, recommended_months_i)
- w_crowd     * Normalize(crowd_level_i)
- w_cost      * Normalize(ticket_cost_omr_i)
- w_detour    * DetourPenalty(i, current_route)
+ w_diversity * DiversityGain(i, selected_set)
```

**Requirements:**

- ✅ All components must be normalized to `[0,1]` before weighting
- ✅ All weights must be documented and justified
- ✅ Pure functions only (no hidden state, no randomness)
- ✅ Identical inputs must always produce identical outputs

### 3. Region-Level Planning Phase (Hierarchical Optimization)

You must plan at two levels:

#### Phase A: Region Allocation (Global)

Allocate the total trip days across regions to maximize utility while enforcing diversity.

**Constraints:**

- At least 2 regions must be visited if trip duration ≥ 3 days
- No region may receive more than `ceil(days / 2)` days
- The allocation must respect season fit (regions with low season fit should be deprioritized)

**Output:**

An ordered list of regions with assigned day counts, e.g.:

```
day 1–2: muscat
day 3–4: dakhiliya
day 5: sharqiya
```

> This phase must be computed algorithmically (not hardcoded).

#### Phase B: Intra-Region Routing (Local)

For each region block, generate an ordered list of stops per day that respects time and distance constraints.

### 4. Routing & Scheduling

You must generate a day-by-day schedule under these constraints:

| Constraint                     | Value                                                                                                  |
| ------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Max daily driving distance** | 250 km                                                                                                 |
| **Max daily visit time**       | 8 hours                                                                                                |
| **Region consistency**         | Each day must start and end in the same region                                                         |
| **Category variety**           | Avoid repeating the same category more than 2 times per day unless the user selected only one category |

**Enforce a minimum "rest gap":**

Two long stops (>90 min) cannot be adjacent without a short stop (<45 min) between them.

**Travel intensity limits:**

| Intensity  | Max Stops/Day |
| ---------- | ------------- |
| `relaxed`  | 3 stops/day   |
| `balanced` | 4 stops/day   |
| `packed`   | 5 stops/day   |

### 5. Route Quality Requirement (No Greedy-Only Solutions)

A simple greedy approach will not score well. Your solution must implement **at least one improvement strategy**, such as:

- **2-opt optimization** (local search) to reduce travel distance within a day
- **Beam search** for stop selection
- **Simulated annealing** (deterministic variant with fixed schedule) to escape local minima
- **Dynamic programming** for stop selection under time constraints (bounded by day capacity)

> **Document which approach you chose and why.**

### 6. Distance Calculation

Implement **Haversine distance**:

```typescript
distanceKm(pointA: {lat: number, lng: number}, pointB: {lat: number, lng: number}): number
```

**External routing/distance APIs are forbidden.**

Additionally compute:

- `totalKm(dayRoute)` - Total distance for a day's route
- `detourKm(route, candidateStop)` - Detour penalty for adding a stop

### 7. Budget-Aware Cost Estimation

Compute and display full breakdown:

```typescript
fuel    = total_km / 12 * fuel_price
tickets = sum(ticket_cost_omr)
food    = 6 OMR × days

hotel (per night):
  low:    20 OMR
  medium: 45 OMR
  luxury: 90 OMR
```

**Add budget feasibility:**

If total cost exceeds a budget threshold (you define and document per tier), the algorithm must:

- Reduce paid attractions
- Favor lower `ticket_cost_omr` alternatives
- Keep category coverage as high as possible

### 8. Map Rendering (Client-Only)

Must include:

- ✅ Markers for all planned stops
- ✅ Route polyline per day
- ✅ Active stop highlight synchronized with the itinerary UI
- ✅ Ability to switch between days while maintaining route visualization

### 9. Persistence

Refreshing the page must not lose:

- Saved interests
- User inputs
- Final generated plan
- Cost breakdown

### Output Format

Your planner must output:

- Region allocation plan
- Day-by-day itinerary with timestamps, stop durations, and inter-stop travel distance
- Total km and cost breakdown
- Explanation panel showing why each stop was selected (top 2 contributing score components)

### ⛔ Disallowed

- ❌ Hardcoded itineraries or "curated" day plans
- ❌ Random selection without deterministic seed and documentation
- ❌ External routing/distance APIs
- ❌ Server-side computation for planning

---

## ⚙️ Technical Constraints

To ensure consistent evaluation, all submissions must adhere to the following implementation constraints:

| Constraint               | Requirement                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Framework**            | Any FE Framework, recommended: React or Next.js                                                                                                                                  |
| **Language**             | TypeScript is **mandatory** across the entire codebase                                                                                                                           |
| **Architecture**         | Fully frontend application, no backend services, server APIs, or external computation endpoints                                                                                  |
| **Itinerary Generation** | Must be algorithmically computed from the dataset; hardcoded or manually curated plans are **not permitted**                                                                     |
| **Determinism**          | The planner must be deterministic—random selection or probabilistic outputs are **disallowed**                                                                                   |
| **AI Usage**             | AI-generated itinerary logic or external AI planning services are **not permitted**                                                                                              |
| **Maps**                 | Map tile providers may be used strictly for visualization purposes (rendering markers and routes only). Distance, routing, and planning calculations must be implemented locally |

> **⚠️ Any violation of these constraints will result in disqualification from evaluation.**

---

## 📦 Submission Requirements

Participants must submit a complete and reviewable project demonstrating both functional correctness and engineering quality.

### 1. Source Code

Provide a **public Git repository** containing:

- The full application source code
- Clear project structure and modular organization
- Meaningful commit history (avoid single-commit submissions)
- Adequate inline comments explaining non-trivial logic
- No compiled build artifacts checked into the repository

### 2. Documentation (README)

The repository must include a comprehensive README covering:

- **Project setup and run instructions**
- **Architectural overview**
- **State management approach**
- **Rendering strategy** (SSR vs CSR boundaries)
- **Detailed explanation of the itinerary generation algorithm**
- **Weight selection rationale and normalization strategy**
- **Performance considerations and optimizations**
- **Known limitations and tradeoffs**

> **⚠️ Submissions lacking algorithm explanation will not be evaluated.**

### 3. Code Quality Expectations

Your submission must demonstrate professional engineering practices:

- ✅ Type-safe implementation (TypeScript)
- ✅ Readable and maintainable naming conventions
- ✅ Separation of concerns (UI, state, algorithm, utilities)
- ✅ Commented complex logic (especially algorithmic decisions)
- ✅ No dead code or unused dependencies

### 4. Optional (Recommended)

You may additionally include:

- 🎨 Design files (Figma or equivalent)
- 🎥 Demonstration videos
- 📊 Architectural diagrams
- 🧪 Test cases for critical utilities or algorithms
- 📈 Performance measurement notes

These are not mandatory but will positively influence evaluation.

> **⚠️ Incomplete submissions or missing documentation may be disqualified from judging.**

---

## 📊 Dataset Schema

All destination content must support both English and Arabic.

```typescript
{
  "id": string,

  "name": {
    "en": string,
    "ar": string
  },

  "lat": number,
  "lng": number,

  "region": {
    "en": "muscat" | "dakhiliya" | "sharqiya" | "dhofar" | "batinah" | "dhahira",
    "ar": string
  },

  "categories": ("mountain" | "beach" | "culture" | "desert" | "nature" | "food")[],

  "company": {
    "en": string,
    "ar": string
  },

  "avg_visit_duration_minutes": number,

  "ticket_cost_omr": number,

  "recommended_months": (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12)[],

  "crowd_level": 1 | 2 | 3 | 4 | 5
}
```

**Implementations must render the correct language dynamically based on the selected locale.**

**Good luck! 🇴🇲**
