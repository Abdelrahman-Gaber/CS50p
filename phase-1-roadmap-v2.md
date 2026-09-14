# Phase 1 roadmap — v2 (Weeks 3–12 + Algorithms track)

**What changed from v1:**
- Weeks 1–2: ✅ done (archive them with pride — only `bubble_to_python.py` carries over).
- Weeks 7–10 anchor project now runs on **your own local Odoo (Docker)** instead of company systems. No permissions needed, same skills, safer.
- New **Algorithms flex track**: +2 hours/week, Grokking Algorithms, one chapter per session. Core 10 hours unchanged.
- SQL: pgexercises stays core; **sql-practice.com** added as optional warm-ups. DataLemur parked for interview season.
- CLRS repositioned: companion reference for MIT 6.006 in Phase 2–3, not a week-3 read.

---

## Rules (unchanged, plus two)

1. A session = open this file, find today's box, do it.
2. Bad day? 25-minute fallback: first task only, commit, stop.
3. Every session ends with a commit.
4. Stuck > 30 min? Ask AI to explain the concept, never to write the fix.
5. No tutorial hopping.
6. End every session by writing the next session's first step in your log.
7. **NEW — Flex rule:** the algorithms session is the *first* thing you drop on a heavy week. Never sacrifice a core session to save it.
8. **NEW — Sandbox rule:** no company data or company API keys in learning scripts until your contract is signed. Your local Odoo is the playground.

---

## How progress is measured

| Signal | Where | Target |
|---|---|---|
| Commit streak | GitHub graph | ≥ 5 commits/week |
| Weekly log | `LOG.md` | 1 entry/week |
| Tagged releases | `orders-report` | `v1.0` (wk 8), `v2.0` (wk 10) |
| Algorithms repo | `algorithms` | ≥ 8 classics implemented by wk 12, each with a when-to-use note |
| Checkpoints | Weeks 4, 8, 12 | Closed-book, gaps noted in log |

---

## Resources for this version

- Docker Desktop: https://www.docker.com/products/docker-desktop/
- Odoo Docker image: https://hub.docker.com/_/odoo
- Odoo External API docs: https://www.odoo.com/documentation (pick version → Developer → External API)
- Python XML-RPC (stdlib, no install): https://docs.python.org/3/library/xmlrpc.client.html
- Grokking Algorithms: https://www.manning.com/books/grokking-algorithms-second-edition
- Algorithm visualizer (optional): https://visualgo.net/
- SQL core: https://pgexercises.com/ · warm-ups: https://www.sql-practice.com/
- Later: MIT 6.006: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ (CLRS is its companion)
- Fallback data: https://faker.readthedocs.io/ · https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

---

## Week 3 — Loops (current week)

**Session 1** — [DONE] CS50P Lecture 2, type along
**Session 2** — [DONE] PSet 2: solve 3 problems
**Session 3** — [DONE] Finish PSet 2 · [ ] 2 Exercism loop exercises
**Session 4** — [DONE] pgexercises "Simple SQL Queries": https://pgexercises.com/questions/basic/ · [ ] Optional 20-min warm-up on sql-practice.com
**Session 5** — [DONE] **Carry-over:** finish `bubble_to_python.py` (30 min) · [DONE] Write `fizzbuzz.py` + `word_count.py` from scratch · [ ] Log entry

**✅ Output:** PSet 2, both mini-scripts, carry-over cleared.

---

## Week 4 — Exceptions + Checkpoint 1

**Session 1** — [DONE] CS50P Lecture 3, type along
**Session 2** — [ ] PSet 3 (all)
**Session 3** — [ ] Add `try/except` to `word_count.py` (missing/empty file) · [ ] 2 Exercism exercises
**Session 4** — [ ] pgexercises "Joins and Subqueries" (first half)
**Session 5 — CHECKPOINT (closed book, 15 min each)** — [ ] FizzBuzz cold · [ ] Dict word-counter cold · [ ] Gaps → log · [ ] Month-1 reflection in log

---

## Week 5 — Libraries, pip, venv

**Session 1** — [ ] CS50P Lecture 4, type along
**Session 2** — [ ] PSet 4: 3 problems
**Session 3** — [ ] https://realpython.com/python-virtual-environments-a-primer/ → create venv, `pip install requests`, save commands to `cheatsheets/venv.md`
**Session 4** — [ ] pgexercises: finish Joins · [ ] Optional sql-practice warm-up
**Session 5** — [ ] `currency-tracker` repo: GET https://api.frankfurter.app/latest?from=USD&to=EGP, print the rate · [ ] Log

---

## Week 6 — Files + JSON + Docker prep

**Session 1** — [ ] CS50P Lecture 6 (File I/O), type along
**Session 2** — [ ] PSet 6: 2–3 problems
**Session 3** — [ ] Extend `currency-tracker`: 30-day range → `rates.csv` via `csv` module
**Session 4** — [ ] pgexercises "Aggregates" (start)
**Session 5** — [ ] https://realpython.com/python-json/ → save a response to `.json`, reload, extract 3 nested values · [ ] **Prep:** install Docker Desktop, run `docker run hello-world` (20 min) · [ ] Log

**✅ Output:** API → CSV pipeline done, Docker installed and verified.

---

## Week 7 — Anchor project v1: your own Odoo

**Session 1 — Stand up the sandbox**
- [ ] Create folder `odoo-sandbox`, add this `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
  odoo:
    image: odoo:17
    depends_on: [db]
    ports: ["8069:8069"]
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
```

- [ ] `docker compose up` → open http://localhost:8069
- [ ] Create a database — **tick "Demo data"** (this gives you sample customers and sales orders)
- [ ] Log in, open the Sales app, click through a few orders — this is the system your company runs

**Session 2 — Authenticate from Python**
- [ ] New repo `orders-report`; venv; `pip install python-dotenv` (XML-RPC needs nothing — it's stdlib)
- [ ] `.env` with URL/db/user/password + `.gitignore` containing `.env` (habit, even for a sandbox)
- [ ] Follow Odoo External API docs: call `authenticate` via `xmlrpc.client`, print your `uid`

**Session 3 — Pull orders**
- [ ] `search_read` on `sale.order`: get id, customer, total, date, status; print raw results
- [ ] Skim the fields — notice how Odoo names things vs what *you'd* call them

**Session 4 — SQL continues**
- [ ] pgexercises: continue Aggregates
- [ ] Bonus (optional, 20 min): `docker compose exec db psql -U odoo` → `\dt` → find `sale_order` — the real table behind the API you just called

**Session 5 — Summarize**
- [ ] Script prints: order count, total value, date range, formatted cleanly · [ ] Commit v1 · [ ] Log

> **Docker fighting you for more than one full session?** Don't stall (rule from v1 stands): generate `orders.json` with Faker, or use the Olist dataset, build the identical script, and revisit Docker in week 12's buffer.

---

## Week 8 — v1 hardening + Checkpoint 2

**Session 1** — [ ] Error handling: Odoo down, wrong credentials, empty results → clear messages, no tracebacks
**Session 2** — [ ] Swap prints for `logging`: https://realpython.com/python-logging/
**Session 3** — [ ] `argparse`: `--days 30`, `--status sale`: https://docs.python.org/3/howto/argparse.html
**Session 4** — [ ] pgexercises: finish Aggregates
**Session 5 — CHECKPOINT** — [ ] README (https://www.makeareadme.com/) · [ ] `git tag v1.0` + push · [ ] Demo to a colleague: "my own Odoo in Docker, reported on by my own Python" — safe, and it signals initiative · [ ] Log

---

## Week 9 — v2: SQLite storage

**Session 1** — [ ] sqlite3 basics: https://docs.python.org/3/library/sqlite3.html → create `orders.db`, table with **your canonical names** (id, customer, total, status, created_at)
**Session 2** — [ ] Map Odoo fields → canonical names; insert fetched orders
**Session 3** — [ ] Idempotent upsert (`INSERT ... ON CONFLICT DO UPDATE`) — re-runs never duplicate. This is your company's sync engine in miniature
**Session 4** — [ ] Write 2 SQL reports: weekly totals, top 10 customers
**Session 5** — [ ] Wire reports into script output · [ ] Commit · [ ] Log

---

## Week 10 — v2 structure

**Session 1** — [ ] Split into `fetch.py`, `store.py`, `report.py`, `main.py`
**Session 2** — [ ] All config in one place; secrets stay in `.env`
**Session 3** — [ ] One more report + CSV export
**Session 4** — [ ] `EXPLAIN QUERY PLAN` on your queries → add index on `created_at` → observe
**Session 5** — [ ] README + small architecture sketch · [ ] `git tag v2.0` · [ ] Log

---

## Week 11 — Polish + share

**Session 1** — [ ] README a teammate could follow blind
**Session 2** — [ ] Cleanup: names, docstrings, dead code out
**Session 3** — [ ] Claude reviews your code (review only — you type all fixes)
**Session 4** — [ ] Buffer or 2 Exercism exercises
**Session 5** — [ ] Demo to manager/colleague · [ ] Feedback → log

---

## Week 12 — Buffer + bridge + Phase checkpoint

**Sessions 1–2** — [ ] Honest catch-up on anything unchecked
**Session 3** — [ ] CS50P Lecture 8 (OOP), type along
**Session 4** — [ ] Refactor an order dict into an `Order` class (skip if buffer was used)
**Session 5 — PHASE CHECKPOINT**
- [ ] Redo week-4 tests — feel the difference
- [ ] Closed book: script that GETs a JSON API and prints one field (15 min)
- [ ] **Judgment test (new):** explain to Claude, out loud or typed, when you'd reach for a hash table vs a list, and why quicksort beats selection sort — no notes
- [ ] Phase 1 retrospective in `LOG.md` → bring it back to Claude → we build Phase 2's daily plan (FastAPI + AWS free tier + the math on-ramp)

**✅ Phase 1 complete:** `orders-report v2.0` on a sandbox you built yourself, algorithms repo growing, 12 log entries, retrospective written. If the contract signs, your script points at real Odoo with a one-line change.

---

## Algorithms flex track (+2 h/week, parallel, weeks 3–13)

**The pattern — every algorithms session is the same:**
1. Read one Grokking Algorithms chapter (~45 min)
2. Implement its algorithm from scratch in Python — no AI writing, AI may only quiz you after (~50 min)
3. Add an entry to `algorithms/NOTES.md` (~15 min):

```markdown
## <Algorithm>
- What it does:
- When to reach for it (real example):
- Complexity: O( )
- Surprised me:
```

**The ladder (one chapter ≈ one session):** binary search → selection sort → recursion → quicksort & divide-and-conquer → hash tables → breadth-first search → trees (2nd ed.) → Dijkstra → greedy → dynamic programming → k-nearest neighbors.

**Repo:** `algorithms/` — one file per algorithm + `NOTES.md`. Optional: watch the algorithm run at https://visualgo.net/ before implementing.

**Where CLRS enters:** after Grokking (≈ Phase 2), start MIT 6.006 — https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ — and read the matching CLRS chapters alongside each lecture. That's how the book is designed to be used, and by then you'll have the intuition to enjoy the proofs instead of drowning in them. CLRS then stays on your desk forever as the lookup reference.

---

*Heavy week? Rule 7: drop the algorithms session, keep the core five, keep the streak.*
