from typing import List

import fontconfig
import freetype

def find_patterns_covering(string: str) -> List[fontconfig.Pattern]:
    """Finds system fonts claiming coverage for all characters in the string.

    Notice this is usually done by blocks and doesn't guarantee there will be
    actual glyphs for all characters.
    """
    conf = fontconfig.Config.get_current()
    wanted_codepoints = {ord(ch) for ch in string}
    pat = fontconfig.Pattern.create (
        vals = (
            (fontconfig.PROP.CHARSET, wanted_codepoints),
        )
    )
    conf.substitute(pat, fontconfig.FC.MatchPattern)
    pat.default_substitute()
    finds, coverage, status = conf.font_sort(pat, trim=False, want_coverage=True)
    return finds


def has_glyphs(font_path: str, string: str) -> bool:
    """True if the font at path has glyphs for all characters in the string."""
    face = freetype.Face(font_path)
    for ch in string:
        if face.get_char_index(ord(ch)) == 0:
            return False
    return True


def sorted_unique(lst: list) -> list:
    """Returns sorted list without duplicates.

    We're forced to do stuff like this because OrderedSet isn't standard.
    """

    return sorted(list(dict.fromkeys(lst)))


def families_with_glyphs_for(string: str) -> List[str]:
    """Find font families which include glyphs for all characters in string."""
    candidates = find_patterns_covering(string)
    glyphed = [pat for pat in candidates
               if has_glyphs(pat.get(fontconfig.PROP.FILE, 0)[0],
                             string)]
    families = [pat.get(fontconfig.PROP.FAMILY, 0)[0]
                for pat in glyphed]
    return sorted_unique(families)
