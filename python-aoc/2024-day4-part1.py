import re

input = """AAMXMASASMXSAMXXSAMSAMXXSXMMSMMSXSASXSXSSSXSAMXXXSXMASXMAMMASAMXAXAXMXMSSMMSXSASXSAMXXMASMXSMMMMMXXMAXXSXXXAXMSAMXSMXMSXSAMXMXMSXMMXSMXMXSMS
AXMASXMAASAMMMSMSAMSAMXMAXMAAAMXMASAAMMMAAAMMXMASMAMAMASMSAASXMAXMMXASAMXAAAMSAMMMAMMMXMASASAXXASMMMMSAMMMXMASXMASMSMMMAMMMMMAXXAMXAXMAMSAAA
XMSMMAMXMMSMAAAAMAMSAMXAMAMSSSMXAMMMSMAMMMMMSASXAXAMASXMAAMXXMSMXSAMXSMMSMMSMMAMASAMMAAXSMMSAMSMMAAAMMAMAASMMMXMMXMASAMAMSMSSSSSSMMXSXMXAMXM
SAMXSAMSXMASMSSMSMMMMMMAMMMMAMASMXSAAMSMMAMXSASMSSXSASMMSMMMSMAAAXAAAXAAMAMXASMMMSASXSMSMMXMXMAXMSMSSSSMSMXAASMMAASAMXSASAAXAAMXAASMMASAMXAX
ASAASXMMAXAXMAXXAXAXASAMXAAXMMMMMAMXSXMASXSMMMMAAMXMASAAMXSAAMMAMSSMSMMMSSMSMMXMXSXMAXXAAXMMSSMSXMAMAAAAXMSSMXASXXMMSMSMSMSMMMMSSMMASAMAXSSS
MMMMSAXSAMMXSASMMSMSAXMASMSMXAXAMXMXXASAMXAMXXXMAXAMXSMMMXMXSMXAXMAAXXSAAXMAMXXMMSAMXMSSXMAAMAAAMMAMMMMMMMAMAMXMXAXXAASAMXAAXXXXMAMMMMSXMAAX
XMAMXMXMASXAMMSAXAAMAMSASMXXSXSXSAMXMAMSMSAMXSMSASXSAMXSMASAXASMMSMMMAMMSSSMSMSMASXMAMMAMSMMSMMMMSASXXAAAMAXXMXASMMMMSMAMSMSMMMXMMMSXMSMSMAM
SSMSAXSMASMMMASMMMMMXMMASAMASAAMSASAMXMAMMAXXAAAAMASXSASMXMASAXXAAAAMAMAAAMXAASMAMASMSMAMXAAMXSXASASASXSSSSMSXMASXAAXAXSMSMAAAMMASASAAXAXXAX
AAAMXMXMAXAXMXXXXXXXXXMMMXMAMXMXMASXMXSASMSMXMSMSMXMAMASAMMMMXMMSSSMSXSXMMSXMSSXMSMMMAMMSMMMSAMMMMAMAMAAAAXAXMXAXMSMSAMXAMMSSMAAXMASXMMSMSAS
MMMMSSXMASMXMASMMMXSXMMMAXMSMSXAMMMXMASASMMMAAAMXMXMXMXMMMXAMASXMAMAXMMMXMAASAXXXAXASASMSXSAMMSAXMAMAMMMMAMMMAMMMXAXMMMMAMAAAMXSXMXMAMAXXSSM
XMAAMAAMAMMAXAAAAXAMMAAMAMMMAXMXSAAAMAMMMAAXXMMMAMAXMASMMSMASAMMMMMMMAAAMMSSMASMSMSXSAMAMSMASXSMSSSSSMSAMXMXASAMXMSMMSASASMMXXMMMXAXAMMSMMAS
MSMSSSSMMSXMMMSSXMMSASXSSMSMMMMMMMSMMASASMMSSMXSASXXSASAAXSXMMXMAAMXSSSXSAXXMAMXAAAXMAMMMASMMMXAXAMAAASXSMXASXXAAAAAXSXSASAMSAAAAMMSXXXAAXAM
XAAAAAXXAAMSXMAMXXMAMMAAAAAAAAAAXAXAXXXXMAAAAAASAMAAMASMMXAMXSASMMSAAAAAMXMXMXSSMSMXMAMAMAMMAMMMMAMXMMMMMAMXXMSSMSSSMSMMAMAAASXMSXMAASMSSMXS
SMSMMMMSMXMXAMASMMSSMMMMMMMXMSSSMSSMMSSSSMMMMMMSAMMMMAMAXSAMXSASAAMMMMMMMMMXMAAAAAXSSMXSMSSSMMAAMAMXXAAAMXXAMXAAMMAAXXAMXMMMMMXMAASMMMAAXXXX
SAMXMAMSMSMXAMAMAAXASAAXXXSAAAAAAAXMAXAAMXXXXAXMASXAMASXMMASXMAMMMMSASXMAAXAMXXMSMSAAXAMXMAAASXMSMSASMSMSAMSSMSSMMSMMSSMAXXAXXAMSXMAAMMMMMSM
SAMXSASXASAASMSMMMMMSXXSAASMMMSMMMSMSMMMMXMMSMSXAXXXSAMXASAMAXSXXXASMSASXSSSXSXXAXMMMMMSAMMMMSAAXAAXAAMAMMSAAAAXAXAXAXMMSMSAXSMMMMSSMSXSXAAA
MAMXSSSMXMAMMAAXSXMXXXXMXMMASAXXSXAAXMMMXMXXAMXMMSSMMMMSXMASMMMMMMAMASXMXAAAASXXXXXAMAMMAMXSASMMMXMSMMMAMSMXSMMSSMMMSSSXMASXMXMAAMAAAXAXMASM
SSMMMAXAMXMMMMMMMAXAXSSMMXSAMXMMSSMMMAAXAXXSSSSXSAMXSAAMMXAMMXMAMMSMAMXSSMMMMMAXSMSSSSXSASXMASAMSAMXAASMSSXMMAXXMAAAMAMAMXMMMASXSSSMXMXMAMXM
MASXMMMXAAMAXMASMMMXSAAAAXMAMXMAMAXXSXMXMXMXMAMSMASAMMSMAMSMSAMMSAAMAMAXAAXXXMSMAAAAAAASAMXMXMAMSXSSXMASAXAAXMXSSSMSMASXMAXAMXSAMAMXSMMSXMAX
SAMXMXMXSXSAMAAAAAAXAMMMMXAXMAMSSSSMXAMASAMAMAMAXSMXSAXMAXMASXSAMXSMMMSSMSXSMMASMXMMMMMMAMMSASAMXAAMMSMMMSMMXMAMAXMXXMMMXMMSMMMAMXMASXAAAMXM
MASASASMMASMSMMXSMMXMXMMMMMMMXSXAAXMAXSASASASXSMMMAXMAMSSSMAMAMMSAMAXAXXXXAAASASXSXAAXXMAAMSXSASMSMMMMMAMMAMXMASMSMSMSMSASMXAASAMAXMXSXSAMXA
MXSASAMAXAXXAXMXMAMXMAXSAAXAXMMMMMMMXXMASXAASAAXAMXMXAXXAXMAMAMXMAMSMMXSAMMMMMMSASXSXSXMASXMASXMXAMXAAMAXSAMXSASXAAAAAXXAMASMMMASMSXAMMAMSSS
XXMMMMSSMMSSMXXAXMAXXAXXXMXMSAMMMXMSXAMAXXMSMMMMXXMASMXXMASMSXSASXAMAMAMASMSMAXMXMXMXMAXAMAMAMXMASXSSSMSXSXSXSXSXMSMSMMMAMAMAASMAMMMASAMXAAM
XMASAMXMAXAAAAMSMSMSMSXSASAXSAMAXSAMSXMASMXAASXMXSXXAXSXXXMASASASAMSAMXSAMXASMSMXMASXMXSASXMMXMXAMXMAAAMASMSXXAMMXAXXAXSMMMSXMMSXAMMMSXSMMXM
XSAMXSASMMMSMMMXAAAXAAAXASMXXSMAMMAMXXXXXAMMXMASAMXSXMASXXXXSXMXMAXSAMAMASXMMMAMAMAAAAASAMXXSASXSSSMMMMMASAMMMMMMXAMXMMXAAASASMMSXASASASASAS
MMASXMASXAXAXXAMSMSMSMAMXMXXMXMMSSSMSSSMXMAXASMMXXMXAMMMMMSASXSASAMXAMSXMMAAASASXMASMMMMAXAXXASXAAXXXMXMAMMMAXMAMMSMXMAMMMXXAMAAASMMASASAMAA
AXAMAMAMMSXMSMSMAXXAXXMAXMMMXXAMAMAMAAAXSXXSAMAMSMSAMMXSAAMMMAXASAXXSAXAXSSMMSMSASXXMASXSMMSMSMMMMMMAXAMAXMXSXMAMMXAAMMMSMSMASXMMAXMMMAMMMSM
SMSSMMASXMAXXAAXMSMXMAMSMXAASMSMASMMMSMMXAAXASMMAAAAMSXMMMXAMAMXMXSAMASAMXXAAXASAMXMSASMXAAAXAAXMAAXXSXSASMMMASMSSMMMSXAAAMSAMASXMASMMSMSAMX
XMAAASXSASAMMSMXSAXAXXMAXSMSMAASAMAAAAXMMSMSAMASMXMSMXAMASXMMASAAXMXMMMMMMSMMSXMMMAAMASXSSSMSSSMMMSMXXAXAAAASAMXAAXSAMXXMMMMXSAMXXAMAMMAMASA
MMMSMMXMMMMMXXAXSAMMMSSMXXXXMSMMSSSMSSSMAAXMASMMXMSAMSXMAXAXSAXMSMMXSAAAMMAAAXAAXSSSMAMXAMXMAXAASAXAXMSMSSSMXAMMMMMMASMSXSASMMASMMMXAMMAMMMM
SAAXAMAMXAMXXMSMMAMXMAASAMXSAMXSAXMAXXMMSSMSAMXMAXMAMSAMSSMMMMMMAAXASMSMSMSSMSSMMXXAMASXMXAXMMSMMASAMAAAMMXMSMMAXXXSAMXAXSAMAXMMXAASXSSSSSXS
MMXSAMAXSASAMXXASAMXMSSMMAAMAMXMASMMMAMXAAAMMSSXMSSMMSAMAAXAASASMSMMSAXXAMMAMMAASXSXMXMASAMXMAMAMMMXASMMMXSMASMMSAMMMXMMMMMMSXMMMMMSXAAAAAAX
XXASAMAMXXMASASMSASXMXMASMSXMASXMAXASAMMMSMSXXMAMMAAAMAMSSMMMSAXAAAXMAMMMXXAMSXMMAMSMASMMMXSMASAMXAXMXXSAMASASMAXXMASAMXAAXAMMMMASXMMXMMMMSS
SMMSXMMMSMSXMASAXMMXMASMMAAXXAXAXMAMMASMAMMMXASXMSSMMSAMXAASMMMMSSMMMAMSXSSMMSMMMXMAMAMAMXXMXXMAMMSXMAXMAMAMXSXAXXSAMASXSSMMSMAAMMAAXMXAXXAX
SAXXMAMAAASMMAMMSXMASASAMMMMMSSSXMMSSXSMMSAAMXAMXAMAMSMSSXMXAAXXAAASXSXSAMXMAMAXAXSAMSSSMSMAMMSSMXXAMXMXMMXXAMXMAMMMSXMMXAMAAXXSXSSMMASXSMMM
SXMASAMSSMMSMXSMAASASMSAMMXSXMAMAAAXMXSAMSMMSAMAMMSSMXAAXMASMMMMXSMMXMAMXMAMAMXMXAMXSMAXAXAAMMAMXASXMAAASMXSASAMMAAXAAMXSAMSMSXMMMASAMXAAMXS
MAMXMAMAAAASXXMMSMMAMAMAMXMMAMAMXMMXXAMAMXSAMXMXSAAASMMMXSAMXAASMMMXSMMMAMMXSSMMXMASAMAMSMXSSMXSMMSASMSMSAASASXSXSMMXAAAMAMXXSASASAMSSMMMMAX
SAMXSSMSSMMSMXXAMMMMSMSSMMAXXMSSXSMXMASAMXMSMSAMMMSSXXMAMMASMXXXAMXAMAASXMSAAAAXASMSAMXSAAAXAMAXMXXAMXAXMMMMXMMAMAAXSMMXSMMXAMAMAMASXSAAAMXS
SASAAAAAAMXSASMMSAAAAXXMASMXMXXMASAASXMASXMAMAAAXXMAMXMASXXMASMSMMMSMSMSMAMMXMMSMSAXXMXMMMMMAMXSMSMSMSXMXXXMASAMXSAMXAMMSAMMSMSMMMXMAMSMSSMS
SAMXSMMSSMAMXSAASMMSMXXMMMSAMSAMMMSMSASXMMSASMMMMMMMSXSMSAMXAAAAASAXAMMXMAMMXSAMXMAMXSAMXAMSXMAAAXAAXAMXMXAMMASXAMAMXXMAXAMAMXMAMMMMXMAXXXAM
MXMXXXMXMMXSAMMMSAMAMSMMSASXMASMAMAXSAMAAAMXSXAAXAMXMASXSXMAMMMSXMAMXMAXXXSAMXASMSXMXAMMSAXXMMSSSMSMSMXSAMXMXMMMXSAMXSSSSSMXXAXMMAASMXXSMMSM
SMMMXMMAAMMMMXXXXAMAXSAXMASXMAMSXSXXMMMMMMXSXMSMSXXAMXMASASXXMAXAMAMMMMSMAMXMSMMAMMMXMMAMSAAXAAMAMXAXAMXSMAMAXXAAXMMXMAMXAASMSSMSXXSAMXAAMAM
AAAAAXSSMSAAMASXMSMSSMSMMSMXMAMMMXMMAMSXAXMXAMXAAMXMMAMMMAMXASAMXXMSAAAAMAMMMSSMAMAXASMXXMSMMSXSAMMMMSMAMXSSSMMMSMMSXMAMMMMMXAAMMXASMASXMSAS
SSMXMXAXAXXMSAMAAMAMAMXMXXAMMMMSMMASXMASMSSMAMMMMSAMSSSXMAMXMMXMMMMMXMSXMASXAMAXXMMMAXAMXMAMXMASXSASAMMXMAXAMAMAAAAAXSASXXMSMSMMMMXSXMAAASAM
MAAASMMMSMSXMASMMMXMAMXMAMXMASAAAAXAMXMMXAASXMSMAXMAAMAASMSASMSAXSAXAMXMXMSMMSAMMASMSMAMSSSMXMAMXSAMASASMSMAMXXSXXMXMMAMXMAXAAAAXMASMSMMXMMS
MMMMXAMAMXMASAMXMASMXMXMASMMAMSXMXSXSAXMMSXMXAAMASXMMSSMMASASAAMMSASXMMSAAXXXMASXAXAAMAMXAAMAMASMMXMSMAMAXMAMXXMMSSMMSSMMMASMSSMSSXMASXMXXXA
SASMSSMASAXMMSAMXMSXSAMSASAMAXAMSMSASAMXAMAMMMMMXAXMAAXAMXMAMAMXAMMMXAASMSMMMSAMMMMMMSAMMMMMAMAMAMXMAMXMAMSSSMSAAAAXAAAAXMASAAXAXXAMSMAMSMXM
SASXAASMMMXXAXMAAXMAMMAMAMXMSMSMSAMXMAMMXSAMSSMSAMXMMMSXMMAXXAXMSXSAMMMMAXXAAMMXMAXAASXXAMAXMMSXSXAXASMMXMMASASAMSSMMXSMMXAMAMMMMXMMXSMXAAAX
MXMMSMMMAMMMSMMSMSMXMAXMSMSMXAAAMMMMSAMXXMAMXAMXMASXAAXAXAMMXAMXXXMASMSMXMMMXSMASASMMMASXSSSMAMAXXASAMXAMXXAMMMAMAXAMAMMMMMSXSAAAASAMAXSMSMS
XSXAAMMMAAAAAAXMAXMMASMAAAAAMSMMMXSASASMMMSSMMMSMAMSMSSSMSAMSMSMSXSAMXAMMXMAXXXAMXAMXMAMXAAXMAMMMMMAMXAMXMMSMXSAMXSXMAMAAAMAASMXSAXAXSMSAAAX
MAMSXSASXSMSSSMMAMAXAAMXMXMMMAAXMASMSAMAAAAAAAAXXAXXSAAAAXAAAAAAAMMAMSXSMASMSMSMMSSSSMMMXMMMMXSAMMXAXMAMAMMMAAAXSMXMMMSSMSMMMMAXMXSMMMAMSMMM
AMXXAMXSXAXAMMMSSMMMMSMXMXMASMSSMASAMMSSMMSSMMXSSMSXMMSMMXMSMSMMMMSMMSXMXMMAAAAAMAAAXAMMXXSXMAMASMMMMXAMMSASMMMXSAMXAAXXAAXXMMMMMASAAMAMAMXA
SXMMMSMSMSMXSAAAAAXXMAXAAASASAAAMAMAXAAAXMAXAXMMAAXMMAXMAMXMAAMXSAMAAXAMASMXMXSSMMSMSXMASMMMMASMMXAAASMSAMXSMSXMMMMSMSSMSMSMMAAAMAMMMMASAMMS
AMXAAAXXAXAAAMMSXMMXSASMSMSAMMSSMMSMMMXXMMASMMMSAMSAMMMMSAMMXMSASAMMMSASASMMSAMXAXXMAXXXAAAMMMSXASMSXMSAMXXMXSAMXXXXAAMAAMXASMXSMMSAXSASASAX
MASMSSSMSMSMXMAXXSAXMASXAASXXXAXXXAMAMXSXMAMXAXAAMXMMXASASMAMSMMMAMXMXMMASAASAMXSMXAASMMSMXMAAMMMMXXAMXMASMSASAMSSMMMMMXMSSMMSMAAMAMXMASXMXS
XMXMAMAMMAMXXXAMXMASMMSAMXMMXMASXSXSMSXAAMSSSSSSSSSXMSMSAXMMSAAXSMMMMASMSMMMSAMAMMXSAMXAAAXSMMSAXSMSXXAMXMASASMMMMAXMASAMAAXAAMSMMXXAMAMAXAX
SAAMMSAMMXMMSAMXSMASAMXXXXXASMMSXMASASMSMMAAAXMXAAMXMAAMXMAMSXSMSAAASASXAAMAXAMAXAMXAMMMMXMAMXMASXAXMSMXXMXMXMXAASMMSASASXMMMSXMSAMXMMSSSMSA
XSXMAXASMAXAXAMXMMMSAMASMMASAAASAMMMAMAAMXMXMAMMMMMMSMSAASXMSXMASMMMMAXMSSMXSXMSSSXSAMXMASMSMSSSSMMMXAAMSMMSSMSXMXAMMMXXMAXAAMAMXMASXMAAAAAM
MAXMSSMMXMSSMMMXXAXMMMASASMXSMMSAMAMAMSMSAXSXMXSAMXAXMXMMXASXMMAMSSSMSMAXXMMSXAXAMASXMMMMSAAAAXAXAAASMSMAAASAMXMSSSMXASXMSMSXMAMMXXSAMMSMMMX
AMXXAAXMAMAAAXAXSMSAAMXMAMXAMXMSAMXMSMMASMSSMMMSAMXSMSMMMSMMAXMSMAXAAAMSMSAAXMMMAMAMAAAXAMXMMMSMSSMMSAAMMMMMMMSXAAAMMMSAAXAMXXXMXMASAMAXAXXM
SXMMSSMSMMSXMMSMMXSXMXMMAMMSSSXXAXAXXASAXMAMAAAXXAXMXSAAAAASMMXXAMSMMMXAASMSSXSSMMASMMXMMSMXXXAXAAAAMXMSXSSSMASMMSMMAXMMMMAMXMSSSMXSAMXSMMMA
XAMXMAMAXAXAMAMAMAMXXAAMAMXMAMAXAMSXSAMXSMMSMMMSASMSASXMSSMMMXSMSMAXMXSMMMAAAXMASMXSAMXSXMMMSSMSSSMMMXXAAAAMMASXMAXSMXMXMSAMASAAXAASMMAMASAS
SAXSAMXXMMMMMAMMMXSAMXSMAMMMAMXSAMXMMXMMXAASMMMMAMAMAXXXAXMASMXAAMXMXAAAXXXMMMSAMXAXAXASASXAMAMAMXMMSSSMMMMMMMSMXMXSMSMAMSXSXMMSMMMSAMXSAXSM
SAMXXSMMXAASMMSXSAMXXAAXXMAXXSAAXSAMXMASXMMSAXXMAMXMSMSMMXSAMXMSMSSMMMSAMXMMXMMAMMXMAMASAMMSSMMMSMXXAAXXAAAMXMSMMSAMXAXAXSMMAAXMAMAXMAXMXMAM
XXAXAAAAMXXSAXSAMASAMSSMMSXSAAMMMSXXSAXXSAAMXMMXXSXAAAAAAAMASXXMMAAAAAMAMMAXASMSMSMXMAXMMMAXXXXXXXMMMSMXSSMSAMXAAMASXMSSMMASMMSSSMASXSMASMMM
MASMSMMMSMAMXMMASXMAMAAAXAMXMMSXAXXMASAAXMMMXXSAAAMSMMMMMXMAMXMAMMSAMXXAMSSSXSAXASAAMSMSASMMSMMMXMASAAAXMXMAMXMMMSXMMAAMSSXMMAXAMXAMXAMAMAMX
AMXAXXMAXMAMAXXAMXMXASXMMMSSXXXMMSMXAMMXMMMSMAAMSMMXMMSMMMMSSMSAMMMMMSMAMXAAMMAMAMXMXAAXASAASAAAASMMSSXMMAXAMXMSAMXMMMMSAXAXSXMXMASAMMMASAMS
XXMXMAMXXSMSMSMMSMAAXASXSAAXSASMMAXMASXASAAAMXMAMXAMXAAAAAMAAXSASXSMAAXAMMSMAMAMMMASMMXMAMMSMSMSXSAMXXAASMMMSAAMASASMMMMMSMMMAMMMMMAMXSASMSA
SSMSMSMMMMAMAAXSMMSMSASMXMASMXMASAMSAMXAMMSMMXXASAMMMXMMMSMMSMSXMMMMSSSMSAMXSSXSMMMSAAMSAMXAAAMMASMMAXSMMAAASMSMSSXSAASAXAAAXAMAAASAMXMASXMM
XMAAMAMAAMAMSMSAXAAAMXMAMXMXMXSAMXMMSSMMSXMASMMXSASXXSXSAAASMMXXAAAAAAMXMMSMAMMMXAAMMXMSASMMSMXSAMXMAMMXMSXMXSAXAXAXMMSMSSSSSSSSMMSXMAAASMSX
MMSMSASMSXXXAMXMMMSXMAMSMASAMMSASXAAAXAAAASAMASMMAMAAAAXSSXMAMMMSSMSMMMXMASXXMASMMSSXMXSAMAMXXAMASXMXMMAXXMASMXXMMASMMMMAAMAAXMASMXMXXSAXAAX
AAMAMXSXMXSSXXAXMXAASMXMMXXASASAMMMMMSMMMMMAXXMAMXMMMMSMMMMMAMAXXMAMAMXMMMSMMXMXMAXXAXAXMSAMXMXSAMAXAMXMSAXMMMSAXMAMAASMMSMMSMMSMSASXMAXMXMX
MMSSMASAMAMAMSXSAMMMMSASMSSMMMSXMAXXXMAMSASAMSSMMAMXAXMAXAAMSXSMSXMXAXAXSXMASASMMSMSMMXMASMSAMASASXMASAMSAMXAAMMXMASXMMAAXAAXAXMAMMMAAAMSMSM
SXAAMAMAMAMAMASMASMAASXMAMMXMXMXMAXMXMAMAMMAMXAASAMSMSSSMMSAMXMMSASMSMSSXASAMAMAAXMXAXXAMSXSASMSAMXMASAXSMXSMSXSASXSAASMMSMMSMMMSMAXSMMSXAXA
AMSSMSSMXSSXSSMSAMMMMMAMMMSASAAXSAMMMMASMMSXMSSMMXASAMAXXAMXSMMASAMAMAXMMMMMSSSMMSASMMMSAMASAMMMAMXMASMMXAASAMASAMASMMMMXXAXMAAAMMXMAAXSMMMS
MAMAMXAAAMXMXAAMXXXMMMXMXXSASXSXMASAAMXXXMMSAAAXAMXMAMMMMXSMSAMAMXMAMSMSXXAMAMXMAXMAAAAAAMXMMMXSXSMMASMMMMMMAMMMSMMMXSASXSSSMMMMXAXXMMMSAMXX
XXSAMSMMXSAAXMMMSMMSAMAXXMMMMMMAXASMSSMSSMAMMSSMAAXSXMXMXMAASMMASASXMAAAXSXMASMSSMSSSMXMXMXMAMMMMMAMASAXXAMSSMMAXXAMMMAXAMAAAXMAMSMSAAXSAMAS
SMSAMXMAXMAMXXSAAAASASXMASAAAAXXMASXAAAAXMASXXXAMSMMXSAXAAXXSASASMXMSMSMMMMSXMXAAAAXAXXSSSMSASAXASXMXSXSSMXAXAMXSXMSAMSMSMSSMMMASAAMSMMMMMAS
MASXMMMSSMXSAAMXSMMMAMXASMSSSSMSMXXXMMMMXSAMXSSSMMMMASASXMSASAMXMXAAAAXXAAAAMXMMMMMSXMAXAAXSASXSXSXXXMXMASMASXMXMXXMXMXAXAAAMXSXSMSMMMSMMMXM
SMSXXSAAXMAMMSMMXAMMAMMMXAAMAAAAMSMSXASAMMMSAMXMAAAMMMAMAAMMMAMAMSSSMMMSSSSMMXMAAAAMASMMSMMMAMASMMMMAMAMMMXXAMXAMASXSSMMMMSSMASAXXXAXAAMSMSX
MAMAMMMMSMMSMMAXSAMSSMSAMMMSXMSMXAAMXXMXMAAMASAMMSMSAMXMXMMAMAMXXAAAXSAMXMAAXAXSMMASMMSAAXAMMMMMAASMMXXXSAMXXSSXSAXMAAAXAXAAMXSMMMMSMSMSAAXM
MSMSMASXMAMXASXMMSMSAMMMSAAXXXAMMMXMMMSMMSXSAMASXMASMSMMMMSXSMMSXMSMMMMSSXSMMMMMASXMAAMSMMSXMASXSMSAXMSMMMXMXAAAMMSSSMMXMSXMAMMASXAXXMSSMMMA
AXAXAASMSAMXMMSMAMXSSMAXSMSSSSXSAMAASAMMAXAMXSAMAMAMAAXXAAAAAAAAAMMMXXMAXXAXASAMXSAMMMMASMXMSASXAASAMXXAAAASMMAMMSAMXXXXXAMXMASAMMSSXMAMAASM
SMXMMMSXAXXXAAXMASXMAMSXXAMAMAASAMSAMASMMXAMASXMAMSMSMSSMSXMSMMSXMASXSMASMMMMMMMAMAMSMSASXXAMMSXSMSASAMSMSXXAXMASMMSSMMXAASXXMMMSAAMMMXMMMSA
MAMXAMXMMASXMXSMSSMSAMXAMSMSMMMMXMXASAMASMMMAMASASXAAAXXAMMAXXAXAMXMMAMASAXAXAMMSSMMMXMXMXSSMXXAMXSXMAMMAXASMMMSXMAMAAMSSMMXAXAAMMXMASMMXAMX
SMAXXSAMXMSAMASMAXAMASMAMXAMXAXMAXXAMAMAMXAMSSMMSMMXMMMSXXASMMSSXMAMSXMAMMMSSMSAMAXMSAMASASAMXMXMAXASMMSAXXAASXMASMSXMMAMSSSMMSXSAMSMSAASMMM
SXSMAXMMAMXAMAXMXMMSAMXMSMSMSSMSAMMSMMSAMXMXMAMMAXAMMSMAXSMMAAAMASMMMMMMSXAXAAMASMMXSASXMXSXMXAAMXMXMSAMXMMSMMASAMAMMMMMSAXAAAXAXMMAXMMMMAAX
SAMMSXXXASXSMSSSMMXMXSXMAAAAMAXMASXXAMXAMAMASMMSMSMASAMXMMASMMXSAMMAMXMXAMXXMMSMMAXASAMXMAMXXASXSSXSAMXSAAXAXMAMXMMMAMSXMMSSMMMMMMSMSSXXSSMS
SAXAXAMSMMAXAMAXAMAMXMASMSMSMXMSSMXMMMSXXXSASXAAMAMXMXXSASAMAMXMASMXMXMAAAMMSASXSSMMMXMAMMSSMAMXAASMXSXSXSMXXMXSAMXSXSMAAXXAMXAXAXAXSMAXMAAA
MAMAMSMAAMAMAMAMMMAMASXMAXXXMMMXAAXXSAMXSXMXSMSSSMMSMSMMAMAMAMASAMMMMAMMXSAAMAMXAAAMAMSAMSAMXAMXSMSSMSAMAMASMMMMASAXMAXXMSXMASASMSMMSAMMSMMM
SXSXMAXMMMXSAMASXXXXAMXMAMMMSAMSMMMMMASXAAMASAAMAMMSAAXMSMMSASMMMSMASAMXAMMMMAMSSMMMAXMAMMAXSXSXXXMAMXAMXMAAAAASMMASXSSMMXMMXAAXAAXASAMXXASX
AMMAXASMSXMMAMAXAASMSMSMMXSASXMXMMSXSAMXMMXAMMMXSMAMXMAMAAXAAXXAMAXMXAXAAMXXXAXMAXMMXMSAXSXMMMMMMMSMMMMMXMMSSMXAMXXXXAAXXAXXAMSMMMSXSXMASMMM
SMMXMXXMAASMSMSSMXMAMAXXMAMMMMXASASXMAMMXMMMXMSAXMSSMXMSSSMMMMSAMXSXSAMSXMXMSSXSMMMSAXSMMSMAMASAAMAXMAXAMXAAXMASXMSMMSMMMMSMMSMXAAMMMMMXXMAS
MAASMMSMSMMAMAMXXASMMMMXMASXSXSAMASMSSMAAMASAAMASXAXMAMMAAAXXAXXASAMMAMMASXMAMAAXAAMMMMXAXAXSASXSMMSMSMAMMMXSMMXAAAXAAMAAAAXXAMXMSXMAAXASMXX
MMMSAAXAMMMAMAMMMMASMMSSSMSXAXMSMXMMAMMSASASMSMMMMMSXSSMMSMMMXSMMMASMXSMMMAMASMMMMMSXSSMSXSAMXSAMAXSAMSAMXAXSAMSMMMMSXSSMMAXMAMXXMAMSMSASMMS
XSXSMMMXMXMAMAMAAXMAXAMXAAMMMAAAXMAMAMAXMAMMXAMMMSXAMMAMAAAASMXAXSSMMASAMSXMASAAXMXSAMXAAAMSMMMAMMAMAMSXMMSXSAMMASXAMAXASXMXSAXSSSSMAAMMMMAA
MSAXMAAASXSXSMSSSSXSAMSXMMMAXSMMMSASXSSSSSSSXXXAAMMSXSAMXSAMXMASAMXAMASXMXMMASAMXMAMXMASMMMAXXMAMXMSAMXSMXXASXMXAMXSMXMAMXAAMMSXAAXMMMMSAMSS
AMXMMMMMMAMXAAMAAMAMMASXSASXMXAXXSASAAXAAAXMASMMMSAMMMAMAAXMASAXASMXMAMAMXAMXSXMAMASAMAXXMXASXXAXXASASAAMAMMMMSMMMXXXMMXMMMMSMXMMMMMXSXMAXXX
XMMSXSXSMMMSMMMMXMAMXMMASASMMSXMAMMMMMMMMMMMMMAMMMMSASXMASMSMSMSMMMAMMSMMXMSASAMASMSAMASASXASMSSXMMSMMMMMAXAAASASAXMMMXASASAMMXMXMAMASASMMMS
XSAMXMAXAAAAAMXSMMAMAXMAMSMAXMAMXSSMMXSAMXAXASXMXMASAMXMSMMXAXMAMAMXXAAXSMMMASAMASXSXMASAMMAMAAAASXSAAXXSXSMXMXAMMMSAAMSSXMASMSMASAMAMMMAXAM
XMASMMAMMMSSSMXMASXSSSMSSMSMAMAMXAAAAASASMSSMSAMAMMMAXXMAAMMAMSASXMXXXSXMAXMXMAMASXMASMMXMSSMMMSMMAMMXSAXXAXSXMMMXAXSXSXMASXMAAXAXMMAMXMMMSS
XSAMASXSXAXXMXMXAXAAAXXMSAASMSXXXMSMMXXXMAAMXSASXSMSMMSSSSMMMMMASMSMSXXASXMMMSMMXMASAMXAAXAAXMAXAMXMAXMAMXXMAMMSAMXMMXAXMASAMXMMSSSMMMSAXMXX
MMASXMAXMMMXMAAMXSMMMMSMMMMSMAMSMXAMXMSMMMMMAMMMMXAAXXXAMAMXAAMMXAAAXASMMAAAAAXXASAMAAMXMMSAMXXSXMMMMSMXMSSMXSASASXAAXMMMAMXXSAXAAAAAAMAMXXX
XSMMMMSMMAAAMMSAXAXAXAXAAXXXMAAAAXMSAMAAAXXMAXMAMMSSSSMXMASMSSSMMSMMMMMXMMXMMXSAMMASMMXSXMASMSXMAAMAAAXXMXAAAMXSAMMMAMXSAMXAXXAMXSSMMMSASMSM
MSAMXAAASMSSSMXAMMSMMXSMMXSASXSSSMASASMSMSSMAXSASAAAMAMXMASXAMXMAMAXAXAAMSSSXMMAXAASASASXSAMMSASXMSMSSMSMSMMXXAMXMASXMAXMSMXSSXXAMAXAASAMAAA
AMAXMAMMMMAAXAXXAXAMMMXAAAMMMAAAAMXMAMMMAMXMAMXAMMSMSAMXXAMMXMXMAMXSMSMXSAAXMASXMSXSAMASAMAXAMAMAAXAXMAAMXXXSAMXXAAMAMMXXMAMMAMXMMMMAMMMMSMX
MSMMXSSSMMXSMMMMSSXSXMMMMXSMMSMSMMAMAMXMAMXMASMAMMMXSASXMASAASXSMMXSAAXSMMSMXAAXAMAMXMAMMMSMMMAMMMMSMMSMSXMASXMMMMMXSASMMMSMSASASAXSSXMAMASA
MMASAMXMASXMAXAAMAMMASXMMXAMXXAAXSAMXMASAMXSAXXAMXAXXMAXSSSMMSAAASASMMMXASXAMMSMAMXMSXMXSAMAXSASXSMMAMXXMAMXXXXAAAAXXAAAAAAXSASASMMAAMXXSASX
MSAMXMASXMASAMMSSMASAXMASMMMMMSMMMASAMXSAMAXXMMMMMXMAXMAMXMAXMXMMMASXAXSXMXXAMAAXSSSMASMMMSAMSASAAAMMMSMMSXMASMSSXSMMXMSMSSXMAMAMMSMMSSMMXMX
AAXMMMMSASAAASAAAXAMMMMAMXMAXMAMMXXMAMASAMXXSMSASXMXXMSMMSSMMMMXXMMMMXXSAMXMMSASAMXASAMAAXMMMMAMMMSXMASAAAMMMAMAMXMXSAXAXAXXMAMXSAMXXAAASMMX
MSMMXSASAMMSMMMSSMMSXXMXSASMMSASAAMMXMXSAMXAMASXSAMSSMSAAAAAAMAMSMSASMMSAMXSXAMXMXSMMMSSXMASXSMSXAMAMASMMXXAMXMXMAMASASXSMMXXXXAMASAMXSSMAAX
AAAXASAMXMXAXAXXXASAMSMMSASAASMMMXSAXSMSXMMXXAMMSAMXAASMMSSSMMXAAAMASXAXMMAXMAMAMMSXMMMMXASXMAASMSXXMMXXMASMSMMMSMMMSAMMAMASXMSMSXMASXMAMSMS
SSSMXSASMSSSSMMSAXMAMXAAMXMMMSXMAAMMMXAXAXMMMMSAMAMXMMMMXXAAMXMSMSMAMMMSMMMSXSMASAMAXMAMXMAAXMMMMAMSXSSSMXSAAXMASAAASAMXAMXXAAAASASXSMXSXMAS
MMAMXSAMAAAAAAAAMMSMMSMMSASXAXMMMMSMAXSMMAXAAXMXSSMSXSASXSMMMMMAAXMSAXMAMASXAMSAMASXMMMSSMSMMMXXMAMXAXAAXAMXASXSSSMXMAMSXSXSMMMMSAMAMAAMAMAM
SXSMMMMMMMMMMMMSMAXAMXAASXSMSSXAASAMAMXAXSSXSASMXMAAAMAMAAAAAXMXSXXAMMSSSMSMMMMXMAMMSAMAXMAXAMXMSMSMMMSMMMSAMXMAMAMASXMMMMMAXAAMMMMAMSMXAMXS
AAMXXAASAMXAXAAXMSSMMSMMXMMXMAXSMSASMSSXMXAXMASMMMSMMMAMXMMMXMMSAMXMAXAMAMXAXAMMXASXSXMXSXSSSSMXAAAAMXMXXAAXXAMMMMSAXXAAAXMMSSMSASMSXMMSMMAA
MSMASMMSXMSMSMSSMAXMAXMXMASAXMAMXSAMXAMMMMMMMAMAXMXMXSSSXSAMSSMAAMMXXMXSAMXSMAASXXMAXAMAMMAMXAXXSSSSMAMXMASMMMMSAAMXSSSMXMAAAAXSASXMAXXAXMXM
XAXAAAAXAMAMAMXAXAMMSMAASXMXSMXXMXXSMMMMAAAMMMSMMXAMMMAAXMAXAAXXMMXSMMXSXSAASXMAMMMXMASAMASASMMXMAMXXAXAXMAXAXASMSSMMXAAAMMMMSMMMMASAMSMSSSS
SMSMSMMMXSASMSSSMXSAAASMSAMXMASMMMMXAXMMSSMMAMAMMSMXAAMMMSSMSSMSXSXMAXAXXSAMSSSMSMAASXMASAXMMASXMMASXMXSSMXSSMXSAAMAASMMMMMAAXAAASAMAXXAMAAA
SXXAMXSXAXAMXMAXXMMMSMXXSAMSAMXAAAXMSMMMAXMSMSASXMMSSSXXXAAMXAAXXSXXSMMSAMAXXAMAAMSMSAXXMAXASMMXSAAXXAXXAMAAMXMMXMAMMXAMAMSAMXSSMSXMMMMSMMMM
MXSXMAMMSSMXMXXMMMAAMAXAMAMXAMSMSXXAAAXMAMXAXXXXAAAAXXXMMMMSSMMMMMSAXAMAMSMMMMMSMXMXXMASMMSAMMXXXMAMMSMSAMMSMMMAMXXMSSSMAXAAXMAXAXMAAAXXAMXX
MAMMMXSAASAASMSAAMASXMMSMSMSMMSXAAMSMSMMAMSSSMASXMMSSMSMMSAXMASXMAMXXMMMXAAAAXMXXAXAMXXXAXMMMXMMMMSMAAAMSMXMASMAMSMXAAXMMMMAMXXMXMASMSSSSMSM
MXSASXMMSXSXSAASXMAXAMXAAAAXMAMMMMMXAXXXAXXAAMAMXAXAAAXAAMASMXMXMASMSSMXSSSMSSMAMSSMSMSMMMMASAAMSAAMSMSMAXMMAMXAMXMMMSMSMAXSXMASASXXMAXAAAAA
SSMXSAAXAMMMMXMMMMMSAASMSMSMMMXSXXSMMMSSMXMXMMSSSXMXMXMMMSSMMAMXSASAAAXXMAXXXAMAMXAMAXAAAMMAMASXMSXXAAXXMSASMSSMSAMXMAMAMSMXAXASASXMMSMMMSMS
MAMASXMMSAAAMAXAXAXSMMXMAMAAMMASMMMASAMASXAASMMMMAASMSAAMXAASMSMSMSMSMMSMMMMSMMMXXAMMSSXMSMXSMMAMXSSMSMMXXAAAAMMSMMASASASAXSXMMMAMXMAMAAAAXA
SMMASASMASMSXMSMMMXXSXXMXSMSMMASAXSAMXSAAMSMMAAAXMXAAXXMSSSMMXSASASXXAMXAXXAAXAAMSAMXAAASAXMAXSAMSXMMAAMSMSMMMSAMASASASXSMXSAMXMXMXMAXSMSMSX
AXMXMAXAMXXMXAAAMSMMAMSMMSAXXMASXMMXSMMMMXMASXMSXXMMMMSSXMMAXXMAMAMAMASMMMMSMSMXMAMXMMMMSASMMMMXMMAXXMMMAAAXAXMASMMMMAMXXMASAMASAMAMSXMXXASM
MMSSMMMSXSASMSMSMAAMMAAAAMAMXSXMXAMAXMASXMMMMXAAASAMXAXAAXSSMXMAMAMAMAMAAAXAAAASMMMXXXXXMXMMXAAAMMMMMSASMSMSMSSMMXXXMAMSSMMSXMASASMSMASAMASM
XAAAAXMAAMAMAXMAMXMMXSSSMMSMAXASMSMSMSAMAASXSMXMASASMMSSSMAXASMMSMSMSAMSMMMXXMMMAAMXSAMSSMMSMSMXSAMAAMXMXAXAMMAAXSMMXSSXAXXXAMMSAMXAMXMAMASM
MMMXMMMMXMMMSMSMSSMSXMXAAXXMAXXAAAAAMMMSMMMAXXXAASAMAMXAMMXMMMMAAXAMMXMMAAASXSASMMMSMAMAAMXSAXAASAMMXMAASMSSSSMMMSAAAXMXMSMMAMXMMMSXMMXXMAMX
MSSXMAAXAAXXMXMXAAXSASMSASMSASMMSMSMSXAAAAMMMMSMMMMSSMMAMMMSXAXSMXMSASMSXMMSAMMXAAXXMAMSSMXMAMAMMXMAXXMMAMAAMAASASMMMSAMXSAXSXMASAMXMAXSMSMS
AAAAMSSXMSSMSAMXSMMSXMAXAAAAAAXXAXXAXMSSSMMXAAAXXAAMAMMSSXAASXMASXXMXSXMASXMAMXXXMMSSMXXAAAMXMAXSSMMMASXSMMSMSMMASAAXAAMASMMAASAMXXSXXXAAAMA
MMSSMAMMXMAXSXSAMAAMMMSMMMSMSMSSXXMXMXAXXXXSMXSMMMSSMMAMAASMAMSAMXXMASASASASXMMSAAXXAMMMMMMMAMMSMXASXMSAMSAAXAXMXMMSSSMMXSXXSAMMSAXSASAMSMSM
XXAXMAMMASMMXMMAMMXSAAAAXAMXXAAAMSMSAMXSMSMSAAXMXAMAMMMMSAMXMMXAMXMXASAMASXMXAASXMMSMMSAAAMXSXSAMMAMAXMAMMMMSXXXMMSAMXAXAXXXXXMAMMSMAMMXMAMX
MMMSMMMSASXAAASMMAXSMMSSMMSMMXMMMAAAMAMXAXAMMMMAMSMMMXSAMAXXXXMSAMXSXMXMAXMMMMMSASAAXASXXMSAMMSASMSSMMMSMSSMMMMAAXMASXMMXSMMMXMASXXMAMXMMAMM
AAMXMAMMAMXXMMAAXAAXAAXXAMXAAXMSSMMMASAMXMSMSASMMXAAAASXSSMSMSAMASASAMXMSSMXAAAMMMAMMASAXSMXSASXMMAAAXMAAAAAAXSASMSMMMMSAXAAAXSXMMMSXXXAMXMA
SXSASXMXASXSMMSMMXXSMMMSSMMSMMSAMXXXAMAMSAMASAMXAMSMMMSAXXAAASASAMASXMAAMAXASMSXXXMXSXMMMAASMMMSAMXSMMSMSMSMMMSAXAAAMXAMMMSSSMMAMMMAMMMSXASM
XASASAXSASASXAAAXMXMASXAXXAAASMMXSAMXSAMMSSMMSMMMMXMSAMXMMSMXMMMXMXMASMSMMMAXAMMSXMASXMAXMMMAXAXXSAMXAXAMXXAMXMAMSMSMMXSXAXMAMSAMAMASAAXSMMX
MAMAMAMMAMAMMSMSAMMSAMMXMMSSSMAAXMSAASASAASMAAXASAMXMASASAXSAASAXMASAMSAASMXMAMAMXMASASMSXMSAMXSAMMSMASXMASXMAMMMXMXAXAMMSXSAMXASXSASMSMSXAM
MSMSMAMMAMXMAMMXMAMXSSXAXXXXXXMMSAMXMSSMMSSMSSSXSXAXSMMMAXMASXMMXSAMXSMSSXAMSXMASAMXSAMXSAMXMAAAXSXXXMAMXMASXXSMXMASAMXXSAMXXSSMMXMXSMMAMXXS"""


lines = input.strip().split("\n")

arr = [list(line) for line in lines]


def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY





# def search(sizeX, sizeY):
#     total = 0
#     for y in range(sizeY - 1):
#         for x in range(sizeX - 1):
#             if search_up(x, y, sizeX, sizeY):
#                 print("search_up")
#                 total += 1
#             if search_down(x, y, sizeX, sizeY):
#                 print("search_down")
#                 total += 1
#             if search_right(x, y, sizeX, sizeY):
#                 print("search_right")
#                 total += 1
#             if search_left(x, y, sizeX, sizeY):
#                 print("search_left")
#                 total += 1
#             if search_up_right(x, y, sizeX, sizeY):
#                 print("search_up_right")
#                 total += 1
#             if search_down_right(x, y, sizeX, sizeY):
#                 print("search_down_right")
#                 total += 1
#             if search_up_left(x, y, sizeX, sizeY):
#                 print("search_up_left")
#                 total += 1
#             if search_down_left(x, y, sizeX, sizeY):
#                 print("search_down_left")
#                 total += 1
#     print(total)

def get_next_char(x, y, next_char, grid):
    if (isValid(x, y, 10, 10)):
        if (grid[y][x] == next_char):
            return True
        else:
            return False
    else:
        return False


# def search_all_dir(max_row, max_col, grid):
#     total = 0
#     char = ['X', 'M', 'A', 'S']
#     counter=0
#
#     after_y = 0
#     after_x = 0
#     before_y = 0
#     before_x = 0
#     found = False
#
#     for y in range (max_row):
#         for x in range (max_col):
#
#             after_y = y+1
#             after_x = x+1
#             before_y = y-1
#             before_x = x-1
#
#             if (isValid(y, x, max_row, max_col)):
#                 if (isValid(before_x, before_y, max_row, max_col)):
#                     if get_next_char()
#                 if (isValid(x, before_y, max_row, max_col)):
#                     return True
#                 if (isValid(after_x, before_y, max_row, max_col)):
#                     return True
#                 if (isValid(before_x, y, max_row, max_col)):
#                     return True
#                 if (isValid(after_x, y, max_row, max_col)):
#                     return True
#                 if (isValid(before_x, after_y, max_row, max_col)):
#                     return True
#                 if (isValid(x, after_y, max_row, max_col)):
#                     return True
#                 if (isValid(after_x, after_y, max_row, max_col)):
#                     return True
#
#
#
#
#             if (counter == 3 and get_next_char(x, y, char[counter], arr)):
#                 total+=1
#                 counter = 0
#             elif (counter != 3 and get_next_char(x, y, char[counter], arr)):
#                 counter+=1
#     return total

def search_right(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            x+=1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                x+=1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    x+=1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_left(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            x -=1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                x -=1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    x -=1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_up(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            y-=1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                y-=1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    y-=1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_down(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            y+=1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                y += 1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    y+=1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_down_right(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            y += 1
            x += 1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                y += 1
                x += 1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    y += 1
                    x += 1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_down_left(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            y += 1
            x -= 1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                y += 1
                x -= 1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    y += 1
                    x -= 1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_up_right(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        if arr[int(y)][int(x)] == "X":
            y -= 1
            x += 1
            if not isValid(x, y, sizeX, sizeY):
                return False
            if arr[int(y)][int(x)] == "M":
                y -= 1
                x += 1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "A":
                    y -= 1
                    x += 1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "S":
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

def search_up_left(x, y, sizeX, sizeY):
    while True:
        if not isValid(x, y, sizeX, sizeY):
            return False
        while isValid(x, y, sizeX, sizeY):
            if arr[int(y)][int(x)] == "X":
                y -= 1
                x -= 1
                if not isValid(x, y, sizeX, sizeY):
                    return False
                if arr[int(y)][int(x)] == "M":
                    y -= 1
                    x -= 1
                    if not isValid(x, y, sizeX, sizeY):
                        return False
                    if arr[int(y)][int(x)] == "A":
                        y -= 1
                        x -= 1
                        if not isValid(x, y, sizeX, sizeY):
                            return False
                        if arr[int(y)][int(x)] == "S":
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return False

sizeX = len(arr[0])
sizeY = len(arr)
total = 0

for y in range (sizeY):
    for x in range (sizeX):
        if (search_up(x, y, sizeX, sizeY)):
            total += 1
        if (search_down(x, y, sizeX, sizeY)):
            total += 1
        if (search_right(x, y, sizeX, sizeY)):
            total += 1
        if (search_left(x, y, sizeX, sizeY)):
            total += 1
        if (search_up_left(x, y, sizeX, sizeY)):
            total += 1
        if (search_up_right(x, y, sizeX, sizeY)):
            total += 1
        if (search_down_left(x, y, sizeX, sizeY)):
            total += 1
        if (search_down_right(x, y, sizeX, sizeY)):
            total+=1


print (total)
# print(search_all_dir(sizeY, sizeX, arr))

