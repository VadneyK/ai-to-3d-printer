# Designing with AI without the slop

AI can write a part in seconds. It will also guess sizes, make walls too thin,
float pieces in the air, and tell you it is done. These steps keep you from
spending six hours of printer time on a part that does not fit.

## The process

1. **Talk it through out loud.** Use dictation (the mic button on your phone or
   computer) and describe the thing as if to a friend: what it is for, where it
   goes, what touches it, what it must hold. Talking gets out details you would
   skip when typing.
2. **Keep ideating before any code.** Ask the AI for two or three ways to build
   it and the trade-offs. Ask what could go wrong. Pick one.
3. **Think through the fit.** What does it attach to, slide over or hold? How
   does it sit on the bed? Which side faces down? Where would it break?
4. **Measure the real thing.** Use calipers (the maker space has them), not a
   photo or a spec sheet. Measure twice. Write the numbers in millimeters and
   give them to the AI.
5. **Iterate on screen.** Look at the part in Bambu Studio from every side
   before printing. Ask the AI to change one thing at a time.
6. **Print a small test first.** Cut out just the part that has to fit (a ring
   of the hole, one corner of the box, one clip) and print that. Minutes, not hours.
7. **Verify it works, then print the full part.** Test the fit with the real
   object. Only then start the long print.

## Checklist before you print

- **Units.** Every size is in millimeters. Check the size Bambu Studio shows
  matches what you expect (a 20 cm box that shows up as 20 mm is a units bug).
- **Real measurements.** Every number that has to fit came from calipers, not
  from the AI's guess. Ask the AI to list the numbers it assumed.
- **Walls.** At least 1.2 mm thick (3 lines of the 0.4 nozzle), 2 mm or more for
  anything that holds weight or gets squeezed.
- **Small details.** Raised or engraved text at least 5 mm tall and lines at
  least 0.8 mm wide, or the 0.4 nozzle cannot draw them.
- **Overhangs.** Nothing leans out more than about 45 degrees from vertical
  without support. Flat ceilings over 10 mm wide need support or a redesign.
  Better: turn the part so the hard side faces down.
- **Flat bottom.** A big flat face sits on the bed. Nothing floats, nothing
  balances on a point.
- **Clearance.** Parts that slide together need a gap. Start with 0.2 mm per
  side and use the result of your clearance test. Holes print a little small,
  so add 0.2 to 0.3 mm to hole sizes for screws and pins.
- **Strength.** Layers are weakest when pulled apart. Turn the part so the force
  runs along the layers, not across them. Clips and snap fits: use PLA Tough+.
- **Fits the bed.** Under 256 x 256 x 256 mm.
- **Slice and look.** In Bambu Studio, slice, check the time and filament, and
  drag to layer 1. The first layer should be solid and touch the bed everywhere.
- **Test print done.** A small piece of the tricky part printed and checked.

## Common mistakes

- **Trusting "done."** The AI cannot see the part unless it has a render tool.
  Look at it yourself every time. Ask "what is the thinnest wall?" and check.
- **Sizes from a photo or a website.** Real objects differ from their spec.
  Cardboard boxes flex and plastic does not, so a box sized to the spec can be
  too tight. Leave 3 to 5 mm of room around loose things like cards.
- **No clearance.** A 10 mm peg will not go into a 10 mm hole.
- **Thin walls and tiny text.** They print as gaps or blobs.
- **Printing the big part first.** A 10 hour print that is 1 mm off wastes the
  whole day. Print the test piece.
- **Multi-color text on a vertical face.** Every layer then needs a filament
  swap, which can turn a 1 hour print into 7. Put colored lettering on a face
  that prints flat (the top or the bottom).
- **Tall single-color parts next to multi-color ones.** They share layers, so
  the whole plate swaps colors on every layer. Give each color mix its own plate.
- **Wrong plate in the file.** Set the plate in Bambu Studio to the plate that
  is really installed, or the first layer will not stick.
- **Asking for a color we do not have.** Check [MAKERSPACE.md](MAKERSPACE.md).
- **Changing five things at once.** When something goes wrong you will not know
  which change did it. One change per round.

## When a print fails

- Stop it early. A bad first layer will not fix itself.
- Take a photo. Note the filament, nozzle, plate and settings.
- Ask the maker space staff before blaming the printer. Try a known good file
  (Bambu's built-in Benchy) to tell a printer problem from a design problem.
- Add what you learned to the common mistakes above so the next person skips it.
