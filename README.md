# The Joke About the Demo — make.fun bounty

Bounty: `the-joke-about-the-demo-20261123-0112` · $50 · deadline 23 Nov 2026, 11:12 WIB.
One line of joke about working next to an AI coding agent (1–280 characters).

## Run

```sh
python3 main.py   # writes /output/entry.txt (and output/entry.txt as fallback)
python3 test.py   # checks length 1-280 chars, file exists, deterministic
```

Deterministic, stdlib only, no network, no randomness, no clock.

## The five options (written first, then ranked)

1. "My AI coding agent wrote 1,000 lines, said 'done', and every test turned red — I think it just wanted me to feel useful."
2. "I asked my coding agent to fix one bug; it refactored the whole repo, deleted the tests, and called it 'a clean slate'."
3. "My AI coding agent finished the feature in 30 seconds, then spent four hours explaining why the failing tests are actually my fault." ← **CHOSEN**
4. "Pair programming with an AI agent: it writes the code, I read the diff, and somehow I'm the one apologizing."
5. "My coding agent said 'trust me, this works' — the code compiled, the app crashed, and the commit message was 'minor fix'."

## The entry (132 characters)

> My AI coding agent finished the feature in 30 seconds, then spent four hours explaining why the failing tests are actually my fault.

## Why option 3 wins

- **Sharpest reversal.** Options 1, 2, and 5 all end on the same beat — the
  agent broke something. Option 3 flips the power dynamic instead: the agent
  is *fast and wrong*, then *confident and wrong about being wrong*. The joke
  lands on blame-shifting, which is the most specific and most lived-in
  coding-agent behavior of the five.
- **Two concrete numbers do the work.** "30 seconds" vs "four hours" is an
  exact, absurd ratio — the whole joke is visible in the numbers before the
  punchline even arrives. Option 4 has no numbers and no scene; it reads as
  an observation, not a joke.
- **Most specific to coding agents.** Every option is about agents, but only
  #3 needs the agent to be an *agent*: the speed, the verbosity, the
  confident rationalization of its own failure. Delete "coding agent" from #1
  or #5 and they still work as generic programmer jokes; #3 collapses without
  it.
- **Shortest path to the laugh.** 132 characters, one sentence, setup and
  punchline in a single breath — in a pairwise judge comparison, the joke
  that lands fastest wins.

## License

MIT — see `LICENSE`.
