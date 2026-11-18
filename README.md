# AI to 3D printer (Berkeley maker space)

Design useful things with an AI helper and print them on the maker space
Bambu Lab X1C with the AMS (up to 4 colors). No CAD experience needed.

The AI writes a short Python script that builds your part. You run it, open
the result in Bambu Studio, and print. The hard part is not the software. It
is giving the AI real measurements and checking its work, so read
[GUIDE.md](GUIDE.md) before your first real print.

## What is in here

- [GUIDE.md](GUIDE.md): the process, a checklist and common mistakes. Read this first.
- [MAKERSPACE.md](MAKERSPACE.md): the printer, nozzles, build plates and filament in stock.
- [examples/clearance_test.py](examples/clearance_test.py): a 15 minute test print. Do this one first.

## Setup (about 20 minutes, once)

1. **Get an AI helper.** Claude (claude.ai or Claude Code) or ChatGPT both work.
   A tool that can run code for you (Claude Code, ChatGPT with code) saves steps,
   but a plain chat works too: you copy the script and run it yourself.
2. **Install Python 3.10 or newer.** Check with `python3 --version` in a terminal.
3. **Install build123d** (the free CAD library the AI writes code for):

   ```bash
   python3 -m venv ~/print-env
   ~/print-env/bin/pip install build123d
   ```

4. **Install Bambu Studio** (free) from bambulab.com. Pick the printer
   "Bambu Lab X1 Carbon" with the 0.4 nozzle when it asks.
5. **Try the example:**

   ```bash
   cd examples
   ~/print-env/bin/python clearance_test.py
   ```

   It writes `clearance_test.stl` next to the script. Open that in Bambu Studio.
   You should see a strip with four holes and a peg.

Optional, for Claude Code users: the build123d MCP server
(github.com/pzfreo/build123d-mcp) lets Claude render and measure the part
while it designs, so it can catch its own mistakes.

## Your first print, end to end

1. Run the example above and open the STL in Bambu Studio.
2. Printer: Bambu Lab X1 Carbon, 0.4 nozzle. Filament: Bambu PLA Basic.
   Process: 0.20mm Standard. Plate: match the plate that is in the printer.
3. Click **Slice plate**. Drag the layer slider to layer 1 and look: every part
   should touch the bed with a solid first layer.
4. Export or send to the printer the way the maker space staff show you.
5. Watch the first layer go down. If it is not sticking, stop and ask.
6. Try the peg in each hole. Write down the smallest gap that slides in.
   That is your clearance for future fits (see GUIDE.md).

## Asking the AI for a part

Start your chat with something like this, then talk through your idea:

> I want to 3D print a part on a Bambu Lab X1C (0.4 nozzle, PLA, bed 256 x 256 mm).
> Write a build123d Python script that exports an STL. All sizes in millimeters.
> Ask me for every measurement you need instead of guessing. Before you write
> code, tell me how it will sit on the bed, where the overhangs are, and the
> thinnest wall. Here is what I want: ...

Paste in [GUIDE.md](GUIDE.md) and [MAKERSPACE.md](MAKERSPACE.md) too, so it
knows the rules and what filament we have.

## Keeping this updated

Filament runs out, new colors come in, and settings change. This repo is only
useful if [MAKERSPACE.md](MAKERSPACE.md) matches what is really on the shelf.

**We need one maker space volunteer to keep it current.** About 10 minutes a
month:

1. Look at the filament shelf and the swatch board. Update the filament table.
2. Note any change to nozzles, plates or the printer firmware.
3. Change the "Last checked" date at the top of MAKERSPACE.md.
4. Add any new hard lesson (a failed print and why) to the common mistakes in GUIDE.md.

If you would like to do this, say so on the Vine post or message Kentaro, and
you will get edit access.

## Advanced

For multi-color projects with exact per-object settings, there is a fuller
pipeline (Bambu Studio command line, automatic G-code safety checks, one zip
per project). It is not needed to get started. Ask Kentaro if you want it.
