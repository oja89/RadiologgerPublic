#use this to store the already searched words so we dont need to ask them again from API

## words found from UMLS database
found_db = ["report", "case", "uterine", "artery", "pseudoanerysm", "woman", "weeks", "gestation", "room", "lower", "left",
            "quadrant", "pain", "vaginal", "bleeding", "ultrasound", "presented", "emergency", "adnexal", "mass", "consistent",
            "percutaneous", "thrombin", "injection", "chosen", "avoid", "contrast", "radiation", "risk", "fetus", "demonstrated",
            "thrombosis", "evidence", "fetal", "distress", "postprocedure", "day", "patient", "similar", "complaints",
            "found", "decision", "made", "treat", "computed", "tomography", "coil", "embolization", "procedure", "successful",
            "angiography"]

## words not found from UMLS database
not_found_db = ["primigravid", "revealed", "recanalized", "revealed"]

## mild synonyms and related words from Merriam-Webster https://www.merriam-webster.com/thesaurus/mild
mild_words = ["mild", "balmy", "clement", "equable", "genial", "gentle", "moderate", "soft", "temperate", "clear", "cloudless", "fair",
"rainless", "sunny", "sunshiny", "calm", "halcyon", "peaceful", "placid", "tranquil", "delightful", "fine", "pleasant"]

## moderate synonyms and related words from Merriam-Webster https://www.merriam-webster.com/thesaurus/moderate
moderate_words = ["moderate", "temperate", "controlled", "curbed", "disciplined", "inhibited", "restrained", "self-controlled",
"self-denying", "self-disciplined", "calculated", "deliberate", "measured", "levelheaded", "rational", "reasonable",
"sensible", "average", "mediocre", "medium", "modest", "run-of-the-mill", "run-of-the-mine", "run-of-mine", "so-so",
"normal", "ordinary", "regular", "routine", "typical", "usual", "average", "intermediate", "mean", "median", "medium",
"middle", "middling", "midsize", "midsized", "modest", "reasonable", " common", "commonplace", "conventional",
"normal", "popular", "regular", "routine", "standard", "typical", "usual", "adequate", "passable", "tolerable"]

## severe  synonyms and related words from Merriam-Webster https://www.merriam-webster.com/thesaurus/severe
severe_words = ["severe", "austere", "authoritarian", "flinty", "hard", "harsh", "heavy-handed", "ramrod", "rigid", "rigorous", "stern",
"strict", "tough", "austere", "authoritarian", "flinty", "hard", "harsh", "heavy-handed", "ramrod", "rigid", "rigorous",
"stern", "strict", "tough", "austere", "dour", "fierce", "flinty", "forbidding", "grim", "gruff", "intimidating",
"lowering", "louring", "rough", "rugged", "stark", "steely", "stern", "ungentle", "bleak", "cold", "hostile", "inhospitable",
"inimical", "unfriendly", "unsympathetic", "adamant", "bound", "determined", "firm", "intent", "purposeful", "resolute",
"resolved", "steadfast", "unflinching", "fixed", "hard", "hardened", "hardheaded", "immovable", "implacable", "inflexible",
"ironhanded", "mulish", "obdurate", "obstinate", "rigid", "self-willed", "set", "stiff", "stubborn", "unbending",
"uncompromising", "unrelenting", "unyielding", "willful", "wilful", "immutable", "unchangeable", "black", "cheerless",
"dark", "gloomy", "glum", "joyless", "melancholic", "moody", "morose", "sulky", "sullen", "surly", "brooding", "grave",
"humorless", "melancholy", "serious", "sober", "sobersided", "solemn", "somber", "sombre", "staid", "unsmiling", "weighty",
"earnest", "grave", "humorless", "no - nonsense", "po-faced", "sedate", "serious", "sober", "sobersided", "solemn", "staid",
"uncomic", "unsmiling", "weighty", "harsh", "stern", "strict", "businesslike", "professional", "dignified", "distinguished",
"elevated", "serious-minded", "gloomy", "grim", "bitter", "brutal", "burdensome", "cruel", "excruciating", "grievous",
"grim", "hard", "hardhanded", "harsh", "heavy", "inhuman", "murderous", "onerous", "oppressive", "rough", "rugged", "searing",
"stiff", "tough", "trying", "austere", "bleak", "comfortless", "discomforting", "forbidding", "inhospitable", "spartan",
"uncomfortable", "biting", "inclement", "intemperate", "wild", "rigorous", "strict", "stringent", "agonizing",
"heartbreaking", "heartrending", "painful", "wretched", "crushing", "grinding", "overwhelming", "wearing", "insufferable",
"insupportable", "intolerable", "unbearable", "unendurable", "harrowing", "tortuous", "bad", "disagreeable", "hostile",
"unfriendly", "unpleasant", "    arduous", "Augean", "backbreaking", "challenging", "demanding", "difficult", "effortful",
"exacting", "formidable", "grueling", "gruelling", "hard", "heavy", "hellacious", "herculean", "killer", "laborious",
"moiling", "murderous", "pick-and-shovel", "rigorous", "rough", "rugged", "stiff", "strenuous", "sweaty", "tall", "testing",
"toilsome", "tough", "uphill", "abstract", "abstruse", "complex", "complicated", "elusive", "hairy", "insoluble", "intricate",
"involved", "knotty", "opaque", "problematic", "problematical", "recondite", "serious", "spiny", "stubborn", "thorny",
"ticklish", "tricky", "bruising", "burdensome", "exhausting", "labored", "onerous", "oppressive", "stressful", "taxing",
"tight", "trying", "annoying", "bothersome", "distressing", "irksome", "troublesome", "vexatious", "grievous", "grim",
"strict", "stringent", "brutal", "cruel", "inhuman", "painful"]
