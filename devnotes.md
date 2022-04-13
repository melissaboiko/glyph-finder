Only by putting up this barely functional code I realised it's actually two distinct things:

 - A tool to find fonts that contain glyphs for the characters you want, and
 - A tool to show a sample in different fonts.

There’s a variety of software already for the second one, though none I like.  It seems that somehow programmers never cared to read even an introduction to typography? Like, no Linux font browser I’ve ever seen lets you do something like ‘show me old-style or slab serifs with true small caps and case forms, at least 5 weights, and a large x-height’.  And it’s not like I'm a designer, I literally merely read an introduction to typography once, years ago.

I have tried before to hack together some font displays, and found it really hard to convince toolkits like gtk or qt etc. to *not* do fallbacks of any kind.  But that’s a moot point here, if you filter it for matching fonts in the first place.  I don't know why I obsessed with that.  I guess I just don’t like the way toolkits take away control.

For the filter task, one might expect fontconfig to do the job.  The lbirary UI is *exceedingly* clunky but it does have a way of doing that (and thanks python-fontconfig author for detailed examples).  I find, however, that many fonts that claim to cover this unicode character don’t actually have anything in there—I think they go by blocks; like, they’ll say they have the Latin set but not be able to render ǚ, for example.

The old snippet that I had saved in my $home.git got around this by rendering the text in pango, then examining a return parameter that counted the number of glyphs missed.  That works, but it’s very slow.  After some digging around I found out that freetype has a very useful feature for our purpose: It normalises glyph index 0 to mean ‘default glyph’ for all fonts.  So you can just look up `get_char_index()` for every char, and the first one that returns 0 means this font is a no go.  Plus I kept the fontconfig filter attempt for a first pass, not just to get the font file paths but to weed out irrelevant fonts.  The end result is fast, or at least passably so on my system.

In an ideal world I would do the filtering functions in rust, and the drawing functions in something that is neither python nor qt, though I don’t know what.  Directly rendering text images in freetype and aligning them in some reasonable minimalistic interface, maybe.
