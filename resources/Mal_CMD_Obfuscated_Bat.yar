rule Mal_CMD_Script_Obfuscated_Bat {
    meta:
        description  = "Detects .bat file obfuscated using superfluous %variable% substitution"
        author = "Original by Florian Roth, modified by Wes Lambert"
        score = 70
    strings:
        $h = { 40 65 63 68 6F 20 6F 66 66 0A 73 65 74 20}
        $s = "%%"
    condition:
        uint16(0) == 0x6540 and filesize < 200KB and
        $h at 0 and
        #s > 3
}
