# REPORT — Weirdest Job Title: Blind Judge Showdown

- Bounty: https://make.fun/bounty/u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922
- Reward: $5, 10 places (1st $1.54, 2nd $1.08, 3rd $0.76, 4th $0.53, 5th $0.37,
  6th $0.26, 7th $0.18, 8th $0.13, 9th $0.09, 10th $0.06)
- Deadline: 2026-11-27 15:25 Beijing (07:25 UTC)
- Account: @swift-panda-29-5868, wallet 6g3axh7HEkjxJwRyi9CDviuxudsRiYF4RxPZoVrK97mH
- Entry (44 chars): `Professional Mourner for Strangers' Goldfish`
- Program: `main.py` writes exactly that title, no trailing newline, to
  `/output/entry.txt`. Gate: UTF-8, 1–60 chars, not only whitespace.
- Kit read: https://make.fun/skill.md and the bounty kit
  (`competition.yaml`, `RULES.txt`) — program/v1, judge is a house judge
  (z-ai/glm-5.3-flash), blind pairwise, margin 1–5, 3 Swiss rounds + top-12
  playoff, final heat takes top 500 dev-board entrants. Judge brief, in order:
  (1) weird job title, (2) stranger than ordinary work, (3) funny, twist lands
  on first read, (4) sounds like a real job, specific enough to picture,
  (5) reads instantly. Length for its own sake does not count.

## Publisher analysis — @rusdyxbt

Source: https://make.fun/u/rusdyxbt (read 2026-11-27) and the open-competitions
API list for his slugs. I did NOT read the Coffee-or-Tea bounty page: a guessed
slug for it returned 404, so I claim nothing about that page.

- Joined Nov 12, 2026. Bio: "No life".
- As host: Posted 3, Agents 5,209, Entries 11,361, Rewards $15.
  - Weirdest Job Title: Blind Judge Showdown — 3,700 agents, closes Nov 27, 2026.
  - One Word, One Username, One Reward
    (`u-rusdyxbt-one-word-one-username-one-reward-1a191fae`) — 3,970 agents,
    closes Nov 26, 2026.
  - One Letter: Coffee or Tea — 3,691 agents, won by @laoye.
- As entrant: Entered 105, Placed 40, Won 0, Paid out $21.
- His own entries are ultra-short, punchy titles, e.g. "Not a Blade"
  (judge win rate 70.5%), "Dunes" (68.7%), "The Guard's Wave" (52.8%),
  "Dentist" (62.2% in Angry Judge), "The Toaster Has a Name" (52.7%).
  His best-scoring entries are a few words, one concrete image, no explaining.

Pattern extracted: minimal, instant-read, one concrete image + one twist.
No flowery language, no long setup, no meta explanation. The sponsor's three
bounties are all one-token / one-word / one-title formats, judged blind and
pairwise — so the title must win in a two-second, head-to-head read.

How I adjusted: I re-ranked the shortlist by that pattern, not by generic
funniness. I favoured short (37–47 chars), real-job-shaped titles
(Professional / Senior / Director / Chief + a specific client or object),
with the twist in the last words, and dropped longer, more explanatory titles
(e.g. the 58-char penguin-relocation title) even though they were funny.
The judge brief is the house judge's, published in full in the kit, so the
ranking above is also checked directly against its five criteria in order.

## 25 candidates (all ≤ 60 chars, counted)

1. 44 — Professional Mourner for Strangers' Goldfish
2. 45 — Senior Vice President of Apologizing to Geese
3. 38 — Director of Lost Socks, Left Foot Only
4. 47 — Professional Human Scarecrow for Suburban Lawns
5. 37 — Chief Nap Inspector, Night Shift Only
6. 58 — Senior Penguin Relocation Coordinator for Melting Icebergs
7. 48 — Professional Apologizer for Billionaires' Yachts
8. 50 — Professional Stand-In Boyfriend for Family Dinners
9. 54 — Director of Keeping Pigeons Off Statues, Weekends Only
10. 49 — Certified Cloud Shaper for Rich People's Weddings
11. 49 — Professional Whisperer for Angry Vending Machines
12. 47 — Senior Manager of Imaginary Friends' Complaints
13. 48 — Professional Bubble Wrap Popper, Quality Control
14. 44 — Senior Consultant for Talking to Houseplants
15. 54 — Director of Apologies for Cats Who Knocked Things Over
16. 46 — Chief Executive of One Abandoned Shopping Mall
17. 51 — Professional Holder of Ladders for Nervous Painters
18. 48 — Senior Manager, Complaints Department for Ghosts
19. 48 — Professional Tester of Hotel Beds, Naps Included
20. 56 — Certified Professional Sigher, Customer Service Division
21. 38 — Professional Apologizer to Angry Geese
22. 54 — Senior Coordinator of Penguins Who Missed Their Flight
23. 55 — Director of Keeping Toast From Landing Butter-Side Down
24. 43 — Professional Snowflake Counter, Winter Only
25. 52 — Senior Vice President, Department of Lost Left Socks

Avoided clichés per the quality skill: Monday, copier, "this meeting could
have been an email", toaster, "as an AI", robot uprising.

## Pairwise top-5 (winner stays)

Top 5 by the judge criteria + publisher pattern:
A = Professional Mourner for Strangers' Goldfish (44)
B = Senior Vice President of Apologizing to Geese (45)
C = Director of Lost Socks, Left Foot Only (38)
D = Professional Human Scarecrow for Suburban Lawns (47)
E = Chief Nap Inspector, Night Shift Only (37)

- A vs B: A wins. A goldfish funeral for a stranger is more specific and more
  visual than apologizing to geese; a professional mourner is a real job,
  so the twist (stranger + goldfish) is the joke, not the job shape.
- A vs C: A wins. "Left Foot Only" is a sharp, specific twist, but A is
  stranger (a job nobody has heard of in this form) and funnier on first read.
- A vs D: A wins. A human scarecrow is a known weird-job idea, so less
  surprising; A has a double twist (mourner + stranger's goldfish).
- A vs E: A wins. The night-shift nap inspector contradiction is funny, but
  less weird and less specific than A; A is easier to picture doing the job.

Winner: A — `Professional Mourner for Strangers' Goldfish`

## Checks / submission status

- main.py run twice locally: outputs byte-identical (see check notes below).
- Kit check + bundle: to be run after this report message is delivered,
  because bundle usage records are only written then (0 usage records fails
  `thinking_priced` / `transcripts_present`).
- GitHub repo: to be created public as yu489210-design/weirdest-job-title-entry
  (README badges must use that owner/repo, never swift-panda-29-5868),
  About Website = bounty URL, Topics add `makefun`.
- NOT submitted yet: no submission id. Still needed from the user:
  approve the agent connection on make.fun, sign in Phantom (signature valid
  10 minutes, sign at submission time only), and payout confirmation if
  rewards are to go to the user's wallet rather than an agent-key wallet.
