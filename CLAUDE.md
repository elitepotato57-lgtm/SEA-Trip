# SE Asia Trip app

A phone web app for Dylan and his mates' Southeast Asia backpacking trip (landing Bangkok 27 Nov 2026).
It is one self-contained `index.html`, served by GitHub Pages from the root of this repo and installed on
iPhone home screens as a PWA. No accounts, no backend. Dylan is not a developer: explain things plainly,
and do the git work for him.

## Layout

- `index.html`, `sw.js`, `manifest.webmanifest`, `icon-*.png`: the live site. `index.html` is BUILT, never edit it by hand.
- `config.js`: holds the Google key on GitHub. It may not exist in a fresh copy of this folder. See rules below.
- `src/template.html`: all the app's HTML, CSS and JavaScript. This is where code changes go.
- `src/data.py`: all data outside Thailand, exchange rates, cross-border routes, the journey-planner network
  (STATIONS, HUBS, EDGES, TAXI, GO12). It ends by running `thai.py` and writing `data.json`.
- `src/thai.py`: the deep Thailand data (21 destinations, 361 places) plus extra hubs and connections.
  Uses helpers `TG` (gaff), `TM` (munch), `TC` (activity). Copy the existing entries' shape exactly.
- `src/countries.json`: simplified country outlines for the offline map.
- `src/vendor/`: Leaflet 1.9.4.
- `src/build.py`: the build. `src/tests/test.js`: the functional test.

## Commands (run inside `src`)

- Build: `python build.py` (needs Python 3; writes `../index.html`)
- Test: `npm install` once, then `node tests/test.js` and `KEY=AIzaTEST node tests/test.js`
  (on Windows cmd: `set KEY=AIzaTEST&& node tests/test.js`). The second run fakes Google to cover photos,
  ratings and the translator.
- Known stale test expectations, not app bugs: "Home-screen mode stretches app", "Settings sections",
  and "Google live suggestions" in the keyed run. Fix the tests rather than the app if you touch them.
- Publish: commit and push to `main`. GitHub Pages redeploys in a minute or two.

## Every change

1. Edit `src/template.html` and/or the data files.
2. Bump `const VERSION` in `template.html`.
3. Build, run both test runs, confirm no JavaScript errors.
4. If `sw.js` changed, bump its `APP` cache name.
5. Commit and push. Tell Dylan to close and reopen the home-screen app twice to pick up the update.

## Rules

- NEVER commit a `config.js` containing the placeholder over the real one, and never delete it. The real key
  lives only in the repo's `config.js`. If the file is missing locally, pull from GitHub rather than recreating it.
  `src/config-template.js` is the blank template.
- The key is restricted to the GitHub Pages address and to Maps JavaScript API, Places API (New) and
  Cloud Translation API. Photos never load from a local file or localhost; that is expected.
- Keep Google costs at zero: Text Search requests ask for IDs only, list cards fetch only `photos`,
  results are cached in localStorage. Do not add fields or calls without checking the free tier.
- No Buddha imagery in the country themes. This was a deliberate choice.
- Every researched fact needs a source link in the data. Do not invent prices, hours or places.
  Unpriced transport legs are flagged "check live". Pins are approximate (`ap=True`); Google snaps them.
- Prices show local currency first with pounds underneath.
- Must keep working offline after first load, and on a 393 px wide iPhone screen.
- Tabs are Map, Gaffs, Munch, Activities, Transport, Tools; Settings is behind the cog. Dylan removed the
  budget tracker, country toggles and the translator's copy button on purpose. Do not bring them back.
- The test location defaults to Bangkok for pre-trip testing. Leave it until Dylan says to turn it off.

## How the app behaves (so you do not re-derive it)

- Lists sort nearest-first with distance chips 2/10/50 km/Anywhere.
- Transport is a journey planner over the hub network in the data. It hides any option beaten on both time
  and price by another. Places outside Thailand fall back to a Rome2Rio link and the saved cross-border routes.
- 12Go links are per leg: `https://12go.asia/en/travel/{from}/{to}` using the `GO12` map.
- `sw.js` is network-first for the page with a 5 second timeout, then cache.
- iPhone home-screen mode: `fitStandalone()` plus the Settings "Screen fit" toggle (`.fill-bottom` CSS) try to
  close a gap under the tab bar. Unverified on a real phone.

See `TODO.md` for what is next.
